# MIT (c) jtankersley 2019-05-19
import unittest
from src import fib
from src import timer


class TestFib(unittest.TestCase):

    def test_fib_rec(self):
        actual = timer.run_timed_result(fib.fib_rec, 16)
        expected = 987
        self.assertEqual(actual, expected, 'fib_rec')

    def test_fib_it(self):
        actual = timer.run_timed_result(fib.fib_it, 16)
        expected = 987
        self.assertEqual(actual, expected, 'fib_it')

    def test_fib_for(self):
        actual = timer.run_timed_result(fib.fib_for, 16)
        expected = 987
        self.assertEqual(actual, expected, 'fib_for')
