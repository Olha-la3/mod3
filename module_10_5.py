
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # если строка пустая
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Список файлов
    start_time = time.time()

    # # Линейное чтение
    # for file in files:
    #     read_info(file)
    # linear_time = time.time() - start_time
    # print(f"Линейное выполнение: {linear_time} секунд.")

    # Многопроцессное чтение
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_time = time.time() - start_time
    print(f"Многопроцессное выполнение: {parallel_time} секунд.")
