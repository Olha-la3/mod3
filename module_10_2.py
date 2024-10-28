

from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name_, power):
        self.name_ = str(name_)    # имя рыцаря. (str)
        self.power = int(power)  # сила рыцаря. (int)
        super().__init__()

    def run(self):
        print(f'{self.name_}, на нас напали!')
        num_days = 0
        enemyes = 100
        while enemyes > 0: # >= self.power:
            sleep(1)    # задержка в 1 секунду
            num_days += 1   # количество дней сражения
            enemyes = enemyes - self.power
            if enemyes < 0:
                enemyes = 0
            print(f'{self.name_} сражается {num_days}-й день..., осталось {enemyes} воинов.')

        print(f'{self.name_} одержал победу спустя {num_days} дней(дня)!')

threads = []

knight1 = Knight('Lancelot', 6)
knight1.start()
knight2 = Knight('Arthur', 12)
knight2.start()

threads.append(knight1)
threads.append(knight2)

for thread in threads:
    thread.join()
print(f'\nВсе враги повержены, битвы закончены!')

