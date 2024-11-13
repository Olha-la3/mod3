import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament
import random


def frozen_decorator(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            print('Тесты в этом кейсе заморожены')
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)

    return wrapper
class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.Andrei = Runner('Андрей', 9)
        self.Nik = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(cls.all_results[i])

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def testTournament1(self):
        tournament = Tournament(90, self.usain, self.Nik)
        dict1 = tournament.start()
        for i in dict1:
            dict1[i] = dict1[i].name
        self.all_results[1] = dict1
        self.assertTrue(dict1[2], 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def testTournament2(self):
        tournament = Tournament(90, self.Andrei, self.Nik)
        dict1 = tournament.start()
        for i in dict1:
            dict1[i] = dict1[i].name
        self.all_results[2] = dict1
        self.assertTrue(dict1[2], 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def testTournament3(self):
        tournament = Tournament(90, self.usain, self.Andrei, self.Nik)
        dict1 = tournament.start()
        for i in dict1:
            dict1[i] = dict1[i].name
        self.all_results[3] = dict1
        self.assertTrue(dict1[2], 'Ник')


if __name__ == '__main__':
    unittest.main()