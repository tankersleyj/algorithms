# MIT (c) jtankersley 2019-06-05
import unittest
from src import graphq as gq
from src import timer

"""
2 dimensional heapq based graph.
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


class TestGraphQ(unittest.TestCase):

    def test_GraphQ(self):

        n1, n2, n3, n4, n5  = gq.Node("a"), gq.Node("b"), gq.Node("c"), gq.Node("d"), gq.Node("e")
        e1, e2, e3          = gq.Edge(5,n1,n2), gq.Edge(8,n1,n4), gq.Edge(1,n1,n5)
        e4, e5, e6          = gq.Edge(5,n2,n1), gq.Edge(6,n2,n3), gq.Edge(2,n2,n5)
        e7, e8, e9          = gq.Edge(6,n3,n2), gq.Edge(7,n3,n4), gq.Edge(3,n3,n5)
        e10, e11, e12       = gq.Edge(8,n4,n1), gq.Edge(7,n4,n3), gq.Edge(4,n4,n5)
        e13, e14, e15, e16  = gq.Edge(1,n5,n1), gq.Edge(2,n5,n2), gq.Edge(3,n5,n3), gq.Edge(4,n5,n4)

        n1.edges += [e1, e2, e3]
        n2.edges += [e4, e5, e6]
        n3.edges += [e7, e8, e9]
        n4.edges += [e10, e11, e12]
        n5.edges += [e13, e14, e15]

        gq.Graph.calculate_distances_from(n1)
        actual = gq.Graph.get_distance_to(n3)
        gq.Graph.show_distances([n1, n2, n3, n4, n5])
        expected = 4
        self.assertEqual(actual, expected, "test_GraphQ.get_distance_to")