'''
Graph - Prim's minimum spanning tree (MST) - greedy algo 5
https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
'''
# The program is for adjacency matrix representation of the graph 


class Graph(): 
    def __init__(self, graph): 
        self.V = len(graph) 
        self.graph = graph

    # A utility function to print the constructed MST stored in parent[] 
    def printMST(self, parent): 
        print("Edge \tWeight")
        for i in range(1, self.V): 
            print(parent[i], "-", i, "\t", self.graph[i][ parent[i] ] )

    # A utility function to find the vertex with minimum distance value
    def minKey(self, key, mstSet): 
        min = 9999

        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: ##if connected to the subtree and not included yet
                min = key[v] 
                min_index = v 

        return min_index 

    def primMST(self):
        key = [9999] * self.V
        mstSet = [False] * self.V
        parent = [-1] * self.V
        key[0] = 0
        
        for _ in range(self.V-1):
            #Add minimum adjacent vertex
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            
            #update key array per this added u vertex..
            for v in range(self.V):
                if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                    key[v] = graph[u][v]
                    parent[v] = u
            
        self.printMST(parent)



graph = [ [0, 2, 0, 6, 0], 
			[2, 0, 3, 8, 5], 
			[0, 3, 0, 0, 7], 
			[6, 8, 0, 0, 9], 
			[0, 5, 7, 9, 0]] 
g = Graph(graph) 
g.primMST() 
