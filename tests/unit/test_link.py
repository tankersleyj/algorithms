# MIT (c) jtankersley 2019-05-19
import unittest
from src import link
from src import timer


class TestSort(unittest.TestCase):

    def test_link_dll(self):
        dll = link.DoubleList()
        dll.addHead(1)
        dll.addHead(2)
        dll.addHead(3)
        actual = str(dll)
        expected = "3,2,1"
        self.assertEqual(actual, expected, "test_link_dll.1")

        actual = dll.peekHead()
        expected = 3
        self.assertEqual(actual, expected, "test_link_dll.2")

        actual = dll.popHead()
        expected = 3
        self.assertEqual(actual, expected, "test_link_dll.3")

        actual = str(dll)
        expected = "2,1"
        self.assertEqual(actual, expected, "test_link_dll.4")

        # print(f"dll.head.data={dll.head.data}")
        # print(f"dll={str(dll)}")
        # print(f"{str(dll)}")
        # print(f"{dll.toString()}")
        # actual = timer.runTimedResult(sort.bubbleSort, unordered_link.copy())
        # expected = ordered_link
        # self.assertEqual(actual, expected, 'bubbleSort')
