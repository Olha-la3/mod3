import sqlite3

# Подключаемся к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('not_telegram2.db')
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

#
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
for i in range(1, 11):
    age = 10 * (i)  # Возраст от 10 до 100, увеличивается на 10
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
        (f"User{i}", f"example{i}@gmail.com", age, 1000))

# Обновляем balance у каждой 2-ой записи, начиная с 1-ой
cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

# Удаляем каждую 3-ю запись, начиная с 1-ой
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

conn.commit()

# Выполняем выборку всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
rows = cursor.fetchall()

for row in rows:
    username, email, age, balance = row
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

# Закрываем соединение с базой данных

conn.close()