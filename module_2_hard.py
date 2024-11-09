n = int(input("Введите число от 3 до 20: "))
result = ""

for i in range(1, n + 1):
    for j in range(i, n + 1):
        s = i + j
        if n % s == 0:
            result += str(i) + str(j)

print("Пароль:", result)