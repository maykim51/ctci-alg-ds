'''
CTCI 3.1. Stack Min: 

How would you design a stack which, in addition to push and pop, has a function min 
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

'''
'''
solution: keep a min stack within the stack class!!!!!!!!
'''



class MinStack:
    def __init__(self):
        self.data = []          
        self.minData  = []      ###!!!!!!!!! Store the minimum element so far


    def push(self, x):
        self.data.append(x)
        if len(self.minData) == 0 or x <= self.minData[-1]:
            self.minData.append(x)


    def pop(self):
        if len(self.data) == 0:
            return None
        else:
            if self.data[-1] == self.minData[-1]:   self.minData.pop()
            return self.data.pop()


    def top(self):
        if len(self.data) == 0: return None             
        else:                   return self.data[-1]


    def getMin(self):
        if len(self.minData) == 0:  return None         
        else:                       return self.minData[-1]