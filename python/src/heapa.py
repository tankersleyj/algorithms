#  MIT (c) jtankersley 2019-06-04

from enum import Enum


"""
Array based Heap.
left_child_index = index * 2 + 1
right_child_index = index * 2 + 2
parentIndex = (index - 1) // 2
              00
      01              02
  03      04      05      06
07  08  09  10  11  12  13  14
"""


class HeapType(Enum):
    MINIMUM = 1
    MAXIMUM = 2


""" Min or Max array based Heap."""
class Heap():

    def __init__(self, type, list=[]):
        self.heap = []
        self.type = type
        if len(list) > 0:
            for index, value in enumerate(list):
                self.push(value)

    def __str__(self):
        """Print value in-order."""
        if self.type == HeapType.MINIMUM:
            return str(self.get_sorted_list())
        else:
            return str(self.get_sorted_list(True))

    def is_empty(self):
        return True if len(self.heap) == 0 else False

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _parent_index(self, index):
        return (index - 1) // 2

    def _child_left_index(self, index):
        return index * 2 + 1

    def _child_right_index(self, index):
        return index * 2 + 2

    def _balance_up(self, index):
        if index > 0:
            value = self.heap[index]
            parent_index = self._parent_index(index)
            parent_value = self.heap[parent_index]
            if self.type == HeapType.MAXIMUM and value > parent_value:
                self._swap(index, parent_index)
                self._balance_up(parent_index)
            if self.type == HeapType.MINIMUM and value < parent_value:
                self._swap(index, parent_index)
                self._balance_up(parent_index)

    def push(self, value):
        self.heap.append(value)
        last_index = len(self.heap) - 1
        self._balance_up(last_index)      
 
    def _balance_down(self, index):
        max_index = len(self.heap) - 1
        left_child_index = self._child_left_index(index)
        right_child_index = self._child_right_index(index)
        if left_child_index <= max_index:
            self._balance_up(left_child_index)
            self._balance_down(left_child_index)
        if right_child_index <= max_index:
            self._balance_up(right_child_index)
            self._balance_down(right_child_index)

    def pop(self):
        last_index = len(self.heap) - 1
        if last_index >= 0:
            value = self.heap[0]
            if last_index > 0:
                self.heap[0] = self.heap.pop()
                self._balance_down(0)
            else:
                self.heap.pop()
            return value       

    def get_sorted_list(self, reverse=False):
        copy_list = self.heap.copy()
        copy_list.sort(reverse=reverse)
        return copy_list
