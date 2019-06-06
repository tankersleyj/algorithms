# MIT (c) jtankersley 2019-05-19
import unittest
from src import list
from src import timer


class TestList(unittest.TestCase):

    def test_link_doubleLinkList_head(self):
        dll = list.DoubleLinkList()
        dll.add_head(1)
        dll.add_head(2)
        dll.add_head(3)
        actual = timer.run_timed_result(str, dll)
        expected = "3,2,1"
        self.assertEqual(actual, expected, "test_link_dllHead.1")

        actual = timer.run_timed_result(dll.peak_head)
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllHead.2")

        actual = actual = timer.run_timed_result(dll.pop_head)
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllHead.3")

        actual = timer.run_timed_result(str, dll)
        expected = "2,1"
        self.assertEqual(actual, expected, "test_link_dllHead.4")

    def test_link_doubleLinkList_tail(self):
        dll = list.DoubleLinkList()
        dll.add_tail(1)
        dll.add_tail(2)
        dll.add_tail(3)
        actual = timer.run_timed_result(str, dll)
        expected = "1,2,3"
        self.assertEqual(actual, expected, "test_link_dllTail.1")

        actual = timer.run_timed_result(dll.peek_tail)
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllTail.2")

        actual = actual = timer.run_timed_result(dll.pop_tail)
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllTail.3")

        actual = timer.run_timed_result(str, dll)
        expected = "1,2"
        self.assertEqual(actual, expected, "test_link_dllTail.4")
