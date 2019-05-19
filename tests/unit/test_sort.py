# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import timer

print("sort.1")
@timer.print_time_dec
def wait(seconds):
  time.sleep(seconds)


class TestTimer(unittest.TestCase):

  def test_print_time_dec(self):
      print("sort.3")
      self.assertEqual('foo'.upper(), 'FOO')

print(f"sort.name={__name__}")
if __name__ == '__main__':
  print("sort.2")
  unittest.main()
