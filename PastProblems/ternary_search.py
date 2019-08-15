'''
[MS Intern]
You're given an array of length n, the elements in the array keeps on increasing till a action point(x) 
and after that it's start decreasing, you've to find the maximum value(that is the action point value). 

I solved it using ternary search.

SOLUTION
use ternary search!

'''
import unittest

def ternary_search(arr, left=0, right=None):
    if arr == []:
        return -1
    if right==None:
        right = len(arr)-1 #2
        
    mid1 = left + (right-left)//3  # 0 + (2-0)//3 = 0
    mid2 = right - (right-left)//3 # 2 - (2-0)//3 = 2
    if mid1 > mid2:
        return -1
    
    ### check it!!
    if mid1 == left:
        mid1 += 1
    if mid2 == right:
        mid2 -= 1
        
    if arr[mid1] > arr[mid1-1] and arr[mid1] > arr[mid1+1]: 
        return mid1
    elif arr[mid2] > arr[mid2-1] and arr[mid2] > arr[mid2+1]:
        return mid2
    
    up_down = [-1, -1, -1] #? down down...
    if arr[left] < arr[mid1]: up_down[0] = 1
    else: up_down[0] = 0
    if arr[mid1] < arr[mid2]: up_down[1] = 1
    else: up_down[1] = 0
    if arr[mid2] < arr[right]: up_down[2] = 1
    else: up_down[2] = 0
    
    if up_down[0]==1 and up_down[2]==0:
        return ternary_search(arr, mid1, mid2)
    if up_down[1]==0 and up_down[2]==0:
        return ternary_search(arr, left, mid1)
    if up_down[0]==1 and up_down[1]==1:
        return ternary_search(arr, mid2, right)
    else: 
        print('something is wrong.')
        return -1
    
    return -1    

class Test(unittest.TestCase):
    def test_ternary_search(self):
        arr1 = [5,6,7,8,16,8,4,2]
        self.assertEqual(ternary_search(arr1), 4)
        arr2 = [1,5,4]
        self.assertEqual(ternary_search(arr2), 1)
        arr3 = [5,6,7,8,16,20,24,50,8,4,2]
        self.assertEqual(ternary_search(arr3), 7)

if __name__ == "__main__":
    unittest.main()