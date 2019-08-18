'''
Frequently asked 04
https://www.geeksforgeeks.org/remove-duplicates-from-a-given-string/
https://www.geeksforgeeks.org/sum-of-two-linked-lists/

Given two linked lists that represent two big numbers (numbers that can not be stored in an int or long long int), 
write a function that adds the numbers and store the result in a third list.

Input: List1: 5->6->3  // represents number 365
       List2: 8->4->2 //  represents number 248
Output: Resultant list: 3->1->6  // represents number 613

Input: List1: 7->5->9->4->6  // represents number 64957
       List2: 8->4 //  represents number 48
Output: Resultant list: 5->0->0->5->6  // represents number 65005
'''
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def addTwoLists(self, first, second): 
        prev = None
        temp = None
        carry = 0

        while(first is not None or second is not None): 
            # Calculate the value of next digit in 
            # resultant list 
            fdata = 0 if first is None else first.data 
            sdata = 0 if second is None else second.data 
            Sum = carry + fdata + sdata 

            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = Node(Sum) 

            # if this is the first node then set it as head 
            # of resultant list 
            if self.head is None: 
                self.head = temp 
            else : 
                prev.next = temp 

            prev = temp 

            if first is not None: 
                first = first.next
            if second is not None: 
                second = second.next

        if carry > 0: 
            temp.next = Node(carry) 


    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data)
            temp = temp.next




# Driver program to test above function 
first = LinkedList() 
second = LinkedList() 

# Create first list 
first.push(6) 
first.push(4) 
first.push(9) 
first.push(5) 
first.push(7) 
print("First List is ")  
first.printList() 

# Create second list 
second.push(4) 
second.push(8) 
print("\nSecond List is ")  
second.printList() 

# Add the two lists and see result 
res = LinkedList() 
res.addTwoLists(first.head, second.head) 
print("\nResultant list is ")  
res.printList() 
