'''
CTCTI 4.2. Minimal Tree:

Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.

'''
'''
Minimal heights = 꽉채워서?

BST Soltuion: 루트의 상황으로 생각!!! 무조건!! sub tree개념으로.
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None
    
    def __str__(self):
        print(self.data)

class BST():
    def __init__(self, root: Node):
        self.root = root
    
    def insert(self, data):
        node = Node(data)
        
        if self.root is None:
            self.root = node
            return
        if data == self.root.data:
            print('invalid input! dup!')
            return
        
        if data < self.root.data and self.root.left is None:
            self.root.left = node
        elif data < self.root.data:
            BST(self.root.left).insert(data)
        elif data > self.root.data and self.root.right is None:
            self.root.right = node
        elif data > self.root.data:
            BST(self.root.right).insert(data)
        
        return

        
if __name__ == "__main__":     
    n1 = Node(9)
    bst = BST(n1)
    bst.insert(7)
    bst.insert(5)           
    print(bst)        

# def minialTree(arr, tree = []):
#     if tree = []:
        
    
#     root = arr[len(arr)//2]
    
    
    
