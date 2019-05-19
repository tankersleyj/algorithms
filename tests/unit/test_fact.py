# MIT (c) jtankersley 2019-05-19
import unittest
from src import fact

class TestFact(unittest.TestCase):

  def test_(self):
    print("test fact")
    self.assertEqual(fact.is_factorial(87178291200), True, "is_factorial")
    self.assertEqual(fact.get_factors(121), [1, 11], "get_factors")
    self.assertEqual(fact.get_factorial(10), 362880, "get_factorial")
