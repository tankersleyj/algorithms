# MIT (c) jtankersley 2019-05-19
import unittest
from src import list
from src import timer


class TestSort(unittest.TestCase):

    def test_list(self):
        dll = list.DoubleList()
        dll.addHead(1)
        dll.addHead(2)
        dll.addHead(3)
        # print(f"{str(dll)}")
        # print(f"{dll.toString()}")
        # actual = timer.runTimedResult(sort.bubbleSort, unordered_list.copy())
        # expected = ordered_list
        # self.assertEqual(actual, expected, 'bubbleSort')
