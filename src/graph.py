#  MIT (c) jtankersley 2019-06-05

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
        """Print matrix."""
        return self._get_matrix_string(self.matrix)

    def _get_verticies(self, size):
        return [f"{chr(index + 97)}" for index in range(self.size)]

    def _create_matrix(self, size, fill_value=0):
        return [[fill_value for index in range(self.size)] for index in range(self.size)]

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

    # in-progress
    def get_shortest_distance_dijkstra(self, start_index, end_index):
        visited = self._create_matrix(self.size, 0)
        visited[start_index][start_index] = 1
        visited[end_index][end_index] = 1
        print(f"visited:\r\n{self._get_matrix_string(visited)}")
        start_neighbors = self.matrix[start_index]
        end_neighbors = self.matrix[end_index]
        return 4  # faker

    # in-progress
    def get_shortest_distance_double_bfs(self, start_index, end_index):
        visited = self._create_matrix(self.size, 0)
        visited[start_index][start_index] = 1
        visited[end_index][end_index] = 1
        print(f"visited:\r\n{self._get_matrix_string(visited)}")
        start_neighbors = self.matrix[start_index]
        end_neighbors = self.matrix[end_index]
        return 4  # faker
