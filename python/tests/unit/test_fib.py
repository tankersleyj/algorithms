# MIT (c) jtankersley 2019-05-19
import unittest
from src import fib
from src import timer


class TestFib(unittest.TestCase):

    def test_get_fib_recursive(self):
        actual = timer.run_timed_result(fib.get_fib_recursive, 1)
        self.assertEqual(actual, 1, 'get_fib_recursive(1)')
        actual = timer.run_timed_result(fib.get_fib_recursive, 2)
        self.assertEqual(actual, 1, 'get_fib_recursive(2)')
        actual = timer.run_timed_result(fib.get_fib_recursive, 3)
        self.assertEqual(actual, 2, 'get_fib_recursive(3)')
        actual = timer.run_timed_result(fib.get_fib_recursive, 4)
        self.assertEqual(actual, 3, 'get_fib_recursive(4)')
        actual = timer.run_timed_result(fib.get_fib_recursive, 5)
        self.assertEqual(actual, 5, 'get_fib_recursive(5)')
        actual = timer.run_timed_result(fib.get_fib_recursive, 16)
        self.assertEqual(actual, 987, 'get_fib_recursive(16)')
        actual = timer.run_timed_result(fib.get_fib_recursive, 24)
        self.assertEqual(actual, 46368, 'get_fib_recursive(24)')

    def test_get_fib_array(self):
        actual = timer.run_timed_result(fib.get_fib_array, 1)
        self.assertEqual(actual, 1, 'get_fib_array(1)')
        actual = timer.run_timed_result(fib.get_fib_array, 2)
        self.assertEqual(actual, 1, 'get_fib_array(2)')
        actual = timer.run_timed_result(fib.get_fib_array, 3)
        self.assertEqual(actual, 2, 'get_fib_array(3)')
        actual = timer.run_timed_result(fib.get_fib_array, 4)
        self.assertEqual(actual, 3, 'get_fib_array(4)')
        actual = timer.run_timed_result(fib.get_fib_array, 5)
        self.assertEqual(actual, 5, 'get_fib_array(5)')
        actual = timer.run_timed_result(fib.get_fib_array, 16)
        self.assertEqual(actual, 987, 'get_fib_array(16)')
        actual = timer.run_timed_result(fib.get_fib_array, 24)
        self.assertEqual(actual, 46368, 'get_fib_array(24)')

    def test_get_fib_vars(self):
        actual = timer.run_timed_result(fib.get_fib_vars, 1)
        self.assertEqual(actual, 1, 'get_fib_vars(1)')
        actual = timer.run_timed_result(fib.get_fib_vars, 2)
        self.assertEqual(actual, 1, 'get_fib_vars(2)')
        actual = timer.run_timed_result(fib.get_fib_vars, 3)
        self.assertEqual(actual, 2, 'get_fib_vars(3)')
        actual = timer.run_timed_result(fib.get_fib_vars, 4)
        self.assertEqual(actual, 3, 'get_fib_vars(4)')
        actual = timer.run_timed_result(fib.get_fib_vars, 5)
        self.assertEqual(actual, 5, 'get_fib_vars(5)')
        actual = timer.run_timed_result(fib.get_fib_vars, 16)
        self.assertEqual(actual, 987, 'get_fib_vars(16)')
        actual = timer.run_timed_result(fib.get_fib_vars, 24)
        self.assertEqual(actual, 46368, 'get_fib_vars(24)')

    def test_get_fib_var2(self):
        actual = timer.run_timed_result(fib.get_fib_var2, 1)
        self.assertEqual(actual, 1, 'get_fib_var2(1)')
        actual = timer.run_timed_result(fib.get_fib_var2, 2)
        self.assertEqual(actual, 1, 'get_fib_var2(2)')
        actual = timer.run_timed_result(fib.get_fib_var2, 3)
        self.assertEqual(actual, 2, 'get_fib_var2(3)')
        actual = timer.run_timed_result(fib.get_fib_var2, 4)
        self.assertEqual(actual, 3, 'get_fib_var2(4)')
        actual = timer.run_timed_result(fib.get_fib_var2, 5)
        self.assertEqual(actual, 5, 'get_fib_var2(5)')
        actual = timer.run_timed_result(fib.get_fib_var2, 16)
        self.assertEqual(actual, 987, 'get_fib_var2(16)')
        actual = timer.run_timed_result(fib.get_fib_var2, 24)
        self.assertEqual(actual, 46368, 'get_fib_var2(24)')
