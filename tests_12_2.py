from unittest import TestCase
from runner_and_tournament import Runner, Tournament

class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
    def setUp(self):
        self.first = Runner("Усэйн", 10)
        self.second = Runner("Андрей", 9)
        self.third = Runner('Ник', 3)

    def test_first_turnement(self):
        tournament = Tournament(90, self.first, self.third)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == "Ник")
    def test_seconde_turnament(self):
        tournament = Tournament(90, self.second, self.third)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == "Ник")

    def test_third_turnament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[3] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for i, j in enumerate(cls.all_results):
            print(f'{i+1}: {j}')


