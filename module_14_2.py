import sqlite3

# Подключаемся к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('not_telegram1.db')
cursor = conn.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# for i in range(10):
#     age = 10 * (i + 1)  # Возраст от 10 до 100, увеличивается на 10
#     cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
#         (f"User{i}", f"example{i}@gmail.com", age, 1000))

# Удаление пользователя с id=6


# cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчитываем общее количество записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Считаем сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вычисляем средний баланс всех пользователей
# average_balance = total_balance / total_records if total_records > 0 else 0
print(all_balances / total_users)


# # Выводим результат
# print(f'Общее количество записей: {total_records}')
# print(f'Сумма всех балансов: {total_balance}')
# print(f'Средний баланс всех пользователей: {average_balance:.2f}')

# Подсчёт кол-ва всех пользователей
# Подсчёт суммы всех балансов

conn.commit()
conn.close()