'''
CTCI 3.5. Sort Stack: 

Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements into any other data structure 
(such as an array). 

The stack supports the following operations: push, pop, peek, and is Empty. 
'''
import unittest

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack == [] or self.stack == None
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        res = ''
        for x in self.stack:
            res += str(x)
            if x != self.size()-1:
                res += ','
        return res

def sort_stack(s):
    if s.isEmpty():
        return 'None'
    
    temp_stack = Stack()
    while not s.isEmpty():
        data = s.pop()
        
        while (not temp_stack.isEmpty()) and data < temp_stack.peek():
            s.push(temp_stack.pop())
        temp_stack.push(data)
        
    while not temp_stack.isEmpty():
        s.push(temp_stack.pop())
    
    return s.stack


class Test(unittest.TestCase):
    def test_sort_stack(self):
      self.assertEqual(str(sort_stack(Stack())), "None")
      stack = Stack()
      stack.push(10)
      stack.push(30)
      stack.push(70)
      stack.push(40)
      stack.push(80)
      stack.push(20)
      stack.push(90)
      stack.push(50)
      stack.push(60)
      self.assertEqual(str(sort_stack(stack)), '[90, 80, 70, 60, 50, 40, 30, 20, 10]')
  
if __name__ == "__main__":
    unittest.main()
  