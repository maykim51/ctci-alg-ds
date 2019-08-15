'''
CTCI 8.3. Magic Index: 

A magic index in an array A [ 0 ... n -1] is defined to be an index such that A[i] = i. 
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A. 

FOLLOW UP 
What if the values are not distinct?

SOLUTION
twicked bst

'''
import unittest

#dup 이 있다고 가정
def magic_index(array, start = 0, end = None):
    if end is None:
        end = len(array)-1
    if start > end: 
        return -1
    
    mid = (start + end) // 2
    print(start)
    print(end, mid)
    if array[mid] == mid:
        return mid
    
    left = magic_index(array, start, min(array[mid], mid-1))
    if left >= 0 :
        return left
    
    right =  magic_index(array, max(array[mid], mid+1), end)
    return right
        

class Test(unittest.TestCase):
    # def test_magic_index_distinct(self):
    # #   self.assertEqual(magic_index_distinct([3,4,5]), None)
    # #   self.assertEqual(magic_index_distinct([-2,-1,0,2]), None)
    # #   self.assertEqual(magic_index_distinct([-20,0,1,2,3,4,5,6,20]), None)
    # #   self.assertEqual(magic_index_distinct([-20,0,1,2,3,4,5,7,20]), 7)
    #   self.assertEqual(magic_index([-20,1,2,3,4,5,6,20]), 4)
    
    def test_magic_index(self):
      self.assertEqual(magic_index([3,4,5]), -1)
      self.assertEqual(magic_index([-2,-1,0,2]), -1)
      self.assertEqual(magic_index([-20,0,1,2,3,4,5,6,20]), -1)
      self.assertEqual(magic_index([-20,0,1,2,3,4,5,7,20]), 7)
      self.assertEqual(magic_index([-20,1,2,3,4,5,6,20]), 3)
      self.assertEqual(magic_index([-20,5,5,5,5,5,6,20]), 6)
  
if __name__ == "__main__":
    unittest.main() 