'''
Frequently asked 06
https://www.geeksforgeeks.org/microsofts-asked-interview-questions/
https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/

Clone a linked list with next and arbitrary (or random) pointer

You are given a Double Link List with one pointer of each node pointing to the next node just like in a single link list. 
The second pointer however CAN point to any node in the list and not just the previous node. 
Now write a program in O(n) time to duplicate this list. That is, write a program which will create a copy of this list.

Let us call the second pointer as arbit pointer as it can point to any arbitrary node in the linked list.
'''
##clone the linked list
## + in place clone: insert new nodes inbtween  original one
## + hash map