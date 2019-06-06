#  MIT (c) jtankersley 2019-06-03

from enum import Enum


"""
2 dimensional array based graph.
diagram:
a---b
|\ /| 
| e |
|/ \|
d---c
edge_distance_matrix: 
  a b c d e
a 0 5 0 8 1
b 5 0 6 0 2
c 0 6 0 7 3
d 8 0 7 0 4
e 1 2 3 4 0
"""


""" Graph """
class Graph():

    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(self.matrix)
        self.verticies = [f"{chr(index + 97)}" for index in range(self.size)]

    def __str__(self):
        """Print matrix"""
        labels = []
        strings = []
        labels_string = ", ".join(self.verticies)
        strings.append(f"   {labels_string}")
        for index, row in enumerate(self.matrix):
            strings.append(f"{self.verticies[index]} {row}")
        string = "\r\n".join(strings)
        return str(f"{string}")

    def get_shortest_distance(self, start_index, end_index):
        visited = self.matrix.copy()
        neighbors = self.matrix[start_index]
        return 4
