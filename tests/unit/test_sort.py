# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import timer


@timer.print_time_dec
def wait(seconds):
  time.sleep(seconds)


class TestTimer(unittest.TestCase):

  def test_sort(self):
      print("test sort")
      self.assertEqual('foo'.upper(), 'FOO')
