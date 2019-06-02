# MIT (c) jtankersley 2019-05-19
import unittest
from src import args


class TestArg(unittest.TestCase):

    def test_getArgs(self):
        self.assertGreater(len(args.getArgs()), 0, "getArgs")

    def test_getArg(self):
        self.assertEqual(args.getArg(1), 'discover', "getArg(1)")
