# MIT (c) jtankersley 2019-05-19
import unittest
from src import fib
from src import timer


class TestFib(unittest.TestCase):

    def test_fib_recursive(self):
        actual = timer.runTimedResult(fib.fib_recursive, 1)
        self.assertEqual(actual, 1, 'fib_recursive(1)')
        actual = timer.runTimedResult(fib.fib_recursive, 2)
        self.assertEqual(actual, 1, 'fib_recursive(2)')
        actual = timer.runTimedResult(fib.fib_recursive, 3)
        self.assertEqual(actual, 2, 'fib_recursive(3)')
        actual = timer.runTimedResult(fib.fib_recursive, 4)
        self.assertEqual(actual, 3, 'fib_recursive(4)')
        actual = timer.runTimedResult(fib.fib_recursive, 5)
        self.assertEqual(actual, 5, 'fib_recursive(5)')
        actual = timer.runTimedResult(fib.fib_recursive, 16)
        self.assertEqual(actual, 987, 'fib_recursive(16)')
        actual = timer.runTimedResult(fib.fib_recursive, 32)
        self.assertEqual(actual, 2178309, 'fib_recursive(32)')
        # actual = timer.runTimedResult(fib.fib_recursive, 64)
        # self.assertEqual(actual, 2178309, 'fib_recursive(64)')

    def test_fib_array(self):
        actual = timer.runTimedResult(fib.fib_array, 1)
        self.assertEqual(actual, 1, 'fib_array(1)')
        actual = timer.runTimedResult(fib.fib_array, 2)
        self.assertEqual(actual, 1, 'fib_array(2)')
        actual = timer.runTimedResult(fib.fib_array, 3)
        self.assertEqual(actual, 2, 'fib_array(3)')
        actual = timer.runTimedResult(fib.fib_array, 4)
        self.assertEqual(actual, 3, 'fib_array(4)')
        actual = timer.runTimedResult(fib.fib_array, 5)
        self.assertEqual(actual, 5, 'fib_array(5)')
        actual = timer.runTimedResult(fib.fib_array, 16)
        self.assertEqual(actual, 987, 'fib_array(16)')
        actual = timer.runTimedResult(fib.fib_array, 32)
        self.assertEqual(actual, 2178309, 'fib_array(32)')

    def test_fib_vars(self):
        actual = timer.runTimedResult(fib.fib_vars, 1)
        self.assertEqual(actual, 1, 'fib_vars(1)')
        actual = timer.runTimedResult(fib.fib_vars, 2)
        self.assertEqual(actual, 1, 'fib_vars(2)')
        actual = timer.runTimedResult(fib.fib_vars, 3)
        self.assertEqual(actual, 2, 'fib_vars(3)')
        actual = timer.runTimedResult(fib.fib_vars, 4)
        self.assertEqual(actual, 3, 'fib_vars(4)')
        actual = timer.runTimedResult(fib.fib_vars, 5)
        self.assertEqual(actual, 5, 'fib_vars(5)')
        actual = timer.runTimedResult(fib.fib_vars, 16)
        self.assertEqual(actual, 987, 'fib_vars(16)')
        actual = timer.runTimedResult(fib.fib_vars, 32)
        self.assertEqual(actual, 2178309, 'fib_vars(32)')

    def test_fib_var2(self):
        actual = timer.runTimedResult(fib.fib_var2, 1)
        self.assertEqual(actual, 1, 'fib_var2(1)')
        actual = timer.runTimedResult(fib.fib_var2, 2)
        self.assertEqual(actual, 1, 'fib_var2(2)')
        actual = timer.runTimedResult(fib.fib_var2, 3)
        self.assertEqual(actual, 2, 'fib_var2(3)')
        actual = timer.runTimedResult(fib.fib_var2, 4)
        self.assertEqual(actual, 3, 'fib_var2(4)')
        actual = timer.runTimedResult(fib.fib_var2, 5)
        self.assertEqual(actual, 5, 'fib_var2(5)')
        actual = timer.runTimedResult(fib.fib_var2, 16)
        self.assertEqual(actual, 987, 'fib_var2(16)')
        actual = timer.runTimedResult(fib.fib_var2, 32)
        self.assertEqual(actual, 2178309, 'fib_var2(32)')
