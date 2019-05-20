# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import fact
from src import timer


class TestFact(unittest.TestCase):

    def test_is_factorial(self):
        print("test is_factorial")
        actual = timer.run_timed(fact.is_factorial, 87178291200)
        expected = True
        self.assertEqual(actual, expected, "is_factorial")

    def test_get_factors(self):
        print("test get_factors")
        actual = timer.run_timed(fact.get_factors, 121)
        expected = [1, 11]
        self.assertEqual(actual, expected, "get_factors")


    def test_get_factorial(self):
        print("test get_factorial")
        actual = timer.run_timed(fact.get_factorial, 10)
        expected = 362880
        self.assertEqual(actual, expected, "get_factorial")
