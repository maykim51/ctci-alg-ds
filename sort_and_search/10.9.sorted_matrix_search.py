'''
[WIP!!]
CTCI 10.9. Sorted Matrix Search: 
Given an M x N matrix in which each row and each column is sorted in ascending order, 
write a method to find an element.  

SOLUTION
1. 각 열의 최소값, 각 행의 최소값과 비교해보면 비교할 곳이 확 줄어든다.
2. 다른 해법 : 대각선을 search해서, 사사분면으로 나눈뒤 재귀해서 재탐색한다 (WIP)

'''
#option 1 - using BST
#option 2 - compare with min of row and col
# def sorted_matrix_search(mat, num): 
#     row = 0 
#     col = len(mat[0])-1
#     while row < len(mat) and col >= 0:
#         if mat[row][col] == num:
#             return (row, col)
#         elif num < mat[row][col]:
#             col -= 1
#         else: 
#             row += 1
#     return (-1, -1)


#option 3 - using diagnolly sorted!
def sorted_matrix_search(mat, num): 
    row, col = 0, 0
    
    while row < len(mat) and col < len(mat[0]): #이 과정도 bst로 할 수 있다
        if mat[row][col] == num:
            return (row, col)
        elif mat[row][col] > num:
            break
        row += 1  
        col += 1
    
    # return partition_and_search(mat, origin, dest, )
    
    
    
import unittest

class Test(unittest.TestCase):
  def test_sorted_matrix_search(self):
    mat = [[1,   2,  3,  4,  5,  6,  7,  8,  9],
           [5,  10, 15, 20, 25, 30, 35, 40, 45],
           [10, 20, 30, 40, 50, 60, 70, 80, 90],
           [13, 23, 33, 43, 53, 63, 73, 83, 93],
           [14, 24, 34, 44, 54, 64, 74, 84, 94],
           [15, 25, 35, 45, 55, 65, 75, 85, 95],
           [16, 26, 36, 46, 56, 66, 77, 88, 99]]
    self.assertEqual(sorted_matrix_search(mat, 10), (1,1))
    self.assertEqual(sorted_matrix_search(mat, 13), (3,0))
    self.assertEqual(sorted_matrix_search(mat, 14), (4,0))
    self.assertEqual(sorted_matrix_search(mat, 16), (6,0))
    self.assertEqual(sorted_matrix_search(mat, 56), (6,4))
    self.assertEqual(sorted_matrix_search(mat, 65), (5,5))
    self.assertEqual(sorted_matrix_search(mat, 74), (4,6))
    self.assertEqual(sorted_matrix_search(mat, 99), (6,8))

if __name__ == "__main__":
  unittest.main()
