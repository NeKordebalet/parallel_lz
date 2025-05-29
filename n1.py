import random
import string
from multiprocessing import Process, Lock
def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def write_to_file(lock, filename, num_chars):
    random_str = random_string(num_chars)
    with lock: 
        with open(filename, 'a') as f:
            f.write(random_str + '\n')
        print(f"Записано: {random_str}")
def main():
    num_processes = 10
    num_chars = 10
    filename = 'output.txt'
    lock = Lock()  
    processes = []
    for _ in range(num_processes):
        p = Process(target=write_to_file, args=(lock, filename, num_chars))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
if __name__ == '__main__':
    main()