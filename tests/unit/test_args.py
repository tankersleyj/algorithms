# MIT (c) jtankersley 2019-05-19
import unittest
from src import args


class TestArg(unittest.TestCase):

    def test_get_args(self):
        self.assertGreater(len(args.get_args()), 0, "get_args")

    def test_get_arg(self):
        self.assertEqual(args.get_arg(1), 'discover', "get_arg(1)")
