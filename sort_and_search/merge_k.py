'''
!!!!!!!!!!!
part of CTCI 10.6 Big file.
[merge k sorted arrays, external sort 중 앞에꺼]
'''
import unittest

class heapNode: #heap as in ARRAY
    def __init__(self, val, i=0, j=0): # i: ix of parent array, j: ix of next var in parent array
        self.val = val
        self.i, self.j = i, j        
        

class minHeap:
    def __init__(self, arr):
        self.heap_arr = arr
        self.size = len(self.heap_arr)
        i = (len(arr)-1) //2 
        while i >= 0:
            self.heapify(i)
            i -= 1
    
    
    def heapify(self, i):
        left_ix = 2*i + 1
        right_ix = 2*i +2
        if left_ix < self.size and self.heap_arr[left_ix].val < self.heap_arr[i].val:
            self.replace(left_ix, i)
            self.heapify(left_ix)
        if right_ix < self.size and self.heap_arr[right_ix].val < self.heap_arr[i].val:
            self.replace(right_ix, i)
            self.heapify(right_ix)
            
    
    def replace(self, i, j):
        temp = self.heap_arr[i]
        self.heap_arr[i] = self.heap_arr[j]
        self.heap_arr[j] = temp
    
    def peek_min(self):
        if self.size < 1:
            return None
        else:
            return self.heap_arr[0]
    
    def replace_root(self, root):
        self.heap_arr[0] = root
        self.heapify(0)
    
        
         

def merge_k_sorted_arrays(arrays):
    #create minheap with first variables with arrs
    k = len(arrays)
    heap_arr = []
    result_size = 0
    for i in range(len(arrays)):
        node = heapNode(arrays[i][0], i, 1)
        heap_arr.append(node)
        result_size += len(arrays[i])
    
    min_heap = minHeap(heap_arr)  
    
    #traverse minheap and save min value from the minheap
    #replace min with next var from its original array, if next is None, replace it with float('inf')
    result = [0]*result_size
    ##FIX IT
    for x in range(result_size):        
        min = min_heap.peek_min()
        result[x]= min.val
        if min.j < len(arrays[min.i]):
            min.val = arrays[min.i][min.j]
            min.j += 1
        else:
            min.val = float("inf")
        min_heap.replace_root(min)
    
    #return the list of result 
    return result  
    

class Test(unittest.TestCase):
    def test_merge_k_sorted_arrays(self):
        arrays1 = [
            [2, 6, 12, 34],
            [1, 9, 20, 1000],
            [23, 34, 90, 2000]
        ]
        self.assertEqual(merge_k_sorted_arrays(arrays1), [1, 2, 6, 9, 12, 20, 23, 34, 34, 90, 1000, 2000])
    
if __name__ == '__main__':
    unittest.main()