'''
Graph - union find (disjoint set)
https://www.geeksforgeeks.org/union-find/ (video is good)
https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html

disjoint set: 서로 원소가 겹치지 않는 부분집합들
union find: disjoint set을 표현할때 사용하는 알고리즘

SOLUTION
create parent array, initiate with -1
FIND per vertext in one edge, then UNION if not in same subset. (== not equal parents)

'''

# Python Program for union-find algorithm to detect cycle in a undirected graph 
# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both 

from collections import defaultdict 

#This class represents a undirected graph using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 


	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A utility function to find the subset of an element i 
	def find_parent(self, parent,i): 
		if parent[i] == -1: 
			return i 
		if parent[i]!= -1: 
			return self.find_parent(parent,parent[i]) 

	# A utility function to do union of two subsets 
	def union(self,parent,x,y): 
		x_set = self.find_parent(parent, x) 
		y_set = self.find_parent(parent, y) 
		parent[x_set] = y_set 



	# The main function to check whether a given graph 
	# contains cycle or not 
	def isCyclic(self): 
		
		# Allocate memory for creating V subsets and 
		# Initialize all subsets as single element sets 
		parent = [-1]*(self.V) 

		# Iterate through all edges of graph, find subset of both 
		# vertices of every edge, if both subsets are same, then 
		# there is cycle in graph. 
		for i in self.graph: 
			for j in self.graph[i]: 
				x = self.find_parent(parent, i) 
				y = self.find_parent(parent, j) 
				if x == y: 
					return True
				self.union(parent,x,y) 


# Create a graph given in the above diagram 
g = Graph(3) 
g.addEdge(0, 1) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 

if g.isCyclic(): 
	print("Graph contains cycle") 
else : 
	print("Graph does not contain cycle ")

#This code is contributed by Neelam Yadav 
