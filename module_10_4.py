
# class Table:
#
# class Guest:
#
# class Cafe:
#
# # Создание столов
# tables = [Table(number) for number in range(1, 6)]
# # Имена гостей
# guests_names = [
# 'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
# 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
# ]
# # Создание гостей
# guests = [Guest(name) for name in guests_names]
# # Заполнение кафе столами
# cafe = Cafe(*tables)
# # Приём гостей
# cafe.guest_arrival(*guests)
# # Обслуживание гостей
# cafe.discuss_guests()
# Для решения этой задачи мы создадим три класса: Table, Guest и Cafe.
#
#
# Класс Table будет представлять столы в кафе. Он будет инициализироваться с номером стола и возможно с гостем.
# Если гость не указан, то по умолчанию будет None.

#
# class Table:
#     def __init__(self, number):
#         self.number = number
#         self.guest = None
#
# # Класс Guest будет наследоваться от Thread. При создании объекта этого класса передается имя гостя,
# # а метод run будет ждать случайное время от 3 до 10 секунд.
#
#
# import random
# from threading import Thread
#
# class Guest(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         time.sleep(random.randint(3, 10))
#
# # Класс Cafe объединит все таблицы и будет управлять очередью гостей. Он будет содержать методы для приема гостей
# # и обслуживания, использующего статусы столиков.
#
#
# from queue import Queue
#
# class Cafe:
#     def __init__(self, *tables):
#         self.queue = Queue()
#         self.tables = tables
#
#     def guest_arrival(self, guest_name):
#         guest = Guest(guest_name)
#         self.queue.put(guest)
#         guest.start()
#
#     def discuss_guests(self):
#         for table in self.tables:
#             if table.guest is None and not self.queue.empty():
#                 table.guest = self.queue.get()

# Для реализации задачи создадим три класса: Table, Guest и Cafe.
#
#
# Класс Table: Хранит объект Guest и управляет состоянием стола.
import threading
import time
import random
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

# Класс Guest: Представляет гостя, который является потоком. В конструкторе определим задержку (от 3 до 10 секунд).


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.eating_time = random.randint(3, 10)

    def run(self):
        time.sleep(self.eating_time)

# Класс Cafe: Управляет столами и очередью. Реализует методы guest_arrival и discuss_guests.

class Cafe:
    def __init__(self):
        self.tables = [Table(i) for i in range(table_count)]
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                   self.queue.put(guest)
                   print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
