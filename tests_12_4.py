import logging
import unittest
from unittest import TestCase


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            r1= Runner("Вася", -5)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50, f"{r1.name} должен пройти 50, а прошел {r1.distance}")
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info= True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            r2 = Runner(15)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100, f"{r2.name} должен пройти 50, а прошел {r2.distance}")
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info= True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challange(self):
        r1 = Runner("Вася")
        r2 = Runner("Коля")
        for i in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)





# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())
