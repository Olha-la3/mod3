
import unittest
import tests_12_2
import tests_12_1
from tests_12_2 import TournamentTest
from tests_12_1 import RunnerTest



trackST = unittest.TestSuite()

# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.

trackST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
trackST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))


# if __name__ == "__main__":
runner = unittest.TextTestRunner(verbosity=2)
runner.run(trackST)