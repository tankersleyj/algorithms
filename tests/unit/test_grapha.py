# MIT (c) jtankersley 2019-06-05
import unittest
from src import grapha_sandbox
from src import timer

graph_matrix = [
    [0,5,0,8,1],
    [5,0,6,0,2],
    [0,6,0,7,3],
    [8,0,7,0,4],
    [1,2,3,4,0]
]


class TestGraph(unittest.TestCase):

    def test_Graph_Temp(self):
        g = grapha_sandbox.Graph(graph_matrix)
        print(f"distance matrix:\r\n{str(g)}")
        actual = g.get_shortest_distance(0,2)
        expected = 4
        self.assertEqual(actual, expected, "test_Graph.get_shortest_distance")
