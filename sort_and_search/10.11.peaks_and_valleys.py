'''
CTCI 10.11. Peaks and Valleys: 
In an array of integers, a "peak" is an element which is greater than or equal to the adjacent integers 
and a "valley" is an element which is less than or equal to the adjacent integers. 
For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. 

Given an array of integers, sort the array into an alternating sequence of peaks and valleys. 

EXAMPLE 
Input: {5, 3, 1, 2, 3} 
Output: {5, 1, 3, 2, 3}

'''
import unittest

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return

def maxix(array, a, b, c):
    mx = max(array[a], array[b], array[c])
    if array[a] == mx : return a
    if array[b] == mx : return b
    if array[c] == mx : return c

def peak_valley(array):
    if len(array) < 3 :
        return None
    
    for i in range(1, len(array), 2): ##!!!!!usage of range
        biggestix = maxix(array, i-1, i, i+1)
        if i != biggestix:
            swap(array, i, biggestix)
        
    return array

class Test(unittest.TestCase):
    def test_peak_valley(self):
        array = [5,3,1,2,3]
        self.assertEqual(peak_valley(array), [3,5,1,3,2])
    
if __name__ == "__main__":
    unittest.main()