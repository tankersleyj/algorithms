# MIT (c) jtankersley 2019-05-19
import unittest
from src import fib
from src import timer


class TestFib(unittest.TestCase):

    def test_fib_for(self):
        print("test fib for")
        self.assertEqual(timer.run_timed(fib.fib_for, 10), 55, 'fib_for')

    def test_fib_rec(self):
        print("test fib rec")
        self.assertEqual(timer.run_timed(fib.fib_rec, 10), 55, 'fib_rec')
