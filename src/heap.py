#  MIT (c) jtankersley 2019-06-03

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

    def __init__(self, type):
        self.heap = []
        self.type = type

    def __str__(self):
        """Print value in-order."""
        return str(self.get_in_order_list())

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

    def add(self, value):
        self.heap.append(value)
        last_index = len(self.heap) - 1
        self._balance_up(last_index)      
 
    def _balance_down(self, index):
        max_index = len(self.heap) - 1
        if index < max_index:
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
            print(f"pop={value}")
            if last_index > 0:
                self.heap[0] = self.heap.pop()
                self._balance_down(0)
            else:
                self.heap.pop()
            return value       

    def get_in_order_list(self):
        return self.heap

    def get_sorted_list(self):
        copy_list = self.heap.copy()
        copy_list.sort()
        return copy_list
