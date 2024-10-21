def is_prime(func):
    def wrapper(*args):
        result = func(*args)

        if result < 2:
            print("Составное")
            return result

        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result

        print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)  # Вывод: Составное 11

# В этом коде:
#
#
#
# Функция sum_three складывает три числа.
#
# Декоратор is_prime проверяет результат функции sum_three и выводит, является ли он простым или составным.
#
# Пример использования показывает, как вызвать функцию и вывести результат.