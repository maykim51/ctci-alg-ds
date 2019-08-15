'''
CTCI 2.1 Remove Dups:

Write code to remove duplicates from an unsorted linked list. 

FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?
'''
from linked_list_ctci import LinkedList
from collections import Counter

#iterate all linked list
#if curr node is equal to previous node
# remove it

def removeDups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll


def removeDups_followup(ll):
    if ll.head is None:
        return
    
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    
    return ll.head

def remove_dups_followup(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll.head


# test
if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.add(2)
    ll1.add('a')
    ll1.add('b')
    ll1.add(3)
    ll1.add_multiple([3,5,7])
    
    print(ll1)
    removeDups(ll1)