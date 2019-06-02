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


@timer.printTimedResult_dec
def _printTimedResult_dec(seconds):
    time.sleep(seconds/100)
    return seconds


# --------        --------
# --------  Time  --------
# --------        --------


@timer.printTime_dec
def wait_printTime(seconds):
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

    def test_runTimedResult(self):
        actual = timer.runTimedResult(wait_time, 1)
        expected = 1
        self.assertEqual(actual, expected, 'runTimedResult')

    def test_printTimedResult_dec(self):
        actual = _printTimedResult_dec(1)
        expected = 1
        self.assertEqual(actual, expected, 'printTimedResult_dec')

    # --------          --------
    # --------  Result  --------
    # --------          --------

    def test_runResult(self):
        actual = timer.runResult(wait_time, 1)
        expected = 1
        self.assertEqual(actual, expected, 'runResult')

    def test_printResult(self):
        actual = wait_time(1)
        timer.printResult(actual, "printResult", 1)
        expected = 1
        self.assertEqual(actual, expected, 'printResult')

    # --------        --------
    # --------  Time  --------
    # --------        --------

    def test_printTime_dec(self):
        actual = wait_printTime(1)
        expected = 1
        self.assertEqual(actual, expected, 'printTime_dec')

    def test_get_time_dec(self):
        actual, time_dict = wait_log_time(1)
        timer.printTime("get_time_dec", time_dict)
        expected = 1
        self.assertEqual(actual, expected, 'get_time_dec')

    def test_printTime(self):
        begin = time.time()
        actual = wait_time(1)
        timer.printTime("printTime", {"begin": begin, "end": time.time()})
        expected = 1
        self.assertEqual(actual, expected, 'printTime')

    def test_runTimed(self):
        actual = timer.runTimed(wait_time, 1)
        expected = 1
        self.assertEqual(actual, expected, 'runTimed')
