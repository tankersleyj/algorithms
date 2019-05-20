# MIT (c) jtankersley 2019-05-19
import unittest


class TestUnit(unittest.TestCase):

    def test_unit(self):
        print("test unit")
        self.assertEqual('foo'.upper(), 'FOO')
