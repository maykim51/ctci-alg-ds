'''
CTCI 16.1 Number Swapper: 

Write a function to swap a number in place (that is, without temporary variables). 
SOLUTION
차이를 저장해놨다가, 한쪽이 옮기고 나면 그 차이 값을 이용하기.
'''

def swap(a, b):
    #image b < a
    a = a-b #a = diff (imagine a> b)
    b = b + a # b + diff = a
    a = b - a #new b - diff
    
    return a, b
    
