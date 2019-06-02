# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import fact
from src import timer


class TestFact(unittest.TestCase):

    def test_isFactorial(self):
        actual = timer.runTimedResult(fact.isFactorial, 87178291200)
        expected = True
        self.assertEqual(actual, expected, "isFactorial")

    def test_getFactors(self):
        actual = timer.runTimedResult(fact.getFactors, 121)
        expected = [1, 11]
        self.assertEqual(actual, expected, "getFactors")


    def test_getFactorial(self):
        actual = timer.runTimedResult(fact.getFactorial, 10)
        expected = 362880
        self.assertEqual(actual, expected, "getFactorial")
