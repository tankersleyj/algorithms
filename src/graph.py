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
        self.verticies = self._get_verticies(self.size)

    def __str__(self):
        """Print matrix"""
        return self._get_matrix_string(self.matrix)

    def _get_verticies(self, size):
        return [f"{chr(index + 97)}" for index in range(self.size)]

    def _get_matrix_string(self, matrix):
        labels = []
        rows = []
        verticies = self._get_verticies(len(matrix))
        labels_string = ", ".join(verticies)
        rows.append(f"   {labels_string}")
        for index, row in enumerate(matrix):
            rows.append(f"{verticies[index]} {row}")
        matrix_string = "\r\n".join(rows)
        return matrix_string

    def get_shortest_distance(self, start_index, end_index):
        visited = [[0 for index in range(self.size)] for index in range(self.size)]  # empty matrix
        visited[start_index][start_index] = 1
        print(f"visited\r\n{self._get_matrix_string(visited)}")
        neighbors = self.matrix[start_index]
        return 4
