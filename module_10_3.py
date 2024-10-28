# import threading
# import random
# import time
#
# class Bank:
#     # def __init__(self):
#     #     self.balance = 0  # Начальный баланс
#     #     self.lock = threading.Lock()
#     #
#     # def deposit(self):
#     #     while i < 100:
#     #         if self.balance >= 500 and self.lock.locked() == True:
#     #             self.lock.release()
#     #             cashe = random.randint(50, 500)
#     #             self.balance = self.balance + cashe
#     #             time.sleep(0.01)
#     #             print(f"Пополнение: {cashe}, Баланс: {self.balance} ")
#     #             i = i + 1
#     #
#     #         time.sleep(0.001)  # Имитация задержки
#     def __init__(self, balance, lock=threading.Lock()):
#         self.balance = balance  # Начальный баланс
#         self.lock = lock
#
#     def deposit(self):
#         for _ in range(100):
#             amount = random.randint(50, 500)  # Случайная сумма пополнения
#             with self.lock:  # Блокировка потока
#                 self.balance += amount
#                 if self.balance >= 500 and self.lock.locked():
#                     self.lock.release()  # Освобождение замка
#                 print(f"Пополнение: {amount}. Баланс: {self.balance}.")
#             time.sleep(0.001)  # Имитация задержки
#     def take(self):
#         for i in range(100):
#             request = random.randint(50, 500)
#             print(f"Запрос на {request}")
#             with self.lock:
#                 if request <= self.balance:
#                     self.balance -= request
#                     print(f"Снятие: {request}. Баланс: {self.balance}")
#                 else:
#                     print("Запрос отклонён, недостаточно средств")
#                     self.lock.acquire()  # Блокировка потока
#                     time.sleep(1)  # Ожидание
#                     self.lock.release()  # Разблокировка
#
#
# bk = Bank()
#
# # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
# th1 = threading.Thread(target=Bank.deposit, args=(bk,))
# th2 = threading.Thread(target=Bank.take, args=(bk,))
#
# th1.start()
# th2.start()
# th1.join()
# th2.join()
#
# print(f'Итоговый баланс: {bk.balance}')
import random
import threading
import time

class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        i = 0
        while i < 100:
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            cashe = random.randint(50, 500)
            self.balance = self.balance + cashe
            time.sleep(0.01)
            print(f"Пополнение: {cashe}, Баланс: {self.balance} ")
            i = i+1

    def take(self):
        i = 0
        while i < 100:
            cashe = random.randint(50, 500)
            print(f"Запрос на: {cashe}")
            if self.balance < cashe:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance = self.balance - cashe
                print(f"Снятие: {cashe}, Баланс: {self.balance} ")
            i = i + 1


bk = Bank(balance=0)

th1 = threading.Thread(target = Bank.deposit, args = (bk,))
th2 = threading.Thread(target = Bank.take, args = (bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
print(f'Итоговый баланс: {bk.balance}')