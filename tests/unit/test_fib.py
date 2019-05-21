# MIT (c) jtankersley 2019-05-19
import unittest
from src import fib
from src import timer


class TestFib(unittest.TestCase):

    def test_fib_for(self):
        actual = timer.run_timed_result(fib.fib_for, 10)
        expected = 55
        self.assertEqual(actual, expected, 'fib_for')

    def test_fib_rec(self):
        actual = timer.run_timed_result(fib.fib_rec, 10)
        expected = 55
        self.assertEqual(actual, expected, 'fib_rec')
