# MIT (c) jtankersley 2019-05-19
import time
import unittest
from src import timer


# --------            --------
# --------  Combined  --------
# --------            --------


def wait_time(seconds):
    time.sleep(seconds/100)
    return seconds


@timer.print_time_result_dec
def _print_time_result_dec(seconds):
    time.sleep(seconds/100)
    return seconds


# --------        --------
# --------  Time  --------
# --------        --------


@timer.print_time_dec
def wait_print_time(seconds):
    time.sleep(seconds/100)
    return seconds


@timer.get_time_dec
def wait_log_time(seconds):
    time.sleep(seconds/100)
    return seconds


class TestTimer(unittest.TestCase):


    # --------            --------
    # --------  Combined  --------
    # --------            --------

    def test_run_timed_result(self):
        actual = timer.run_timed_result(wait_time, 1)
        expected = 1
        self.assertEqual(actual, expected, 'run_timed_result')

    def test_print_time_result_dec(self):
        actual = _print_time_result_dec(1)
        expected = 1
        self.assertEqual(actual, expected, 'print_time_result_dec')

    # --------          --------
    # --------  Result  --------
    # --------          --------

    def test_run_result(self):
        actual = timer.run_result(wait_time, 1)
        expected = 1
        self.assertEqual(actual, expected, 'run_result')

    def test_print_result(self):
        actual = wait_time(1)
        timer.print_result(actual, "print_result", 1)
        expected = 1
        self.assertEqual(actual, expected, 'print_result')

    # --------        --------
    # --------  Time  --------
    # --------        --------

    def test_print_time_dec(self):
        actual = wait_print_time(1)
        expected = 1
        self.assertEqual(actual, expected, 'print_time_dec')

    def test_get_time_dec(self):
        actual, time_dict = wait_log_time(1)
        timer.print_time("get_time_dec", time_dict)
        expected = 1
        self.assertEqual(actual, expected, 'get_time_dec')

    def test_print_time(self):
        begin = time.time()
        actual = wait_time(1)
        timer.print_time("print_time", {"begin": begin, "end": time.time()})
        expected = 1
        self.assertEqual(actual, expected, 'print_time')

    def test_run_timed(self):
        actual = timer.run_timed(wait_time, 1)
        expected = 1
        self.assertEqual(actual, expected, 'run_timed')
