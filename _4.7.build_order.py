'''
_오래걸렸음
CTCI 4.7. Build Order

You are given a list of projects and a list of dependencies 
(which is a list of pairs of projects, where the second project is dependent on the first project). 
All of a project's dependencies must be built before the project is. 

Find a build order that will allow the projects to be built. 
If there is no valid build order, return an error. 

EXAMPLE Input: projects: a, b, c, d, e, f 
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) 
Output: f, e, a, b, d, c 
'''
'''
SOLLUTION: external sort, topological sort
'''
import unittest

def build_order(projects, dependencies):
    #base case (check + condition to terminate the recursion)
    if projects is None:
        return None
    
    #generate graph = (data, Node(data))
    graph = {} 
    for data in projects:
        graph[data] = Node(data)
    for (start, dest) in dependencies:
        graph[start].add_outbound(graph[dest])

    queue = []
    for node in graph.values():
        if node.dependencies == 0:
            queue.append(node)
    
    output = []
    while queue:
        node = queue.pop(0)
        output.append(node.data)
        for dest in node.outbounds:
            dest.dependencies -= 1
            if dest.dependencies == 0:
                queue.append(dest)
    
    if len(output) < len(projects):
        return Exception("Cycle detected") ##!!!!!!!!!!!!!!!!!!!!
    return output


class Node():
    def __init__(self, data):
        self.data = data
        self.outbounds = []
        self.dependencies = 0
    
    def add_outbound(self, node):
        self.outbounds.append(node)
        node.dependencies += 1
        

class Test(unittest.TestCase):
  def test_build_order(self):
    projects = ["A", "B", "C", "D", "E", "F", "G"]
    dependencies1 = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
        ("A", "E"), ("B", "E"), ("D", "G")]
    self.assertEqual(build_order(projects, dependencies1),
        ["D", "F", "G", "B", "C", "A", "E"])
    dependencies2 = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
    self.assertEqual(build_order(projects, dependencies2).__class__, Exception)
    dependencies3 = [("A", "B"), ("A", "C"), ("E", "A"), ("E", "B"), ("A", "F"),
        ("B", "F"), ("C", "F"), ("G", "D")]
    self.assertEqual(build_order(projects, dependencies3),
        ["E", "G", "A", "D", "B", "C", "F"])

if __name__ == "__main__":
  unittest.main()
