'''
CTCI 8.2. Robot in a Grid: 

Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
The robot can only move in two directions, right and down, but certain cells are "off limits" 
such that the robot cannot step on them. 

Design an algorithm to find a path for the robot from the top left to the bottom right. 

'''
'''
f(r,c) = f(r,c-1) + f(r-1, c)
use tuple for points (row, col)
'''


### Option 1: Solution with recursion O(2^r+c)
def getPath(maze):
    if maze == None or len(maze) == 0:
        return None
    path = [] 
    if isPath(maze, len(maze)-1, len(maze[0])-1, path):
        return path
    return None

def isPath(maze, row, col, path):
    #base case / how to terminate recursion / if out of bounds or not available, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    
    isAtOrigin = (row == 0) and (col == 0)

    #if there's a path from the start to here, add my location
    if isAtOrigin or isPath(maze, row, col-1, path) or isPath(maze, row-1, col,path):
        point = (row,col)
        path.append(point)
        return True

    return False

### Option 2: Solution with memoization 
def getPathMemoized(maze):
    if maze == None or len(maze) == 0:
        return None
    path = []
    failedPoints = []
    if isPathMemoized(maze, len(maze)-1, len(maze[0])-1, path, failedPoints):
        return path
    return None

def isPathMemoized(maze, row, col, path, failedPoints):
    #If out of bounds or not availabe, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    
    point = (row,col)

    # if we've already visisted this cell, return
    if point in failedPoints:
        return False

    isAtOrigin = (row == 0) and (col == 0)

    #If there's a path from start to my current location, add my location
    if isAtOrigin or isPathMemoized(maze, row, col-1, path, failedPoints) or isPathMemoized(maze, row-1, col, path, failedPoints):
        path.append(point)
        return True

    failedPoints.append(point) 
    return False

import unittest

class Test(unittest.TestCase):
  def test_path_through_grid(self):
    grid = [[True, True, True, True, True, True, False],
            [True, False, False, True, False, False, True],
            [True, True, False, True, True, True, True],
            [False, False, True, True, True, False, True]]
    self.assertEqual(getPathMemoized(grid), [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6)])
    self.assertEqual(getPathMemoized(grid), [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6)])

if __name__ == "__main__":
  unittest.main()
