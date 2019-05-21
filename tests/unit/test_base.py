# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import base
from src import timer


class TestBase(unittest.TestCase):

    def test_convert_to_base_10(self):
        actual = timer.run_timed_result(base.convert_to_base_10, "11011", 2)
        expected = 27
        self.assertEqual(actual, expected, "convert_to_base_10")
