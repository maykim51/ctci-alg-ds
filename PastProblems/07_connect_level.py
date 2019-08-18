'''
Frequently asked 07
https://www.geeksforgeeks.org/microsofts-asked-interview-questions/
https://www.geeksforgeeks.org/connect-nodes-at-same-level/

Connect nodes at same level.
Write a function to connect all the adjacent nodes at the same level in a binary tree. 
Structure of the given Binary Tree node is like following.

struct node{ 
  int data; 
  struct node* left; 
  struct node* right; 
  struct node* nextRight;   
} 

Initially, all the nextRight pointers point to garbage values. 
Your function should set these pointers to point next right for each node.
Input Tree
       A
      / \
     B   C
    / \   \
   D   E   F


Output Tree
       A--->NULL
      / \
     B-->C-->NULL
    / \   \
   D-->E-->F-->NULL


SOLUTION
bfs traverse? 
or pre-order (below)
'''
##PREORDER WAY  
class newnode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = self.nextRight = None
		
# Sets the nextRight of root and calls 
# connectRecur() for other nodes 
def connect (p): 
	p.nextRight = None
	connectRecur(p) 

# Set next right of all descendents of p. 
# Assumption: p is a compete binary tree 
def connectRecur(p): 
	if (not p): 
		return

	if (p.left): 
		p.left.nextRight = p.right 
	
	if (p.right): 
		if p.nextRight: 
			p.right.nextRight = p.nextRight.left 
		else: 
			p.right.nextRight = None
	
	# Set nextRight for other nodes in 
	# pre order fashion 
	connectRecur(p.left) 
	connectRecur(p.right) 

# Driver Code 
if __name__ == '__main__': 

	# Constructed binary tree is 
	#		 10 
	#	 / \ 
	#	 8	 2 
	# / 
	# 3 
	root = newnode(10) 
	root.left	 = newnode(8) 
	root.right	 = newnode(2) 
	root.left.left = newnode(3) 

	# Populates nextRight pointer in all nodes 
	connect(root) 

	# Let us check the values of nextRight pointers 
	print("Following are populated nextRight", 
		"pointers in the tree (-1 is printed", 
					"if there is no nextRight)") 
	print("nextRight of", root.data, "is ", end = "") 
	if root.nextRight: 
		print(root.nextRight.data) 
	else: 
		print(-1) 
	print("nextRight of", root.left.data, "is ", end = "") 
	if root.left.nextRight: 
		print(root.left.nextRight.data) 
	else: 
		print(-1) 
	print("nextRight of", root.right.data, "is ", end = "") 
	if root.right.nextRight: 
		print(root.right.nextRight.data) 
	else: 
		print(-1) 
	print("nextRight of", root.left.left.data, "is ", end = "") 
	if root.left.left.nextRight: 
		print(root.left.left.nextRight.data) 
	else: 
		print(-1) 
