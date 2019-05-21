# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import timer


class TestSearch(unittest.TestCase):

    def test_search(self):
        self.assertEqual('foo'.upper(), 'FOO')
