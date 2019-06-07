#  MIT (c) jtankersley 2019-06-05

import sys
import heapq


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


class Edge():
    
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end

""" HeapQ based Graph with Dijkstra shortest distance search """
class Node():

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.prior_node = None
        self.edges = []
        self.distance_from_start = sys.maxsize

    def __cmp__(self, other):
        self.cmp(self.distance_from_start, other.distance_from_start)

    def __lt__(self, other):
        return self.distance_from_start < other.distance_from_start

class Graph():

    def calculate_distances_from(start):
        heap = []
        start.distance_from_start = 0
        heapq.heappush(heap, start)
        while len(heap) > 0:
            vertext = heapq.heappop(heap)
            for edge in vertext.edges:
                new_distance = edge.start.distance_from_start + edge.weight
                if new_distance < edge.end.distance_from_start:
                    edge.end.prior_node = edge.start
                    edge.end.distance_from_start = new_distance
                    heapq.heappush(heap, edge.end)

    def get_distance_to(end):
        return end.distance_from_start

    def _get_prior_nodes(node):
        prior_nodes = []
        if node.prior_node:
            prior = node.prior_node
            while not prior == None:
                prior_nodes.append(prior)
                prior = prior.prior_node
        return prior_nodes

    def show_distances(nodes):
        for node in nodes:
            prior_nodes = Graph._get_prior_nodes(node)
            prior_nodes_names = [node.name for node in prior_nodes]
            print(f"{node.name}.distance={node.distance_from_start}, prior_nodes={prior_nodes_names}")
