'''
CTCI 4.9. BST Sequences: 

A binary search tree was created by traversing through an array from left to right and inserting each element. 

Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree. 

EXAMPLE 
Input: {1,{2},3} TREE
Output: {2, 1, 3}, {2, 3, 1} 

SOLUTION
weave...

https://gist.github.com/kean/40a1e592a608154b117a0dac48baf25f
https://hackernoon.com/bst-sequences-in-python-c072c0e9b19f
'''
import copy

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:            
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def insert(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._insert(val, self.root)
    
    def _insert(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._insert(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._insert(val, node.r)
            else:
                node.r = Node(val)
              
# 'first' list shall be referred to as first[]
# 'second' list shall be referred to as second[]
# 'prefix' list shall be referred to as prefix[]
def weaveLists(first, second, results, prefix):
    # if first or second is an empty list
    if not first or not second:
        # ensuring that result is a CLONE and not a reference to prefix
        result = copy.deepcopy(prefix)
        
        # add result to first or/ and second lists
        if first:
            result += first
        if second:
            result += second
        # append the weaved list which is result, to results
        results.append(result)
        return        # add result to first or/ and second lists
        if first:
            result += first
        if second:
            result += second
        # append the weaved list which is result, to results
        results.append(result)
        return    # this would be the method as described in the textbook
    # first, remove and store first element of first[]
    headFirst = first.pop(0)
    # append to prefix
    prefix.append(headFirst)
    ### add recursive call to operate on first[]
    weaveLists(first, second, results, prefix) 
    # exit when first[] is empty    # reset prefix for second recursive call below by removing last element
    # IMPT to modify in-place
    del prefix[-1] 
    # reset first[] for second recursive call below by adding back first element
    # IMPT to modify in-place
    first.insert(0,headFirst)    # do the same thing on the second[]
    headSecond = second.pop(0)
    prefix.append(headSecond)
    ### add recursive call to operate on first[] and second[]
    weaveLists(first, second, results, prefix)
    del prefix[-1]
    second.insert(0,headSecond)