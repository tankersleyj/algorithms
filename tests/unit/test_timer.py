# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import timer


@timer.print_time_dec
def wait_print_time(seconds):
  time.sleep(seconds/100)
  return seconds


@timer.log_time_dec
def wait_log_time(seconds):
  time.sleep(seconds/100)
  return seconds


class TestTimer(unittest.TestCase):

  def test_print_time_dec(self):
      print("test print_time_dec")
      self.assertEqual(wait_print_time(1), 1, 'print_time_dec')

  def test_log_time_dec(self):
      print("test log_time_dec")
      result, time_dict = wait_log_time(1)
      print(f"result={result}, time_dict={time_dict}")
      self.assertEqual(result, 1, 'log_time_dec')
