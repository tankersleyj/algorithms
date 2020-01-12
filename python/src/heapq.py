#  MIT (c) jtankersley 2019-06-04

import heapq


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


""" Min array based Heap using Python heapq."""
class HeapQ():

    def __init__(self, list):
        self.heap = []
        if len(list) > 0:
            for index, value in enumerate(list):
                self.push(value)

    def __str__(self):
        """Print value in-order."""
        return str(self.get_sorted_list())

    def is_empty(self):
        return True if len(self.heap) == 0 else False

    def push(self, value):
        heapq.heappush(self.heap, value)    
 
    def pop(self):
        last_index = len(self.heap) - 1
        if last_index >= 0:
            return heapq.heappop(self.heap)      

    def get_sorted_list(self, reverse=False):
        copy_list = self.heap.copy()
        copy_list.sort(reverse=reverse)
        return copy_list
