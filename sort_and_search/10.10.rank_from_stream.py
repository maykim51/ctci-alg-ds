'''
CTCI 10.10. Rank from Stream: 

Imagine you are reading in a stream of integers. 
Periodically, you wish to be able to lookup the rank of a numberx (the number of values less than or equal to x). 

lmplementthe data structures and algorithms to support these operations. That is, 
implement the method 'track( int x)', which is called when each number is generated, 
and the method 'getRankOfNumber(int x)', which returns the number of values less than or equal to x 
(not including x itself). 

EXAMPLE 
Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3 
getRankOfNumber(l) 0 
getRankOfNumber(3) = 1 
getRankOfNumber(4) 3 

SOLUTION
BST, that root keeps track of number of nodes in left subtree.
careful with handling null situation (if node not in the tree, return -1)

'''

#root node of tree
root = None

def track(data):
    global root
    if root is None:
        root = RankNode(data)
    else:
        root.insert(RankNode(data))
        

class RankNode:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None
        self.left_size = 0
    
    
    def insert(self, node):
        if node.data <= self.data:
            self.left_size += 1
            if self.left is None: self.left = node
            else: return self.left.insert(node)            
        elif self.right is None: self.right = node
        else: return self.right.insert(node)
        
    def __str__(self):
        return '{'+ 'L: {}, V:{}, R:{}'.format(self.left, self.data, self.right) + '}'
    
    def get_rank(self, data):
        if data == self.data:
            return self.left_size
        elif data < self.data:
            if self.left:
                return self.left.get_rank(data)
            else: return -1
        elif data > self.data:
            if self.right:
                right_rank  =  self.right.get_rank(data)
                if right_rank == -1: return -1
                else: return self.left_size + 1 + right_rank
            else: return -1
        

track(11)
track(30)
track(7)
track(7)
track(10)
track(15)
track(7)
track(3)
track(22)

print(root.left_size)
print(root.get_rank(22))
print(root.get_rank(11))
print(root.get_rank(8))
print(root.get_rank(15))
