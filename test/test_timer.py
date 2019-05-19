# MIT (c) jtankersley 2019-05-18
import time
import unittest
from src import timer

print("1")
@timer.print_time_dec
def wait(seconds):
  time.sleep(seconds)


class TestTimer(unittest.TestCase):

  def test_print_time_dec(self):
      print("3")
      self.assertEqual('foo'.upper(), 'FOO')

print(f"name={__name__}")
if __name__ == '__main__':
  print("2")
  unittest.main()
