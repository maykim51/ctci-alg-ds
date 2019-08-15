"""
'''part of Snake Game!'''

Singly Linked List Implementation¶

In a Linked List the first node is called the head and the last node is called the tail. 
Let's discuss the pros and cons of Linked Lists:

Pros ##!!!!!!!!!!!!!!!!!!!##
Linked Lists have constant-time insertions and deletions in any position, in comparison, 
arrays require O(n) time to do the same thing.

Linked lists can continue to expand without having to specify their size ahead of time 
(remember our lectures on Array sizing form the Array Sequence section of the course!)

Cons
To access an element in a linked list, you need to take O(k) time to go from the head of the list to the kth element. 
In contrast, arrays have constant time operations to access elements in an array.
"""


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = Node(head)

    def insert(self, value=None):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def insertList(self, *args):
        for element in args:
            self.insert(element)
    
    def removeLast(self):
        current = self.head
        while current.next.next:
            current = current.next
        last = current.next
        current.next = None
        return last
    
    def addFirst(self, value):
        if not value:
            newHead = Node(value)
            newHead.next = self.head
            self.head = newHead
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next     

    def printLinkedList(self):
        current = self.head
        while current.next:
            print(current.value, end=" > ")
            current = current.next
        print(current.value)
