from flask import Flask, redirect, url_for, session, request
from requests_oauthlib import OAuth2Session
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Настройки OAuth
CLIENT_ID = '552379720947-t6jkdbu5r2fgn8t06qmgdusu8iqhiv7c.apps.googleusercontent.com'
CLIENT_SECRET = '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'
AUTHORIZATION_BASE_URL = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URL = 'https://oauth2.googleapis.com/token'
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = ['https://www.googleapis.com/auth/userinfo.profile']


@app.route('/')
def home():
    return '<h1>Главная страница</h1><a href="/login">Войти с Google</a>'


@app.route('/login')
def login():
    google = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)
    authorization_url, state = google.authorization_url(AUTHORIZATION_BASE_URL, access_type='offline', prompt='consent')

    # Сохраняем state в сессии
    session['oauth_state'] = state
    return redirect(authorization_url)


@app.route('/callback')
def callback():
    google = OAuth2Session(CLIENT_ID, state=session['oauth_state'], redirect_uri=REDIRECT_URI)
    token = google.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=request.url)

    # Сохраняем токен в сессии
    session['oauth_token'] = token
    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    # Запрос информации о пользователе
    google = OAuth2Session(CLIENT_ID, token=session['oauth_token'])
    user_info = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    return f'<h1>Профиль</h1><pre>{user_info}</pre>'


if __name__ == '__main__':
    app.run(debug=True)