'''
CTCI 10.5. Sparse Search: 산재한 탐색?

Given a sorted array of strings that is interspersed with empty strings, 
write a method to find the location of a given string. 

EXAMPLE 
Input: ball,{"at", "" , '"' , "" , "ball", "" , "" , "car", "" , '"' , "dad", '"' }
Output:4 

SOLUTION
BST + mid찾을때 ""이면 가까운 곳으로 탐색해 나간다
'''
def sparse_search(array, num, first=0, last=None):
  
  if last == None:
    last = len(array)-1
  
  if first >= last:
    return -1
  
  mid = (first + last) //2
  #mid 수정
  if array[mid] == 0:
    left = mid -1
    right = mid +1
    while(True):
          if left < first and right > last:
              return -1
          if left >= first and array[left] != 0:
                mid = left
                break
          if right <= last and array[right] != 0:
                mid = right
                break
          left -= 1
          right += 1
  
  #본업
  if array[mid] == num:
        return mid
  elif num < array[mid]:
        return sparse_search(array, num, first, mid-1)
  elif num > array[mid]:
        return sparse_search(array, num, mid+1, last)



import unittest

class Test(unittest.TestCase):
  def test_sparse_search(self):
    array = [0, 0, 7, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 37, 40, 0, 0, 0]
    self.assertEqual(sparse_search(array, 7), 2)
    self.assertEqual(sparse_search(array, 19), 8)
    self.assertEqual(sparse_search(array, 37), 13)
    self.assertEqual(sparse_search(array, 40), 14)
    array = [0, 12, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.assertEqual(sparse_search(array, 12), 1)
    self.assertEqual(sparse_search(array, 18), 3)

if __name__ == "__main__":
  unittest.main()