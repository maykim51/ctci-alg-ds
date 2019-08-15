'''
[L60] Swap 2 numbers without using a temp variable
'''
a = 15
b = 10
a = a-b #diff
b = b+a
a = b-a #새로운 a, 즉 b에서 diff 빼줌 !!!
print(a,b)

'''
Given an array, put even numbers at even index and odd numbers at odd index
'''
'''
Given an undirected graph where each node has a letter. 
Find if a given string can be traversed starting from any node in the graph and visiting the neighboring nodes. 
Basically, it's a simple DFS on graph.  - DFS is good for checking if it exists
'''
graph = {'A': set(['B', 'C', 'T']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'T': set()}
s = 'CAT'

output = ['not in the graph.', 'yes in the graph!']     
    
def is_in_graph(graph, s, visited, stack):
    ch = s.pop(0)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
        
        if node == ch:
            if s == []:
                return True
            else:     
                ch = s.pop(0)
    
    return False
    
def dfs(graph, s):
    if s is None:
        return True
    
    if s[0] in graph:
        visited, stack = set(), [s[0]]
        return is_in_graph(graph, list(s), visited, stack)
    
    return False


print(output[dfs(graph,s)])