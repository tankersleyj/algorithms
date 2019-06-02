# MIT (c) jtankersley 2019-05-19
import unittest
from src import sort
from src import timer

ordered_list = [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]
unordered_list = [10,20,31,4,6,5,15,2,12,25,3,30,32,1,7,8]


class TestSort(unittest.TestCase):

    def test_bubbleSort(self):
        actual = timer.runTimedResult(sort.bubbleSort, unordered_list.copy())
        expected = ordered_list
        self.assertEqual(actual, expected, 'bubbleSort')

    def test_mergeSort(self):
        actual = timer.runTimedResult(sort.mergeSort, unordered_list.copy())
        expected = ordered_list
        self.assertEqual(actual, expected, 'mergeSort')

    def test_pythonSort(self):
        actual = timer.runTimedResult(sort.pythonSort, unordered_list.copy())
        expected = ordered_list
        self.assertEqual(actual, expected, 'pythonSort')
