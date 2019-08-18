class Node():
    def __init__(self, value):
        self.value = value
        self. left, self.right = None, None
        
    def __str__(self):
        return str(self.value)
       

class Tree(): #binary tree
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return 
        queue = []  
        queue.append(self.root)
        
 
        # not bst, just binary -> level traverse
        while queue != []:  
            node = queue[0]  
            queue.pop(0)  
    
            if (not node.left): 
                node.left = Node(value)  
                return 
            else: 
                queue.append(node.left)  
    
            if (not node.right): 
                node.right = Node(value) 
                return
            else: 
                queue.append(node.right) 
                   
    
    def print_tree(self, node=None):
        if node is None:
            node = self.root
        print('{', end="")
        if node.left:            
            self.print_tree(node.left)
        print('{', end="")
        print(node, end="")
        print('}', end="")
        if node.right:            
            self.print_tree(node.right)
        print('}', end="")


#Driver
if __name__ == "__main__":
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(15)
    n4 = Node(6)
    n5 = Node(8)
    t = Tree()
    t.insert(n1)
    t.insert(n2)
    t.insert(n3)
    t.insert(n4)
    t.insert(n5)
    t.print_tree()

            
        

        