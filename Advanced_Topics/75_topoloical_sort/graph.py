## Option 1

"""
The graph will be directed and the edges can hold weights.

We will have three classes, a State class, a Node class, and finally the Graph class.

We're going to be taking advantage of two built-in tools here, OrderDict and Enum

"""
from enum import Enum

class State(Enum):
    unvisited = 1 #White
    visited = 2 #Black
    visiting = 3 #


from collections import OrderedDict

class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node, val = weight

    def __str__(self):
        return str(self.num)


class Graph:
    
    def __init__(self):
        self.nodes = OrderedDict()  # key = node id, val = node

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight


#### Option 2


# class Graph:
#     '''
#     In order to implement a Graph as an Adjacency List 
#     what we need to do is define the methods our Adjacency List object will have:
#     Graph() creates a new, empty graph.
#     addVertex(vert) adds an instance of Vertex to the graph.
#     addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
#     addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
#     getVertex(vertKey) finds the vertex in the graph named vertKey.
#     getVertices() returns the list of all vertices in the graph.
#     in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
#     '''
#     def __init__(self):
# #         self.nodes = set() # all the vertexes in the graph -- could be done in the edges part
#         self.connections = {} # all the connections start_vertex:{end_vertex:weigth}
        
# #     def add_node(self, node):
# #         self.nodes.add(node)
    
#     def contains(self, v):
#         return v in self.connections.keys()
        
#     def connect(self, start, end, weight=1):
# #         v = self.get_vertex(str(from_vertex)) or Vertex(str(from_vertex))
#         if start not in self.connections:
#             self.connections[start] = {end:weight} 
#         else:
#             self.connections[start][end] = weight
            
#         if end not in self.connections:
#             self.connections[end] = {}

#     def get_nodes(self):
#         return self.connections.keys()
        
# #     assume there is one and only one start node (no one points to it) in the directed graph
#     def get_start_vertex(self):
#         cadidates = set(self.get_nodes())
#         for end in self.connections.values():
#             for k in end.keys():
#                 if k in cadidates:
#                     cadidates.remove(k)
# #         return set(self.get_nodes()) - set(end_nodes)
#         return cadidates
        
#     def paint(self):
#         print(self.connections)