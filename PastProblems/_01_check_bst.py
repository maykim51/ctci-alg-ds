'''
MS Past Q. Frequently asked.


Check if a Binary Tree is BST or not 
https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
https://practice.geeksforgeeks.org/problems/check-for-bst/1

'''
'''
= CTCI 4.5 
'''


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