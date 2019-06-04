# MIT (c) jtankersley 2019-05-19
import unittest
from src import heap
from src import timer


orderedList = [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]
unOrderedList = [10,20,31,4,6,5,15,2,12,25,3,30,32,1,7,8]


class TestSort(unittest.TestCase):

    def test_MaxHeap(self):
        bt = heap.Heap(heap.HeapType.MAXIMUM)
        for n in unOrderedList:
            bt.add(n)
        actual = bt.get_in_order_list()
        expected = orderedList
        self.assertEqual(len(actual), len(expected), "test_MaxHeap")

    def test_MinHeap(self):
        bt = heap.Heap(heap.HeapType.MINIMUM)
        for n in unOrderedList:
            bt.add(n)
        actual = bt.get_in_order_list()
        expected = orderedList
        self.assertEqual(len(actual), len(expected), "test_MinHeap")
