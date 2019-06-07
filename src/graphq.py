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
    
    def __init__(self, distance, start_node, end_node):
        self.distance = distance
        self.start_node = start_node
        self.end_node = end_node

""" HeapQ based Graph with Dijkstra shortest distance search """
class Node():

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.prior_node = None
        self.edges = []
        self.distance_from_start_node = sys.maxsize

    def __cmp__(self, other_node):
        self.cmp(self.distance_from_start_node, other_node.distance_from_start_node)

    def __lt__(self, other_node):
        return self.distance_from_start_node < other_node.distance_from_start_node

class Graph():

    def calculate_distances_from(start_node):
        heap = []
        start_node.distance_from_start_node = 0
        heapq.heappush(heap, start_node)
        while len(heap) > 0:
            next_node = heapq.heappop(heap)
            if next_node.visited == False:
                next_node.visited = True
                print(f"process node {next_node.name}")
                for edge in next_node.edges:
                    print(f"    process edge {edge.end_node.name}")
                    new_distance = edge.start_node.distance_from_start_node + edge.distance
                    if new_distance < edge.end_node.distance_from_start_node:
                        edge.end_node.prior_node = edge.start_node
                        edge.end_node.distance_from_start_node = new_distance
                        if edge.end_node.visited == False:
                            heapq.heappush(heap, edge.end_node)

    def get_distance_to(end_node):
        return end_node.distance_from_start_node

    def show_distances(nodes):
        for node in nodes:
            prior_node_name = node.prior_node.name if node.prior_node else ''
            print(f"{node.name}.distance from start={node.distance_from_start_node}, prior node={prior_node_name}")
