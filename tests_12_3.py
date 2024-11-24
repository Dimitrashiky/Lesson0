import unittest
from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def tes_walk(self):
        r1= Runner("Вася")
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50, f"{r1.name} должен пройти 50, а прошел {r1.distance}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r2 = Runner("Коля")
        for i in range(10):
              r2.run()
        self.assertEqual(r2.distance, 100, f"{r2.name} должен пройти 50, а прошел {r2.distance}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challange(self):
        r1 = Runner("Вася")
        r2 = Runner("Коля")
        for i  in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)

class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.first = Runner("Усэйн", 10)
        self.second = Runner("Андрей", 9)
        self.third = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first_turnement(self):
        tournament = Tournament(90, self.first, self.third)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_seconde_turnament(self):
        tournament = Tournament(90, self.second, self.third)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_turnament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[3] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, value in enumerate(cls.all_results):
            print(f'{key+1}: {value}')

