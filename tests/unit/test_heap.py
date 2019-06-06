# MIT (c) jtankersley 2019-05-19
import unittest
from src import heap
from src import timer


multiOrderedList = [1,2,3,3,3,3,4,5,6,7,7,8,10,12,12,12,15,20,25,30,31,32]
multiUnOrderedList = [10,20,12,31,3,4,12,6,5,15,7,3,2,12,25,3,3,30,32,1,7,8]


class TestHeap(unittest.TestCase):

    def test_MinHeap(self):
        bt = heap.Heap(heap.HeapType.MINIMUM)
        for n in multiUnOrderedList:
            bt.add(n)
        actual = bt.get_in_order_list()
        expected = multiOrderedList
        print(f"test_MinHeap={actual}")
        self.assertEqual(len(actual), len(expected), "test_MinHeap")

        actual = bt.get_sorted_list()
        print(f"test_MinHeap.sorted={actual}")
        self.assertEqual(actual, expected, "test_MinHeap.sorted")

    def test_MinHeapPop(self):
        bt = heap.Heap(heap.HeapType.MINIMUM)
        for n in multiUnOrderedList:
            bt.add(n)
        actual = []
        while not bt.is_empty():
            actual.append(bt.pop())
        expected = multiOrderedList
        print(f"test_MaxHeapPop={actual}")
        self.assertEqual(actual, expected, "test_MaxHeapPop")

    def test_MaxHeap(self):
        bt = heap.Heap(heap.HeapType.MAXIMUM)
        for n in multiUnOrderedList:
            bt.add(n)
        actual = bt.get_in_order_list()
        expected = multiOrderedList
        print(f"test_MaxHeap={actual}")
        self.assertEqual(len(actual), len(expected), "test_MaxHeap")

        actual = bt.get_sorted_list()
        print(f"test_MaxHeap.sorted={actual}")
        self.assertEqual(actual, expected, "test_MaxHeap.sorted")

    def test_MaxHeapPop(self):
        bt = heap.Heap(heap.HeapType.MAXIMUM)
        for n in multiUnOrderedList:
            bt.add(n)
        actual = []
        while not bt.is_empty():
            actual.append(bt.pop())
        expected = multiOrderedList.copy()
        expected.reverse()
        print(f"test_MaxHeapPop={actual}")
        self.assertEqual(actual, expected, "test_MaxHeapPop")
