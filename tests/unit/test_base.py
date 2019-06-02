# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import base
from src import timer


class TestBase(unittest.TestCase):

    def test_convertToBase10(self):
        actual = timer.runTimedResult(base.convertToBase10, "11011", 2)
        expected = 27
        self.assertEqual(actual, expected, "convertToBase10")
        actual = timer.runTimedResult(base.convertToBase10, "FF", 16)
        expected = 255
        self.assertEqual(actual, expected, "convertToBase10")

    def test_convertFromBase10(self):
        actual = timer.runTimedResult(base.convertFromBase10, 27, 2)
        expected = "011011"
        self.assertEqual(actual, expected, "convertFromBase10")
        actual = timer.runTimedResult(base.convertFromBase10, 255, 16)
        expected = "0FF"
        self.assertEqual(actual, expected, "convertToBase10")
