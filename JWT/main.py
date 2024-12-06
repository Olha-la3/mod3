from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3

app = Flask(__name__)
app.secret_key = 'ваш_секретный_ключ'  # Для использования flash-сообщений

# Настройки для JWT
app.config["JWT_SECRET_KEY"] = "ваш_секретный_ключ"  # Необходимо заменить на свой секретный ключ

# Инициализация JWT
jwt = JWTManager(app)


# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('users.db')  # Создаёт или подключается к базе данных
    cursor = conn.cursor()

    # Создание таблицы пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


# Вызов init_db() при запуске приложения
init_db()


# Главная страница
@app.route('/')
def home():
    return render_template('index.html')


# Регистрация нового пользователя
@app.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT COUNT(*) FROM users WHERE  username = ?
    ''', (username,))

    count = cursor.fetchone()[0]

    if count > 0:
        flash('Пользователь уже существует!', 'danger')
        conn.close()
        return redirect(url_for('home'))

    # добавление пользователя
    cursor.execute('''
    INSERT INTO users (username, password) VALUES
    (?, ?)
    ''', (username, password))

    conn.commit()
    conn.close()

    flash('Пользователь успешно зарегистрирован!', 'success')
    return redirect(url_for('home'))


# Вход пользователя и получение токена
@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM users WHERE  username = ? AND password = ?
        ''', (username, password,))

    count = cursor.fetchone()[0]

    if count > 0:
        access_token = create_access_token(identity=username)
        conn.close()
        return jsonify(access_token=access_token), 200

    flash('Неверные учетные данные!', 'danger')
    conn.close()
    return redirect(url_for('home'))


# Пример защищенного маршрута
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()  # Получаем текущего пользователя
    return jsonify(message=f'Привет, {current_user}!'), 200


if __name__ == '__main__':
    app.run(debug=True)