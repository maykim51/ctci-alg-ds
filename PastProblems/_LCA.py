'''
Given Binary tree with parent pointer and two nodes. Find LCA of the given two nodes in a given binary tree
filter_none
brightness_4
struct TreeNode 
{ 
int data; 
TreeNode *left,*right,*parent; 
}; 

https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
'''
""" Program to find LCA of n1 and n2 using one traversal of 
 Binary tree 
It handles all cases even when n1 or n2 is not there in tree 
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#visited [T,F]
def findLCAUtil(root, n1, n2, v):
    # Base Case
    if root is None:
        return None

    if root.value == n1:
        v[0] = True
        return root

    if root.value == n2:
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

    if (root.value == k or covers(root.left, k) or
            covers(root.right, k)):
        return True

    return False


def findLCA(root, n1, n2):
    v = [False, False]
    if not covers(root, n1) or not covers(root, n2):
        return None

    lca = findLCAUtil(root, n1, n2, v)

    # Returns LCA only if both n1 and n2 are present in tree
    if (v[0] and v[1] or v[0] and covers(lca, n2) or v[1] and
            covers(lca, n1)):
        return lca



# # Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# lca = findLCA(root, 4, 5)

# if lca is not None:
#     print("LCA(4, 5) = {}". format(lca.value))
# else:
#     print("values are not present")

# lca = findLCA(root, 4, 10)
# if lca is not None:
#     print("LCA(4,10) = {}".format(lca.value))
# else:
#     print("values are not present")
