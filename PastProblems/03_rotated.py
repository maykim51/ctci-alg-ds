'''
Frequently asked 03
https://www.geeksforgeeks.org/remove-duplicates-from-a-given-string/

Given a rotated array which is sorted search for an element in it 
An element in a sorted array can be found in O(log n) time via binary search. But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time.

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 3
Output : Found at index 8

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 30
Output : Not found

Input : arr[] = {30, 40, 50, 10, 20}
        key = 10   
Output : Found at index 3

SOLUTION : bst with medium
pick start and medium of the arr, 
check normal order or not
recurse.

'''
def search (arr, l, h, key): 
    if l > h: 
        return -1

    mid = (l + h) // 2
    if arr[mid] == key: 
        return mid 

    # If arr[l...mid] is sorted 
    if arr[l] <= arr[mid]: 
        if key >= arr[l] and key <= arr[mid]: 
            return search(arr, l, mid-1, key) 
        return search(arr, mid+1, h, key) 

    # If arr[l..mid] is not sorted, then arr[mid... r] 
    # must be sorted 
    if key >= arr[mid] and key <= arr[h]: 
        return search(arr, mid+1, h, key) 
    return search(arr, l, mid-1, key) 

# Driver program 
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 6
i = search(arr, 0, len(arr)-1, key) 
if i != -1: 
	print ("Index: %d"%i) 
else: 
	print ("Key not found") 

