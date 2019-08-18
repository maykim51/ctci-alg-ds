'''
CTCI 4.6.successor: 
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. 
You may assume that each node has a link to its parent. 

SOLUTION
원래 in-order를 내가 root일때를 기준으로 생각한다. 그러고나서 예외를 생각한다. 
1. R subtree의 왼쪽노드,
2. R이 없다면? -> parent를 따라서..
'''

# Return the successor of a node in a binary search tree.

def successor(node):
  if not node:
    return None

# normal in-order : return left most child of right subtree
  child = node.right
  if child:
    while child.left:
      child = child.left
  if child:
    return child

    #else find first parent that is left child of its won parent
    ''' 이상하지만 fix it later''' 
  if node.parent and node.parent.data > node.data:
    return node.parent
  return None

class Node():
  def __init__(self, data, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.parent = None
    if self.left:  self.left.parent  = self
    if self.right: self.right.parent = self

import unittest

class Test(unittest.TestCase):
  def test_successor(self):
    self.assertEqual(successor(Node(22, Node(11))), None)
    self.assertEqual(successor(Node(22, Node(11), Node(33))).data, 33)
    self.assertEqual(successor(Node(22, Node(11), Node(33, Node(28)))).data, 28)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).left).data, 22)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)

if __name__ == "__main__":
  unittest.main()

