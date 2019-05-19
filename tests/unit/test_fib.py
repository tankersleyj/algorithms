# MIT (c) jtankersley 2019-05-19
import unittest
from src import fib


class TestFib(unittest.TestCase):

  def test_fib_for(self):
      print("test fib for")
      self.assertEqual(fib.fib_for(10), 55, 'fib_for')

  def test_fib_rec(self):
      print("test fib rec")
      self.assertEqual(fib.fib_rec(10), 55, 'fib_rec')
