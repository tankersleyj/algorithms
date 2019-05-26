# MIT (c) jtankersley 2019-05-19
import unittest
from src import sort
from src import timer

unordered_list = [10,35,20,31,4,6,5,34,15,2,12,25,3,30,32,33,1,7,36,8]
ordered_list = [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32,33,34,35,36]


class TestSort(unittest.TestCase):

    def test_sort_bubble(self):
        actual = timer.run_timed_result(sort.sort_bubble, unordered_list.copy())
        expected = ordered_list
        self.assertEqual(actual, expected, 'sort_bubble')

    def test_sort_instant(self):
        actual = timer.run_timed_result(sort.sort_instant, unordered_list.copy())
        expected = ordered_list
        self.assertEqual(actual, expected, 'sort_instant')

    def test_sort_merge(self):
        actual = timer.run_timed_result(sort.sort_merge, unordered_list.copy())
        expected = ordered_list
        self.assertEqual(actual, expected, 'sort_merge')

    def test_sort_quick(self):
        actual = timer.run_timed_result(sort.sort_quick, unordered_list.copy())
        expected = ordered_list
        self.assertEqual(actual, expected, 'sort_quick')
