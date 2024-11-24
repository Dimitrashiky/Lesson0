import unittest
import tests_12_3


runner_suite = unittest.TestSuite
runner_suite.run(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)