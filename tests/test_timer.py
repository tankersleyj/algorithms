# MIT, jtankersley, 2019-05-18
import time
import unittest
from src import timer

@timer.print_time_dec
def wait(seconds):
  time.sleep(seconds)


class TestTimer(unittest.TestCase):

    def test_print_time_dec(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()