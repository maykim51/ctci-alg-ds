'''
****************!!!!******
[MS SDE]

Implement a calculator with +, * (, and ).
https://leetcode.com/problems/basic-calculator-iii

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) 
and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. 
All intermediate results will be in the range of [-2147483648, 2147483647].

SOLUTION
https://www.geeksforgeeks.org/make-simple-calculator-using-python/

'''
import unittest
class Solution(object):
    # def calculate(self, s):
    #     def update(op, num):
    #         if op == '+':
    #             stack.append(int(num))
    #         elif op == '-':
    #             stack.append(int(-num))
    #         elif op == '*':
    #             stack.append(int(stack.pop()*num))
    #         elif op == '/':
    #             stack.append(int(stack.pop()/num))
    #         print(stack)
                
    #     num, op = 0, '+'
    #     stack = []
        
    #     for i in range(len(s)):
    #         if s[i].isdigit():
    #             num += num*10 + int(s[i])
    #         elif s[i] in ['+', '-', '*', '/', ')']:
    #             stack.append(num)
    #             if s[i] == ')':
    #                 while isinstance(stack[-1], int):
    #                     num += stack.pop()
    #                 op = stack.pop()
    #                 update(op, num)
    #             num, op = 0, s[i]
    #         elif s[i] == '(':
    #             stack.append(op)
    #             num, op = 0, '+'
        
    #     update(op, num)
    #     _sum = 0
    #     print(stack)
    #     for n in stack:
    #         if type(num) == int:
    #             _sum+= n
    #     return _sum

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def update(op, num):
            if op == '+':
                stack.append(int(num))
            elif op == '-':
                stack.append(int(-num))
            elif op == '*':
                stack.append(int(stack.pop() * num))
            elif op == '/':
                stack.append(int(stack.pop() / num))
        
        stack = []
        num, op = 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in ['+', '-', '*', '/', ')']:
                update(op, num)
                if s[i] == ')':
                    num = 0
                    while isinstance(stack[-1], int): ##!!!!!!!!!!
                        num += stack.pop() 
                    op = stack.pop()
                    update(op, num)
                num, op = 0, s[i]
            elif s[i] == '(':
                stack.append(op)
                num, op = 0, '+'
            
        update(op, num)
        print(stack)
        _sum = 0
        for n in stack:
            if type(n) == int:
                _sum+= n
        return _sum
                
            
            

class Test(unittest.TestCase):
    def test_calculate(self):
        sol = Solution()
        self.assertEqual(sol.calculate("1+1"), 2)
        self.assertEqual(sol.calculate(" 6-4 / 2 "), 4)
        self.assertEqual(sol.calculate("2*(5+5*2)/3+(6/2+8)"), 21)

if __name__ == "__main__":
    unittest.main()

    
                             