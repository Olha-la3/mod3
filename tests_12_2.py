import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament

class TournamentTest(unittest.TestCase):


    def setUp(cls):
        cls.usain = Runner('Усэйн', 10)
        cls.Andrei = Runner('Андрей', 9)
        cls.Nik = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(cls.all_results[i])

    def testTournament1(cls):
        tournament = Tournament(90, cls.usain, cls.Nik)
        dict1 = tournament.start()
        for i in dict1:
            dict1[i] = dict1[i].name
        cls.all_results[1] = dict1
        cls.assertTrue(dict1[2], 'Ник')

    def testTournament2(cls):
        tournament = Tournament(90, cls.Andrei, cls.Nik)
        dict1 = tournament.start()
        for i in dict1:
            dict1[i] = dict1[i].name
        cls.all_results[2] = dict1
        cls.assertTrue(dict1[2], 'Ник')

    def testTournament3(cls):
        tournament = Tournament(90, cls.usain, cls.Andrei, cls.Nik)
        dict1 = tournament.start()
        for i in dict1:
            dict1[i] = dict1[i].name
        cls.all_results[3] = dict1
        cls.assertTrue(dict1[2], 'Ник')


if __name__ == '__main__':
    unittest.main()
