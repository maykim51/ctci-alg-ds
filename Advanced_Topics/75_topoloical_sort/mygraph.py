from enum import Enum

class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3 #??
    

class Node():
    def __init__(self, val):
        self.value = val
        self.visit_state = State.unvisited
        self.adjacent = {}
        
    def __str__(self):
        return str(self.value)


class Graph():
    def __init__(self):
        self.graph = {} #key: node's value, value: adjacents
            
    def add_node(self, value):
        if value not in self.graph:
            self.graph[value] = Node(value)
    
    def add_edge(self, src, dest, weight=0):
        if self.graph[src] and self.graph[dest]:
            self.graph[src].adjacent[dest] = weight
    
    def print_graph(self):
        printing_dict = {}
        for node in self.graph.values():
            printing_dict[node.value] = node.adjacent
        print(printing_dict)


if __name__ == '__main__':
    new_graph = Graph()
    new_graph.add_node('a')
    new_graph.add_node('b')
    new_graph.add_node('c')
    new_graph.add_edge('a','b', 2)
    new_graph.add_edge('a','c', 5)
    new_graph.add_edge('b','c', 3)
    new_graph.print_graph()
        