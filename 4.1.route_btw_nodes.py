""" 
CTCI 4.1. Route between Nodes

Given a directed graph, design an algorithm to find out whether there is a route between two nodes. 
"""

### Option 1
# graph = {'A': ['B', 'C'],
#          'B': ['A', 'D', 'E'],
#          'C': ['A', 'F'],
#          'D': ['B', 'Z'],
#          'E': ['B', 'F'],
#          'F': ['C', 'E'],
#          'Z': ['C']}


# def hasRoute(graph, start, goal):
#     if start not in graph or goal not in graph:
#         return False
    
#     queue = [(start, [start])]
#     while queue:
#         (node, path) = queue.pop(0)
#         for next in set(graph[node]) - set(path):
#             if next == goal:
#                 path_to_goal = path + [next]
#                 return True, path_to_goal
#             else:
#                 queue.append((next, path + [next]))
#     return False


# print('A and Z is connected: {}'.format(hasRoute(graph, 'A', 'Z')))
# print('Z and A is connected: {}'.format(hasRoute(graph, 'Z', 'A')))


###Option 2
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B', 'Z']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'Z': set('C')}


def hasRoute(graph, start, goal):
    if start not in graph or goal not in graph:
        return False
    
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next in graph[node] - set(path):
            if next == goal:
                path_to_goal = path + [next]
                return True, path_to_goal
            else:
                queue.append((next, path + [next]))
    return False



print('A and Z is connected: {}'.format(hasRoute(graph, 'A', 'Z')))
print('Z and A is connected: {}'.format(hasRoute(graph, 'Z', 'A')))
