# MIT (c) jtankersley 2019-05-19
import unittest
from src import fib
from src import timer


class TestFib(unittest.TestCase):

    def test_fib_recursive(self):
        actual = timer.run_timed_result(fib.fib_recursive, 16)
        expected = 987
        self.assertEqual(actual, expected, 'fib_recursive')

    def test_fib_array(self):
        actual = timer.run_timed_result(fib.fib_array, 16)
        expected = 987
        self.assertEqual(actual, expected, 'fib_array')

    def test_fib_vars(self):
        actual = timer.run_timed_result(fib.fib_vars, 16)
        expected = 987
        self.assertEqual(actual, expected, 'fib_vars')
