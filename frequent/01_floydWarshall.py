'''
Graph - Floyd Warshall
https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/


전체 노드들 끼리의 shortest path를 저장하는 함수
NxN 테이블 2개로 구현: dist, prev
'''
import unittest
INF = float("inf")

def floydwarshall(g):
    N = len(g)
    dist = g
    via = [[-1]*N]*N
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    via[i][j] = k
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    print(dist)
    print(via)
            
    
    return
    

#Driver

class Test(unittest.TestCase):
    
    def test_floydwarshall(self):
        graph = [
            [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]
        
        ans = [
            [0, 5, 8, 9],
            [INF, 0, 3, 4],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]

        # self.assertEqual(floydwarshall(graph), ans)
        floydwarshall(graph)

if __name__ == "__main__":
    unittest.main()
