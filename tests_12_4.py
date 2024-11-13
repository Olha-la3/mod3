import logging
import unittest
from rt_with_exceptions import Runner

# Настройка логирования
# logging.basicConfig(
#     level=logging.INFO,
#     filename='runner_tests.log',
#     filemode='w',
#     encoding='utf-8',
#     format='%(asctime)s - %(levelname)s - %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner(name='Masha', speed=-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner: %s")


    def test_run(self):
        try:
            runner = Runner(name=123, speed=10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner: %s")

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filename='runner_tests.log',
        filemode='w',
        encoding='utf-8',
        format='%(asctime)s - %(levelname)s - %(message)s')