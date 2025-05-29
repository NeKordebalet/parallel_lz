import asyncio
from n1 import Logs, Zowoo, ThreadedSearch
from n2 import multiprocessing
from n3 import asyncio_task

def threading_task():
    print("=== ЗАДАЧА 1: Поиск слова 'error' ===")
    creator = Logs()
    creator.generate_files(50)          
    files = creator.file_list           
    search_word = "error"

    print("Запускаем обычный поиск...")
    zowoo = Zowoo(search_word)
    zowoo.execute_search(files)        

    print("Запускаем поиск с 2 потоками...")
    thread = ThreadedSearch(search_word)
    thread.execute_search(files, num_threads=2)

    print("Запускаем поиск с 4 потоками...")
    thread.execute_search(files, num_threads=4)

    print("Запускаем поиск с 8 потоками...")
    thread.execute_search(files, num_threads=8)

def main():
    while True:
        print("Выберите задачу для выполнения:")
        print("1 — Поиск с потоками | 2 — Поиск с процессами | 3 — Асинхронный поиск | 0 — Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            threading_task()
        elif choice == "2":
            multiprocessing()
        elif choice == "3":
            asyncio.run(asyncio_task())
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()