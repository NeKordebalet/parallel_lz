import asyncio
import random
async def producer(queue):
    while True:
        item = random.randint(1, 100) 
        await queue.put(item)  
        print(f'Производитель добавил: {item}')
        await asyncio.sleep(random.uniform(0.1, 1))  
async def consumer(queue):
    while True:
        item = await queue.get()  
        print(f'Потребитель обработал: {item}')
        queue.task_done()  
        await asyncio.sleep(random.uniform(0.1, 1))  
async def main():
    queue = asyncio.Queue(maxsize=10)  
    producers = [asyncio.create_task(producer(queue)) for _ in range(2)]
    consumers = [asyncio.create_task(consumer(queue)) for _ in range(2)]
    await asyncio.gather(*producers, *consumers)
if __name__ == '__main__':
    asyncio.run(main())