'''
MS:Intern 
Reverse words in a given string
Example: Let the input string be “i like this program very much”. 
The function should change the string to “much very program this like i”

Input: s = “geeks quiz practice code”
Output: s = “code practice quiz geeks”

Input: s = “getting good at coding needs a lot of practice”
Output: s = “practice of lot a needs coding at good getting”

https://www.geeksforgeeks.org/reverse-words-in-a-given-string/
'''

# Python3 program to reverse a string 
# s = input() 
s = "i like this program very much"
words = s.split(' ') 
string =[] 
for word in words: 
	string.insert(0, word) 

print("Reversed String:") 
print(" ".join(string)) 

