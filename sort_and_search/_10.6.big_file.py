'''
CTCI 10.6 Big File Sort
Imagine you have a 20 GB file with one string per line. 
Explain how you would sort the file. 

SOLUTION
External Sort
Algorithms: External sort (includes merge sort, merge k sorted arrays)

https://www.geeksforgeeks.org/external-sorting/
'''
'''
SOLUTION: 내가 썼네..
천천히 해서 그렇지 할 수 있기는 하네~~
'''
from merge_k import minHeap, heapNode
from random import randrange
import math

#merge k files
def mergeFiles(output_fileName, run_size, num_ways):
    files = [None]*num_ways
    for i in range(num_ways):
        files[i] = open(str(i)+".txt", 'r')    
    ###FIX THE FILE NAME LATER
    fileOut = open("output.txt", 'w')
    
    heap_arr = []
    for i in range(num_ways):
      node = heapNode(int(files[i].readline().strip()), i, 1)
      heap_arr.append(node)

    min_heap = minHeap(heap_arr)  
    
    ''''''
    #traverse minheap and save min value from the minheap
    #replace min with next var from its original array, if next is None, replace it with float('inf')

    ##FIX IT
    for x in range(run_size*num_ways):        
      min = min_heap.peek_min()
      fileOut.write(str(min.val)+'\n')
      # result[x]= min.val
      if min.j < run_size:
            min.val = int(files[min.i].readline())
            min.j += 1
      else:
            min.val = float("inf")
      min_heap.replace_root(min)
    ''''''
    
    '''#testing print'''
    for x in heap_arr:
      print(x.val)
    
    
    fileOut.close()
    for file in files:
        file.close()
    pass

def merge(arr, left, mid, right):
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = left     # Initial index of merged subarray 
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
            
    while i < len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    
    while j < len(R) :
        arr[k] = R[j]
        j+=1
        k+=1


def mergeSort(arr, left, right):
    mid = 0
    
    if left < right:
        mid = math.floor(left + (right - left) / 2)
    
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        
        merge(arr, left, mid, right)


# divide input, sort, and store in separate files 
def createInitialRuns(input_fileName, run_size: int, num_ways: int):
    fileIn = open(input_fileName, 'r')
    
    #prep output files
    output_files = [None]*num_ways
    for i in range(num_ways):
        fileName = str(i)+".txt"
        output_files[i] = open(fileName, 'w')
    
    #dynamic array
    # arr = 한번 run 할때 쓰는 array
    arr = []
    
    ##???
    more_input = True
    next_output_file = 0
    
    
    while more_input: 
        #write run_size elements into arr from input file
        for i in range(run_size):
            line = fileIn.readline()
            if not line: ##file내용이 runsize 보다 작을 수 있으므로. (e.x. 마지막 파일)
                more_input = False
                break
            else: 
                arr.append(line)
        
        #sort the input
        mergeSort(arr, 0, len(arr)-1)
        print(arr)

        for j in range(len(arr)):
            output_files[next_output_file].write(str(arr[j]))
        
        arr = []    
        next_output_file += 1
    
    for file in output_files:
        file.close()
    
    fileIn.close()
        


    
    
    
    
    fileIn.close()
    pass


def externalSort(input_file, output_file, num_ways, run_size):
    #read inputfile, create initial runs
    #assign runs to the output files
    createInitialRuns(input_file, run_size, num_ways)
    
    # Merge the runs using the K-way merging 
    mergeFiles(output_file, run_size, num_ways)

#Driver to run 

if __name__ == "__main__":
    # No. of Partitions of input file. 
    num_ways = 10 #2
    
    #The size of each partition 
    # total size 10000 = 10 * 1000
    run_size = 1000 #10
    
    input_file = open("input.txt", 'w')
    output_file = open("output.txt", 'w')
    
    #generate input file 
    for i in range(num_ways * run_size):
        rand = randrange(0, run_size)
        input_file.write(str(rand)+"\n")
    
    input_file.close()    
    output_file.close()

    
    externalSort("input.txt", output_file, num_ways, run_size)
        
