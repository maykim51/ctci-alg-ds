'''
CTCI 16.1. Number Swapper: 
Write a function to swap a number in place (that is, without temporary variables). 
'''
n1 = 10
n2 = 15
def num_swap(n1, n2):
    n1 = n1 - n2 #diff = 
    n2 = n2 + n1 #n2 + diff = n1
    n1 = n2 - n1 #new n2, n1 - diff
    print(n1, n2)

num_swap(n1, n2)