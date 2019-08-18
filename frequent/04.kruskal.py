'''
Graph - Kruskal Algorithm - greedy algo 
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
https://www.youtube.com/watch?v=LQ3JHknGy8c (good) / https://blog.naver.com/ndb796/221230994142 

그래프의 노드를 최소비용으로 연결하는 알고리즘 (최소 비용 spanning tree를 구하는 알고리즘)
SOLUTION : 간선을 거리가 짧은 순서대로 그래프에 포함시키면 어떨까!!
1. 간선 정렬
2. 정렬된 간선 중 작은 것부터 그래프에 포함
3. 포함시킬때 union-find 방법으로(부모 노드) 사이클이 없는 지 확인
4. 사이클이 없는 짧은 간선만 포함시킨다

'''
from collections import defaultdict 

class Graph: 
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = []

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    
    def union(self, parent, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        parent[yroot] = xroot

    def KruskalMST(self): 
            res =[]

            #1. sort
            self.graph = sorted(self.graph, key=lambda x: x[2])
            
            
            #2. prep for cycle detection - find and union
            parent = []
            for node in range(self.V): 
                parent.append(node) 
            
            e = 0 #number of edges
            i = 0 # index of graph node
            while e < self.V-1:
                u, v, w = self.graph[i]
                i += 1
                if self.find(parent,u) != self.find(parent, v):
                    e +=1 
                    res.append([u,v,w])
                    self.union(parent, self.find(parent, u), self.find(parent, v))
                    
        
            print("Following are the edges in the constructed MST")
            for u,v,weight in res: 
                print ("%d -- %d == %d" % (u,v,weight)) 


# Driver code 
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

# g.KruskalMST() 
g.KruskalMST()

