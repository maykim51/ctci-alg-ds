'''
CTCTI 4.3. List of Depths: 

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
(e.g., if you have a tree with depth D, you'll have D linked lists). 
'''
'''

'''
from mybst import BST, Node

def depthList(tree):
    # if tree.root is None:
    #     return
    
    queue = [tree.root, 's']
    dl = [[]]
    curr = queue.pop(0)
    while queue:
        if curr == 's':
            dl.append([])
            queue.append('s')
            curr = queue.pop(0)
            continue       
        else:
            dl[-1].append(curr.data)
            
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    
        curr = queue.pop(0)
    
    return dl


if __name__ == "__main__":     
    n1 = Node(6)
    bst = BST(n1)
    bst.insert(4)
    bst.insert(2)    
    bst.insert(5)
    bst.insert(10)
    bst.insert(9)
    bst.insert(12) 
    
    print(depthList(bst))