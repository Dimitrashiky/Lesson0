from unittest import TestCase
from runner_and_tournament import Runner, Tournament

class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.first = Runner("Усэйн", 10)
        self.second = Runner("Андрей", 9)
        self.third = Runner('Ник', 3)

    def test_first_turnement(self):
        tournament = Tournament(90, self.first, self.third)
        self.all_results[1] = tournament.start()
        self.assertTrue(self.all_results[2][1] == "Ник")
    def test_seconde_turnament(self):
        tournament = Tournament(90, self.second, self.third)
        self.all_results[2] = tournament.start()
        self.assertTrue(self.all_results[2][2] == "Ник")

    def test_third_turnament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        self.all_results[2] = tournament.start()
        self.assertTrue(self.all_results[3][2] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f'{i+1}: {j}')


