# MIT (c) jtankersley 2019-05-19
import unittest
from src import list
from src import timer


class TestSort(unittest.TestCase):

    def test_link_doubleLinkList_head(self):
        dll = list.DoubleLinkList()
        dll.addHead(1)
        dll.addHead(2)
        dll.addHead(3)
        actual = timer.runTimedResult(str, dll)
        expected = "3,2,1"
        self.assertEqual(actual, expected, "test_link_dllHead.1")

        actual = timer.runTimedResult(dll.peekHead)
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllHead.2")

        actual = actual = timer.runTimedResult(dll.popHead)
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllHead.3")

        actual = timer.runTimedResult(str, dll)
        expected = "2,1"
        self.assertEqual(actual, expected, "test_link_dllHead.4")

    def test_link_doubleLinkList_tail(self):
        dll = list.DoubleLinkList()
        dll.addTail(1)
        dll.addTail(2)
        dll.addTail(3)
        actual = timer.runTimedResult(str, dll)
        expected = "1,2,3"
        self.assertEqual(actual, expected, "test_link_dllTail.1")

        actual = timer.runTimedResult(dll.peekTail)
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllTail.2")

        actual = actual = timer.runTimedResult(dll.popTail)
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllTail.3")

        actual = timer.runTimedResult(str, dll)
        expected = "1,2"
        self.assertEqual(actual, expected, "test_link_dllTail.4")
