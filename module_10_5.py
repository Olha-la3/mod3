# import time
# from multiprocessing import Pool


# def read_info(name):
#     all_data = []
#     with open(name, 'r') as file:
#         while True:
#             line = file.readline()
#             if not line:
#                 break
#             all_data.append(line.strip())
#     return all_data

# def read_info(name):
#     all_data = []  # Шаг 2: создаем пустой список
#     with open(name, 'r') as file:  # Шаг 3: открываем файл
#         while True:
#             line = file.readline()  # Шаг 4: считываем строку
#             if line == '':  # Шаг 5: проверяем на пустую строку
#                 break
#             all_data.append(line.strip())  # добавляем в список, убирая пробелы
#     return all_data  # возврат результата
#
# # file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
# filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start_time = time.time()
# for filename in filenames:
#     read_info(filename)
# linear_time = time.time() - start_time
# print(f'Время линейного вызова: {linear_time:.4f} секунд')

# Многопроцессный вызов
# if __name__ == '__main__':
#     start_time = time.time()
#     with Pool(processes=4) as p:
#         result = p.map(read_info, filenames)
#         multiproc_time = time.time() - start_time
#
# print(f'Время многопроцессного вызова: {multiproc_time:.4f} секунд')

# start_time = time.time()
#    with Pool() as pool:
#        pool.map(read_info, file_names)
# end_time = time.time()
# print(f"Multiprocessing execution time: {end_time - start_time} seconds")
# start_time = time.time()
#
# with Pool() as pool:
#     pool.map(read_info, filenames)
#
# parallel_duration = time.time() - start_time
# print(f"Многопроцессное время выполнения: {parallel_duration} секунд")

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