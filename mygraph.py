class Node():
    def __init__(self, value):
        


# class Graph():

#     def __init__(self):
#         self.max_vertices = 6
#         self.vertices = [0] * self.max_vertices
#         self.count = 0

#     def addNode(self, x):
#         if self.count < self.max_vertices:
#             self.vertices[self.count] = x
#             self.count += 1
#         else:
#             print ("Graph full")

#     def getNodes(self):
#         return self.vertices


# class Node():

#     def __init__(self, vertex, adjacentLength):
#         self.adjacent = [0] * adjacentLength
#         self.vertex = vertex
#         self.adjacentCount = 0
#         self.visited = False

#     def addAdjacent(self, x):
#         if self.adjacentCount < len(self.adjacent):
#             self.adjacent[self.adjacentCount] = x
#             self.adjacentCount += 1
#         else:
#             print ("No more adjacent nodes can be added")

#     def getAdjacent(self):
#         return self.adjacent

#     def getVertex(self):
#         return self.vertex
