'''
___?? 다시 돌아와서 이해하기
CTCI 4.12 Paths with Sum: 

You are given a binary tree in which each node contains an integer value (which might be positive or negative). 
Design an algorithm to count the number of paths that sum to a given value. 
The path does not need to start or end at the root or a leaf, but it must go downwards 
(traveling only from parent nodes to child nodes). 

SOLUTIONS
1) traverse and count (brute force)
2) hashtable (O(N))
'''


# Return all downward paths through a tree whose nodes sum to a target value.

def paths_with_sum(binary_tree, target_sum):
  partial_paths = ListDict({target_sum: [[]]})
  return paths_with_partial_sum(binary_tree, target_sum, partial_paths)
  
def paths_with_partial_sum(node, target_sum, partial_paths):
  if not node:
    return []
  next_partial_paths = ListDict({target_sum: [[]]})
  for path_sum, paths in partial_paths.items():
    for path in paths:
      next_partial_paths[path_sum - node.value] += [path + [node.name]]
  paths = next_partial_paths[0]
  for child in [node.left, node.right]:
    paths += paths_with_partial_sum(child, target_sum, next_partial_paths)
  return paths

class Node():
  def __init__(self, name, value, left=None, right=None):
    self.name, self.value, self.left, self.right = name, value, left, right

class ListDict(dict):
    #dict에 키가 없는 경우
  def __missing__(self, key):
    return []

import unittest

class Test(unittest.TestCase):
  def test_paths_with_sum(self):
    bt=Node("A",4,Node("B",-2,Node("D",7),Node("E", 4)),
                  Node("C", 7,Node("F",-1,Node("H",-1),Node("I",2,Node("K",1))),
                              Node("G", 0,None,        Node("J", -2))))
    self.assertEqual(paths_with_sum(bt, 12), [["A", "C", "F", "I"]])
    self.assertEqual(paths_with_sum(bt, 2), [["A", "B"], ["B", "E"], ["I"],
        ["F", "I", "K"]])
    self.assertEqual(paths_with_sum(bt, 9), [["A","B","D"], ["A","C","F","H"],
        ["C","F","I","K"], ["A","C","G","J"]])

if __name__ == "__main__":
  unittest.main()
