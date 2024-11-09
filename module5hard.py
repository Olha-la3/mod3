#
# Класс User:
#
# Атрибуты: nickname, password (хэшированное), age.
# Методы: __eq__ для сравнения пользователей, __str__ для представления.
#
# Класс Video:
#
# Атрибуты: title, duration, time_now, adult_mode.
# Методы: __str__ для представления видео.
#
# Класс UrTube:
#
# Атрибуты: users (список объектов User), videos (список объектов Video), current_user.
# Методы:
# register: добавляет пользователя, если его не существует.
# log_in: авторизация пользователя по никнейму и паролю (сравнение по хэшу).
# log_out: сброс текущего пользователя.
# add: добавляет видео в список, если оно с таким же названием не существует.
# get_videos: возвращает список видео по ключевым словам (негорологичный поиск).
# watch_video: воспроизводит видео с учетом возраста и авторизации пользователя.
from time import sleep
import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


    def hash_password(self, password):
        # Создание хэш-значения пароля
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        # Проверка введенного пароля с хранившимся
        return self.password == self.hash_password(password)

    # def __str__(self):
    #     return (f"User(nickname={self.nickname}, age={self.age})

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode



class UrTube:
    def __init__(self, users = [], videos = []):
        self.users = users
        self.videos =  videos
        self.current_user = None

    # def log_in(self, nickname, password): # принимает на вход никнейм и пафорд
    #     for user in self.users:
    #         if user.nickname == nickname and user.password == password: #пытается найти пользователя с таким лог и пар
    #             self.current_user = user

    def log_in(self, nickname, password):
        global current_user

        for user in users:
            if user['nickname'] == nickname and user['password'] == hash_password(password):
                current_user = user
                print('Successfully logged in as', nickname)
        return print('Invalid nickname or password')

    def register(self, nickname, password, age):
        if nickname in users:
            print(f"Пользователь {nickname} уже существует")
        else:
            users[nickname] = {'password': password, 'age': age}
            login(nickname, password)
            # users.append({'nickname': nickname, 'password': password, 'age': age})
            # current_user = {'nickname': nickname, 'age': age}

    def log_out():
        global current_user
        current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, keyword):
        return [v.title for v in self.videos if keyword.lower() in v.title.lower()]

    def watch_video(self, title):
        if not self.log_in:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = next((v for v in self.videos if v.title == title), None)
        if video and self.current_user >= 18:
            for second in range(video.length):
                print(f"Смотрим {title}: {second} секунд")
                sleep(1)
            print("Конец видео")
        else:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')