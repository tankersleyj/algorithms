# MIT (c) jtankersley 2019-05-19
import unittest
from src import link
from src import timer


class TestSort(unittest.TestCase):

    def test_link_dllHead(self):
        dll = link.DoubleList()
        dll.addHead(1)
        dll.addHead(2)
        dll.addHead(3)
        actual = str(dll)
        expected = "3,2,1"
        self.assertEqual(actual, expected, "test_link_dllHead.1")

        actual = dll.peekHead()
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllHead.2")

        actual = dll.popHead()
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllHead.3")

        actual = str(dll)
        expected = "2,1"
        self.assertEqual(actual, expected, "test_link_dllHead.4")

    def test_link_dllTail(self):
        dll = link.DoubleList()
        dll.addTail(1)
        dll.addTail(2)
        dll.addTail(3)
        actual = str(dll)
        expected = "1,2,3"
        self.assertEqual(actual, expected, "test_link_dllTail.1")

        actual = dll.peekTail()
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllTail.2")

        actual = dll.popTail()
        expected = 3
        self.assertEqual(actual, expected, "test_link_dllTail.3")

        actual = str(dll)
        expected = "1,2"
        self.assertEqual(actual, expected, "test_link_dllTail.4")

        # print(f"dll.Tail.data={dll.head.data}")
        # print(f"dll={str(dll)}")
        # print(f"{str(dll)}")
        # print(f"{dll.toString()}")
        # actual = timer.runTimedResult(sort.bubbleSort, unordered_link.copy())
        # expected = ordered_link
        # self.assertEqual(actual, expected, 'bubbleSort')
