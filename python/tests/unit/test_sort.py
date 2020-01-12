# MIT (c) jtankersley 2019-05-19
import unittest
from src import sort
from src import timer

orderedList = [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]
unOrderedList = [10,20,31,4,6,5,15,2,12,25,3,30,32,1,7,8]


class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        actual = timer.run_timed_result(sort.bubble_sort, unOrderedList.copy())
        expected = orderedList
        self.assertEqual(actual, expected, 'bubble_sort')

    def test_merge_sort(self):
        actual = timer.run_timed_result(sort.merge_sort, unOrderedList.copy())
        expected = orderedList
        self.assertEqual(actual, expected, 'merge_sort')

    def test_python_sort(self):
        actual = timer.run_timed_result(sort.python_sort, unOrderedList.copy())
        expected = orderedList
        self.assertEqual(actual, expected, 'python_sort')
