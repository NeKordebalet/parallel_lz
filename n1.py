import random
import string
import threading

class Logs:
    def __init__(self):
        self.file_list = []

    def generate_files(self, count=10):
        error_index = random.randint(1, count)
        for i in range(1, count + 1):
            filename = f"log_file_{i}.txt"
            self.file_list.append(filename)
            with open(filename, 'w', encoding='utf-8') as f:
                if i == error_index:
                    f.write("Содержит слово error\n")
                for _ in range(5):
                    line = ''.join(random.choices(string.ascii_letters + ' ', k=30))
                    f.write(line + "\n")
        print(f"Создано {count} файлов. Ошибка в файле log_file_{error_index}.txt")

class SearchEngine:
    def __init__(self, keyword):
        self.keyword = keyword

    def search_in_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            if self.keyword in f.read():
                return filename
        return None

class Zowoo(SearchEngine):
    def execute_search(self, files):
        results = []
        for file in files:
            if self.search_in_file(file):
                results.append(file)
        print(f"Найдено: {results}")

class ThreadedSearch(SearchEngine):
    def execute_search(self, files, num_threads=8):
        results = []
        lock = threading.Lock()

        def worker(files_to_check):
            for file in files_to_check:
                if self.search_in_file(file):
                    with lock:
                        results.append(file)

        chunk_size = max(1, len(files) // num_threads)
        threads = []
        for i in range(num_threads):
            start_idx = i * chunk_size
            end_idx = len(files) if i == num_threads - 1 else (i + 1) * chunk_size
            t = threading.Thread(target=worker, args=(files[start_idx:end_idx],))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        print(f"Найдено: {results}")

def main():
    logs = Logs()
    logs.generate_files(10)
    keyword = "error"
    sequential_search = Zowoo(keyword)
    sequential_search.execute_search(logs.file_list)
    multi_threaded_search = ThreadedSearch(keyword)
    multi_threaded_search.execute_search(logs.file_list)

if __name__ == "__main__":
    main()
