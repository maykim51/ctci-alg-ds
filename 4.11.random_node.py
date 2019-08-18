'''
___약간 찜찜
CTCI 4.11. Random Node:

You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, 
has a method getRandomNode() which returns a random node from the tree. 

All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, 
and explain how you would implement the rest of the methods. 

SOLUTION
1) traverse and pick
2) pick level / pick self or left or right, but provide size of subtree to make 확률 1/N
3) Sol # 7... 이해 안됨

'''
from random import randint

class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        # Keep track of size of each side
        self.size = 1
        if self.left:
          self.size += self.left.size
        if self.right:
          self.size += self.right.size
    
    def get_random(self):
        self.helper(randint(0, self.size - 1))
        
    # each subtree's rate must be its size*1/N...
    def helper(self, rand):
        # If rand number is 0, return root
        if rand == 0:
            return self
        
        # If left exists
        if self.left:
            # If rand number is < left_size
            if rand-1 < self.left.size:
                return self.left.helper(rand-1)
            # If rand number is > left_size
            elif self.right:
                return self.right.helper(rand-1-self.left.size)
        
        # If left size is 0, and right exists
        if self.right:
            return self.right.helper(rand-1)
            
        # If no possible result
        return None



import unittest

class Test(unittest.TestCase):
  def test_get_random_value(self):
    tree = Node(11,Node(21,Node(31),Node(32,Node(41),Node(42,None,Node(51)))),
                   Node(22,Node(33),Node(34)))
    self.assertEqual(tree.helper(0).data, 11)
    self.assertEqual(tree.helper(4).data, 41)
    self.assertEqual(tree.helper(8).data, 33)

if __name__ == "__main__":
  unittest.main()