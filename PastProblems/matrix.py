'''
[MS SDE]
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

SOLUTIONS
1. brute force
2. BFS :: 일반 BFS + 출발점이 여러개인 점! (= 시작할때 큐에 여러개를 넣어야함! 거리의 도착점도 0임!)
3. DP :: 양쪽에서 출발하는 걸 둘다 해야 한다. 즉 왼->오 + 위-> 아래로 한번 가야 하고, 그 반대로 한번 해야 한다.

'''
import unittest

###Option1. BFS
class Solution(object):
    def updateMatrix(self, matrix):
        queue = []
        R, C = len(matrix), len(matrix[0])
        
        #save dists per cell. 0 for 0, INF for 1
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    queue.append((r,c))
                else:
                    matrix[r][c] = float("INF")
        
        for i, j in queue:
            for r, c in ((i-1, j), (i,j+1), (i+1, j), (i, j-1)):
                new_dist = matrix[i][j] +1 #neighbor dist is always 1
                if 0<= r < R and 0 <= c < C and new_dist < matrix[r][c]: #thinkg absolution conditons!!!!!!!!!!!!!
                        matrix[r][c] = new_dist
                        queue.append((r,c))
        
        return matrix  
    
    
## option 2 DP

    def updateMatrix_dp(self, matrix):
        R,C = len(matrix), len(matrix[0])
        dist = [[float("INF")]*C for i in range(R)]
        
        #traverse left to right, top to bottom
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    dist[r][c] = 0
                else:
                    dist[r][c] = min(dist[r][c], dist[r-1][c]+1, dist[r][c-1]+1)
                    
        #traverse right to left, bottom to top
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if matrix[r][c] != 0:
                    if r < R-1:
                        dist[r][c] = min(dist[r][c], dist[r+1][c]+1)
                    if c < C-1:
                        dist[r][c] = min(dist[r][c], dist[r][c+1]+1)
        
        return dist

class Test(unittest.TestCase):
    def test_matrix(self):
        sol = Solution()
        mat1  = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        mat2 = [
            [0,0,0],
            [0,1,0],
            [1,1,1]
        ]
        # self.assertEqual(sol.updateMatrix(mat1), [[0,0,0],[0,1,0],[0,0,0]])
        # self.assertEqual(sol.updateMatrix(mat2), [[0,0,0],[0,1,0],[1,2,1]])
        self.assertEqual(sol.updateMatrix_dp(mat1), [[0,0,0],[0,1,0],[0,0,0]])
        self.assertEqual(sol.updateMatrix_dp(mat2), [[0,0,0],[0,1,0],[1,2,1]])

if __name__ == "__main__":
    unittest.main()
