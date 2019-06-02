# MIT (c) jtankersley 2019-05-19
import unittest
from src import prime
from src import timer


class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        actual = timer.runTimedResult(prime.is_prime, 11)
        expected = True
        self.assertEqual(actual, expected, 'is_prime')
