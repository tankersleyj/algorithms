# MIT (c) jtankersley 2019-05-19
import unittest
from src import graph
from src import timer

graph_matrix = [
    [0,5,0,8,1],
    [5,0,6,0,2],
    [0,6,0,7,3],
    [8,0,7,0,4],
    [1,2,3,4,0]
]


class TestGraph(unittest.TestCase):

    def test_Search(self):
        g = graph.Graph(graph_matrix)
        print(f"{str(g)}")
        actual = g.get_shortest_distance(0,2)
        expected = 4
        self.assertEqual(actual, expected, "test_Graph")
