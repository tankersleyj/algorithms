# MIT (c) jtankersley 2019-05-19
import unittest
from src import fact


class TestFact(unittest.TestCase):

  def test_is_factorial(self):
    print("test is_factorial")
    self.assertEqual(fact.is_factorial(87178291200), True, "is_factorial")

  def test_get_factors(self):
    print("test get_factors")
    self.assertEqual(fact.get_factors(121), [1, 11], "get_factors")

  def test_get_factorial(self):
    print("test get_factorial")
    self.assertEqual(fact.get_factorial(10), 362880, "get_factorial")
