#  MIT (c) jtankersley 2019-05-19
import unittest


class TestIntegration(unittest.TestCase):

    def test_integration(self):
        self.assertEqual('foo'.upper(), 'FOO')
