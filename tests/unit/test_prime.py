# MIT (c) jtankersley 2019-05-19
import unittest
from src import prime


class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        print("test is_prime")
        self.assertEqual(prime.is_prime(11), True, 'is_prime')
