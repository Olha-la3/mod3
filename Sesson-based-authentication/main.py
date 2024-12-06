from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'dfaagbkm123dsgj234c'  # Замените на свой секретный ключ

# Простейшая база данных пользователей (как пример)
users = {
    "user1": "password1",
    "user2": "password2"
}

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
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'register' in request.form:  # Регистрация
            username = request.form.get('username')
            password = request.form.get('password')

            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()

            # Проверка на существование пользователя
            cursor.execute('''
                SELECT COUNT(*) FROM users WHERE  username = ?
                ''', (username,))

            count = cursor.fetchone()[0]

            if count > 0:
                flash('Пользователь уже существует!', 'danger')
                conn.close()
            else:
                # добавление пользователя
                cursor.execute('''
                    INSERT INTO users (username, password) VALUES
                    (?, ?)
                    ''', (username, password))

                conn.commit()
                conn.close()
                flash('Пользователь успешно зарегистрирован! Вы можете войти.', 'success')

        elif 'login' in request.form:  # Вход
            username = request.form.get('username_login')
            password = request.form.get('password_login')

            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()

            # Проверка учетных данных
            cursor.execute('''
                    SELECT COUNT(*) FROM users WHERE  username = ? AND password = ?
                    ''', (username, password,))

            count = cursor.fetchone()[0]

            if count > 0:
                conn.close()
                session['username'] = username
                flash('Вы успешно вошли!', 'success')
                return redirect(url_for('protected'))

            flash('Неверные учетные данные!', 'danger')
            conn.close()

    return render_template('index.html')


# Защищенная страница
@app.route('/protected')
def protected():
    if 'username' not in session:
        flash('Пожалуйста, войдите, чтобы увидеть эту страницу.', 'warning')
        return redirect(url_for('home'))

    return f'Привет, {session["username"]}! <a href="/logout">Выйти</a>'


# Выход
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Вы вышли из системы.', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)