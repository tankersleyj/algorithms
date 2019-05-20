# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import timer


@timer.print_time_dec
def wait_print_time(seconds):
    time.sleep(seconds/100)
    return seconds


@timer.get_time_dec
def wait_log_time(seconds):
    time.sleep(seconds/100)
    return seconds


def wait_time(seconds):
    time.sleep(seconds/100)
    return seconds


class TestTimer(unittest.TestCase):

    def test_print_time_dec(self):
        print("test print_time_dec")
        actual = wait_print_time(1)
        expected = 1
        self.assertEqual(actual, expected, 'print_time_dec')

    def test_get_time_dec(self):
        print("test get_time_dec")
        actual, time_dict = wait_log_time(1)
        timer.print_time("get_time_dec", time_dict)
        expected = 1
        self.assertEqual(actual, expected, 'get_time_dec')

    def test_print_time(self):
        print("test print_time")
        begin = time.time()
        actual = wait_time(1)
        timer.print_time("print_time", {"begin": begin, "end": time.time()})
        expected = 1
        self.assertEqual(actual, expected, 'print_time')

    def test_run_timed(self):
        print("test run_timed")
        actual = timer.run_timed(wait_time, 1)
        expected = 1
        self.assertEqual(actual, expected, 'get_time_dec')
