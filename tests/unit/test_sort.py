# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import timer


class TestSort(unittest.TestCase):

    def test_sort(self):
        self.assertEqual('foo'.upper(), 'FOO')
