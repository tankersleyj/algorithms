# MIT (c) jtankersley 2019-05-19
import unittest
from src import fib
from src import timer


class TestFib(unittest.TestCase):

    def test_getFib_recursive(self):
        actual = timer.runTimedResult(fib.getFib_recursive, 1)
        self.assertEqual(actual, 1, 'getFib_recursive(1)')
        actual = timer.runTimedResult(fib.getFib_recursive, 2)
        self.assertEqual(actual, 1, 'getFib_recursive(2)')
        actual = timer.runTimedResult(fib.getFib_recursive, 3)
        self.assertEqual(actual, 2, 'getFib_recursive(3)')
        actual = timer.runTimedResult(fib.getFib_recursive, 4)
        self.assertEqual(actual, 3, 'getFib_recursive(4)')
        actual = timer.runTimedResult(fib.getFib_recursive, 5)
        self.assertEqual(actual, 5, 'getFib_recursive(5)')
        actual = timer.runTimedResult(fib.getFib_recursive, 16)
        self.assertEqual(actual, 987, 'getFib_recursive(16)')
        actual = timer.runTimedResult(fib.getFib_recursive, 24)
        self.assertEqual(actual, 46368, 'getFib_recursive(24)')

    def test_getFib_array(self):
        actual = timer.runTimedResult(fib.getFib_array, 1)
        self.assertEqual(actual, 1, 'getFib_array(1)')
        actual = timer.runTimedResult(fib.getFib_array, 2)
        self.assertEqual(actual, 1, 'getFib_array(2)')
        actual = timer.runTimedResult(fib.getFib_array, 3)
        self.assertEqual(actual, 2, 'getFib_array(3)')
        actual = timer.runTimedResult(fib.getFib_array, 4)
        self.assertEqual(actual, 3, 'getFib_array(4)')
        actual = timer.runTimedResult(fib.getFib_array, 5)
        self.assertEqual(actual, 5, 'getFib_array(5)')
        actual = timer.runTimedResult(fib.getFib_array, 16)
        self.assertEqual(actual, 987, 'getFib_array(16)')
        actual = timer.runTimedResult(fib.getFib_array, 24)
        self.assertEqual(actual, 46368, 'getFib_array(24)')

    def test_getFib_vars(self):
        actual = timer.runTimedResult(fib.getFib_vars, 1)
        self.assertEqual(actual, 1, 'getFib_vars(1)')
        actual = timer.runTimedResult(fib.getFib_vars, 2)
        self.assertEqual(actual, 1, 'getFib_vars(2)')
        actual = timer.runTimedResult(fib.getFib_vars, 3)
        self.assertEqual(actual, 2, 'getFib_vars(3)')
        actual = timer.runTimedResult(fib.getFib_vars, 4)
        self.assertEqual(actual, 3, 'getFib_vars(4)')
        actual = timer.runTimedResult(fib.getFib_vars, 5)
        self.assertEqual(actual, 5, 'getFib_vars(5)')
        actual = timer.runTimedResult(fib.getFib_vars, 16)
        self.assertEqual(actual, 987, 'getFib_vars(16)')
        actual = timer.runTimedResult(fib.getFib_vars, 24)
        self.assertEqual(actual, 46368, 'getFib_vars(24)')

    def test_getFib_var2(self):
        actual = timer.runTimedResult(fib.getFib_var2, 1)
        self.assertEqual(actual, 1, 'getFib_var2(1)')
        actual = timer.runTimedResult(fib.getFib_var2, 2)
        self.assertEqual(actual, 1, 'getFib_var2(2)')
        actual = timer.runTimedResult(fib.getFib_var2, 3)
        self.assertEqual(actual, 2, 'getFib_var2(3)')
        actual = timer.runTimedResult(fib.getFib_var2, 4)
        self.assertEqual(actual, 3, 'getFib_var2(4)')
        actual = timer.runTimedResult(fib.getFib_var2, 5)
        self.assertEqual(actual, 5, 'getFib_var2(5)')
        actual = timer.runTimedResult(fib.getFib_var2, 16)
        self.assertEqual(actual, 987, 'getFib_var2(16)')
        actual = timer.runTimedResult(fib.getFib_var2, 24)
        self.assertEqual(actual, 46368, 'getFib_var2(24)')
