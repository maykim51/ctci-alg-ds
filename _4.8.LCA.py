'''
MS past question
CTCI 4.4 First Common Ancestor:  (=LCA)

Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
Avoid storing additional nodes in a data structure. 
NOTE: This is not necessarily a binary search tree. 

https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
'''
'''
SOLUTION
1. parent link가 있으면
1-1. 둘다 search해서 올라가면서 서로의 ancestor안에 자기가 있나확인
1-2. 하나만 올라가면서 parent 노드의 sibling 확인
2. parent link가 없으면 루트에서 시작해서 좌우 위치를 상대적으로 비교. (둘다 left or right, 각각 left and right)
'''
import unittest
###Option 1 - iterate parents
# class Node():
#     def __init__(self, data=None, left=None, right=None):
#       self.data, self.left, self.right = data, left, right
#       self.parent = None
#       if self.left:
#         self.left.parent = self
#       if self.right:
#         self.right.parent = self
        
      
# def first_common_ancestor(root=None, node1, node2):
#   search1, search2 = node1, node2
#   ancestors1, ancestors2 = {}, {}
#   while search1 or search2:
#     if search1:
#       if search1 in ancestors2:
#         return search1
#       ancestors1[search1] = True
#       search1 = search1.parent
#     if search2:
#       if search2 in ancestors1:
#         return search2
#       ancestors2[search2] = True
#       search2 = search2.parent
#   print('ancestor1: {}'.format(ancestors1.keys()))
#   print('ancestor2: {}'.format(ancestors2.keys()))
#   return None

## Option 2 use parents


class Node:
  def __init__(self, data=None, left=None, right=None):
      self.value = data
      self.left = left
      self.right = right

#visited [T,F]
def findLCAUtil(root, n1, n2, v):
  
  # Base Case
  if root is None:
      return None

  if root.value == n1.value:
      v[0] = True
      return root

  if root.value == n2.value:
      v[1] = True
      return root

  left_lca = findLCAUtil(root.left, n1, n2, v)
  right_lca = findLCAUtil(root.right, n1, n2, v)

  if left_lca and right_lca:#둘다 있으면
    return root

  # 둘 중에 뭐라도 있는 쪽을 다시 본다는 거.
  return left_lca if left_lca is not None else right_lca


def covers(root, k):
  # Base Case
  if root is None:
    return False

  if (root.value == k.value or covers(root.left, k) or covers(root.right, k)):
    return True

  return False


def first_common_ancestor(root, n1, n2):
  v = [False, False]
  if (not covers(root, n1)) or (not covers(root, n2)):
      return None
  lca = findLCAUtil(root, n1, n2, v)
  return lca


# test

class Test(unittest.TestCase):
  def test_first_common_ancestor(self):
    node1 = Node(11, Node(55), Node(77, Node(44)))
    node2 = Node(22, Node(99))
    node3 = Node(33, node1, Node(88, Node(123, None, node2)))
    node4 = Node(44, node3, Node(66))
    # self.assertEqual(first_common_ancestor(None, node1, node2), None)    
    self.assertEqual(first_common_ancestor(node3, node1, node2), node3)

if __name__ == "__main__":
  unittest.main()