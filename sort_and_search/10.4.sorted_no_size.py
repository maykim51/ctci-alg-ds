'''
CTCI 10.4. Sorted Search, No Size: 

You are given an array-like data structure Listy which lacks a size method. 
It does, however, have an elementAt( i) method that returns the element at index i in 0(1) time. 
If i is beyond the bounds of the data structure, it returns -1. 
(For this reason, the data structure only supports positive integers.) 

Given a 'Listy' which contains sorted, positive integers, find the index at which an element x occurs. 
If x occurs multiple times, you may return any index.
'''

def search_listy(listy, item, leftix=0, rightix=None):
      
  if rightix is None:
    rightix = 1
    right = listy[rightix]
    while right < item and right != -1:
      rightix *= 2
      right = listy[rightix]
    if right == item:
      return rightix
   
  #recursion (BST)  
  if leftix == rightix:
    return None
  middleix = (leftix + rightix) // 2
  middle = listy[middleix]
  if middle == item:
    return middleix
  if middle == -1 or middle > item:
    return search_listy(listy, item, leftix, middleix)
  else:
    return search_listy(listy, item, middleix+1, rightix)



import unittest
class Listy:
  def __init__(self, array):
    self.array = array
  
  def __getitem__(self, ix):
    if ix < len(self.array):
      return self.array[int(ix)]
    else:
      return -1

class Test(unittest.TestCase):
  def test_search_listy(self):
    listy = Listy([-22, -11, 11, 22, 33, 44, 55, 66, 77, 88, 99])
    self.assertEqual(search_listy(listy, 25), None)
    self.assertEqual(search_listy(listy, -22), 0)
    self.assertEqual(search_listy(listy, 22), 3)
    self.assertEqual(search_listy(listy, 66), 7)
    self.assertEqual(search_listy(listy, 77), 8)
    self.assertEqual(search_listy(listy, 99), 10)
    self.assertEqual(search_listy(listy, 100), None)

if __name__ == "__main__":
  unittest.main()