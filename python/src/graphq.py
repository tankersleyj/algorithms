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


""" HeapQ based Graph with Dijkstra shortest distance search """
class Node():

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.prior_node = None
        self.edges = []
        self.total_distance = sys.maxsize

    def __cmp__(self, other_node):
        self.cmp(self.total_distance, other_node.total_distance)

    def __lt__(self, other_node):
        return self.total_distance < other_node.total_distance


class Edge():
    
    def __init__(self, distance, start_node, end_node):
        self.distance = distance
        self.start_node = start_node
        self.end_node = end_node


class Graph():

    def calculate_distances_from(start_node):
        heap = []
        start_node.total_distance = 0
        heapq.heappush(heap, start_node)
        while len(heap) > 0:
            next_node = heapq.heappop(heap)
            next_node.visited = True
            print(f"visit node {next_node.name}, distance from start = {next_node.total_distance}")
            for edge in next_node.edges:
                print(f"    calculate edge {edge.end_node.name}, distance = {edge.distance}")
                new_total_distance = edge.start_node.total_distance + edge.distance
                if new_total_distance < edge.end_node.total_distance:
                    edge.end_node.prior_node = edge.start_node
                    edge.end_node.total_distance = new_total_distance
                    if edge.end_node.visited == False:
                        heapq.heappush(heap, edge.end_node)

    def get_distance_to(end_node):
        return end_node.total_distance

    def show_distances(nodes):
        sorted_nodes = []
        for node in nodes:
            heapq.heappush(sorted_nodes, node)
        while len(sorted_nodes) > 0:
            node = heapq.heappop(sorted_nodes)
            prior_node_name = node.prior_node.name if node.prior_node else ''
            print(f"{node.name}.distance from start={node.total_distance}, prior node={prior_node_name}")
