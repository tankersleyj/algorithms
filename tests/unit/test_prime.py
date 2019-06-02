# MIT (c) jtankersley 2019-05-19
import unittest
from src import prime
from src import timer


class TestPrime(unittest.TestCase):

    def test_isPrime(self):
        actual = timer.runTimedResult(prime.isPrime, 11)
        expected = True
        self.assertEqual(actual, expected, 'isPrime')
