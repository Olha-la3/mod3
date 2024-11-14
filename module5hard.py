
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
        return hashlib.sha256(password.encode()).hexdigest() == self.hash_password(password)

    # def str(self):
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

    def log_in(self, nickname, password):
        global current_user

        for user in self.users:
            if user.nickname == nickname and user.check_password(password) == True:
                current_user = user
                return print('Successfully logged in as', nickname)

        return print('Invalid nickname or password')

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.log_in(nickname, password)


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
        if video == None:
            return None
        if video.adult_mode == True and current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for second in range(video.duration):
                print(f"Смотрим {title}: {second} секунд")
                sleep(1)
            print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
