import asyncio
import random

async def producer(queue):
    try:
        while True:
            item = random.randint(1, 100)
            await queue.put(item)
            print(f'Производитель добавил: {item}')
            await asyncio.sleep(random.uniform(0.1, 0.5))
    except asyncio.CancelledError:
        print("Производитель отменён")
        raise
async def consumer(queue):
    try:
        while True:
            item = await queue.get()
            print(f'Потребитель обработал: {item}')
            queue.task_done()
            await asyncio.sleep(random.uniform(0.1, 0.5))
    except asyncio.CancelledError:
        print("Потребитель отменён")
        raise
async def asyncio_task():
    print("ЗАДАЧА 3")
    queue = asyncio.Queue(maxsize=10)
    producers = [asyncio.create_task(producer(queue)) for _ in range(2)]
    consumers = [asyncio.create_task(consumer(queue)) for _ in range(2)]
    await asyncio.sleep(5)
    for p in producers:
        p.cancel()
    for c in consumers:
        c.cancel()
    await asyncio.gather(*producers, *consumers, return_exceptions=True)

if __name__ == '__main__':
    asyncio.run(asyncio_task())
