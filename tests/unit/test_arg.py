# MIT (c) jtankersley 2019-05-19
import unittest
from src import arg


class TestArg(unittest.TestCase):

    def test_get_args(self):
        print("test get_args")
        self.assertGreater(len(arg.get_args()), 0, "get_args")

    def test_get_arg(self):
        print("test get_arg")
        self.assertEqual(arg.get_arg(1), 'discover', "get_arg(1)")
