#  MIT (c) jtankersley 2019-06-03

from enum import Enum


"""
Array based Heap.
leftChildIndex = index * 2 + 1
rightChildIndex = index * 2 + 2
parentIndex = (index - 1) // 2
              00
      01              02
  03      04      05      06
07  08  09  10  11  12  13  14
"""


class HeapType(Enum):
    MINIMUM = 1
    MAXIMUM = 2


""" Basic Min or Max Heap, distinct keys, non-sorted. """
class Heap():

    def __init__(self, type):
        self.heap = []
        self.type = type

    def __str__(self):
        """Print value in-order."""
        return str(self.get_in_order_list())

    def _swap(self, index1, index2):
        save = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = save

    def _balance_up(self, index):
        if index > 0:
            value = self.heap[index]
            parent_index = (index - 1) // 2
            parent_value = self.heap[parent_index]
            if self.type == HeapType.MAXIMUM and value > parent_value:
                self._swap(index, parent_index)
                self._balance_up(parent_index)
            if self.type == HeapType.MINIMUM and value < parent_value:
                self._swap(index, parent_index)
                self._balance_up(parent_index)

    def add(self, value):
        self.heap.append(value)
        last_index = len(self.heap) - 1
        self._balance_up(last_index)       

    def get_in_order_list(self):
        return self.heap


""" Multi-value Heap. """
class MultiHeap():

    def __init__(self, type):
        self.heap = []
        self.count = []
        self.type = type

    def __str__(self):
        """Print value in-order."""
        return str(self.get_in_order_list())

    def _swap(self, list, index1, index2):
        save = list[index1]
        list[index1] = list[index2]
        list[index2] = save

    def _balance_up(self, index):
        if index > 0:
            value = self.heap[index]
            parent_index = (index - 1) // 2
            parent_value = self.heap[parent_index]
            if (self.type == HeapType.MAXIMUM and value > parent_value) or \
                (self.type == HeapType.MINIMUM and value < parent_value):
                self._swap(self.heap, index, parent_index)
                self._swap(self.count, index, parent_index)
                self._balance_up(parent_index)

    def add(self, value):
        last_index = len(self.heap) - 1
        if last_index < 0:
            self.heap.append(value)
            self.count.append(1)
        else:
            last_value = self.heap[last_index]
            if value == last_value:
                self.count[last_index] += 1
            else:
                self.heap.append(value)
                self.count.append(1)
                self._balance_up(last_index)       

    def get_in_order_list(self):
        multiList = []
        for index, value in enumerate(self.heap):
            for i in range(self.count[index]):
                multiList.append(value)
        return multiList
