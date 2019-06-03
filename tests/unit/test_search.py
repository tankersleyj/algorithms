# MIT (c) jtankersley 2019-05-19
import unittest
from src import search
from src import timer

orderedList = [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]


class TestSearch(unittest.TestCase):

    def test_binarySearch(self):
        actual = timer.runTimedResult(search.binarySearch, orderedList, 15)
        expected = 10
        self.assertEqual(actual, expected, 'binarySearch')
