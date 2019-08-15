'''
CTCTI 4.5. Validate BST:

Implement a function to check if a binary tree is a binary search tree.
'''
'''
###conditions of bst
## 1. in order traversal
## 2. left <= root < right

#recursively?
'''




import unittest
class Node():
  def __init__(self, data, left=None, right=None):
    self.data, self.left, self.right = data, left, right


# ### Option 1. In-order travel (- dup이 있으면 판별 불가)
# def is_sorted(queue):
#     if len(queue) <= 1:
#           return True

#     for i in range(1, len(queue)):
#           if queue[i-1] > queue[i]:
#                 return False
#     return True


# def validate_tree(tree):
#   queue = []
#   result = copy_tree(tree, queue)

#   if is_sorted(result):
#     return True
#   else:
#     return False


# def copy_tree(tree, q):  # in-order
#   #base case
#   if not tree:
#     return
#   queue = q
#   #TODO - initiate & recurse
#   copy_tree(tree.left, queue)
#   queue.append(tree.data)
#   copy_tree(tree.right, queue)

  # return queue

### Option 2 . 배열 사용 안 하고 global last_printed 를 사용 in-order
last_printed = None


# def validate_tree(tree):
#   global last_printed
  
#   if not tree:
#     return True

#   #recurse left
#   if not validate_tree(tree.left):
#     return False

#   # 해야하는 일 본업
#   if (last_printed != None) and (tree.data <= last_printed) :
#     return False
#   last_printed = tree.data

#   #recurse right
#   if not validate_tree(tree.right):
#     return False
  
#   return True  # 검사 통과!


# ## (BEST) Option 3 - min, max 를 사용하는 방법
def validate_tree(root, min=None, max=None):
      #base case: how to terminate recursion?
      if root is None:
            return True
      
      if (min != None and root.data < min) or (max != None and root.data > max):
            return False
        
      if (not validate_tree(root.left, min, root.data)) or (not validate_tree(root.right, root.data, max)):
            return False
      
      return True


class Test(unittest.TestCase):
  def test_validate_tree(self):
    global last_printed
    self.assertEqual(validate_tree(Node(3, Node(1), Node(8))), True)
    last_printed = None
    tree1 = Node(5, Node(3, Node(1), Node(4)), Node(
        7, Node(6), Node(8, None, Node(9))))
    self.assertEqual(validate_tree(tree1), True)
    last_printed = None
    tree2 = Node(7, Node(3, Node(1), Node(8)), Node(9, Node(8), Node(11)))
    self.assertEqual(validate_tree(tree2), False)
    last_printed = None
    tree3 = Node(20, Node(20, None, Node(25)), Node(30))
    self.assertEqual(validate_tree(tree3), False)
    last_printed = None


if __name__ == "__main__":
  unittest.main()
