'''
CTCI 4.10. Check Subtree: 

Tl and T2 are two very large binary trees, with Tl much bigger than T2. 
Create an algorithm to determine if T2 is a subtree of Tl. A tree T2 is a subtree of Tl 
if there exists a node n in Tl such that the subtree of n is identical to T2. 
That is, if you cut off the tree at node n, the two trees would be identical. 

SOLUTION
Tree cmp, mirror -> PRE-ORDER + NULL!! 

'''

class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def traverse_preorder(t):
    curr = t
    queue = [curr]
    res = []
    while queue:
        node = queue.pop(0)
        if node == 'None':
            res.append('None')
            continue
        res.append(node.data)
        if node.left:
            queue.append(node.left)
        else:
            queue.append('None')
        if node.right:
            queue.append(node.right)
        else:
            queue.append('None')
    return res
    
    

def is_subtree(t1, t2):
    #preorder traverse t1, t2 with null
    l1 = traverse_preorder(t1)
    l2=  traverse_preorder(t2)
    print(l1)
    print(l2)
    
    for i in range(len(l1)):
        if l1[i] == l2[0]:
            if l1[i:len(l2)] == l2:
                return True
    return False
    

#Driver
import unittest
class Test(unittest.TestCase):
  def test_is_subtree(self):
    tree1 = Node(5,Node(3,Node(2),Node(4)),Node(8,Node(7,Node(9)),Node(1)))
    tree2 = Node(8,Node(7),Node(1))
    self.assertEqual(is_subtree(tree1, tree2), False)
    tree3 = Node(8,Node(7,Node(9)),Node(1))
    self.assertEqual(is_subtree(tree1, tree3), True)

if __name__ == "__main__":
  unittest.main()