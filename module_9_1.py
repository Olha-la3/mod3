def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:

        results.update({func.__name__: func(int_list)})
    return results


def min(int_list):  # - список, минимальное значение из него.
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] < int_list[i + 1]:
            result = int_list[i]
    return result

def max(int_list):  # - список, максимальное значение из него.
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] > int_list[i + 1]:
            result = int_list[i]
    return result

def len_(int_list):  # - список, кол-во элементов в нём.
    result = len(int_list)
    return result

def sum(int_list):  # - список, сумма его элементов.
    result = 0
    for i in int_list:
        result += i
    return result

def sorted_(int_list):  # - список, новый отсортированный список.
    result = sorted(int_list)
    return result

def midle(int_list):  # - список, среднее значение его элементов.
    result = 0
    for i in int_list:
        result += i
    result = result / len_(int_list)
    return result



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))