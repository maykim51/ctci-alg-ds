'''
CTCI 2.2 Return Kth to Last: 

Implement an algorithm to find the kth to last element of a singly linked list. 
'''
from linked_list_ctci import LinkedList

def kth_to_last(ll, k):
    curr = ll.head
    runner = curr
    for _ in range(k):
        if curr.next:
            runner = runner.next
        else: # no cycle ll.
            return "k is too big for this ll"
        
    while runner.next:
        runner = runner.next
        curr = curr.next
    
    return curr
    
# test
ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))