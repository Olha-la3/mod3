# def calculate_structure_sum(data):
#     total_sum = 0
#     total_length = 0
#
#     for element in data:
#         if isinstance(element, (int, float)):  # Проверяем, является ли элемент числом
#             total_sum += element
#         elif isinstance(element, str):  # Проверяем, является ли элемент строкой
#             total_length += len(element)
#         elif isinstance(element, list) or isinstance(element, tuple):  # Если элемент - список или кортеж
#             inner_sum, inner_length = calculate_structure_sum(element)  # Рекурсивный вызов
#             total_sum += inner_sum
#             total_length += inner_length
#         elif isinstance(element, dict):  # Если элемент - словарь
#             for key, value in element.items():
#                 if isinstance(key, (int, float)):
#                     total_sum += key
#                 elif isinstance(key, str):
#                     total_length += len(key)
#                 total_sum += value if isinstance(value, (int, float)) else 0
#                 if isinstance(value, str):
#                     total_length += len(value)
#                 elif isinstance(value, (list, tuple)):
#                     inner_sum, inner_length = calculate_structure_sum(value)
#                     total_sum += inner_sum
#                     total_length += inner_length
#
#     return total_sum, total_length
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)

def calculate_structure_sum(data):
    total_sum = 0

    for item in data:
        if isinstance(item, (int, float)):  # Проверяем, является ли элемент числом
            total_sum += item
        elif isinstance(item, str):  # Проверяем, является ли элемент строкой
            total_sum += len(item)  # Добавляем длину строки
        elif isinstance(item, (list, tuple)):  # Проверяем, является ли элемент коллекцией
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для коллекций
        elif isinstance(item, dict):  # Проверяем, является ли элемент словарем
            for key, value in item.items():  # Проходим по ключам и значениям
                total_sum += calculate_structure_sum([key, value])  # Рекурсивный вызов для ключей и значений

    return total_sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99