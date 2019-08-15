'''
https://www.geeksforgeeks.org/practice-problems-on-hashing/
Que – 2. The keys 12, 18, 13, 2, 3, 23, 5 and 15 are inserted into an initially empty hash table of length 10 
using open addressing with hash function h(k) = k mod 10 and linear probing. What is the resultant hash table?
'''
hash_table = [None]*10
keys = [12, 18, 13, 2, 3, 23, 5, 15]
        
def hash(x):
    return x%10

for key in keys:
    hashed = hash(key)
    while hash_table[hashed] != None:
        hashed = hash(hashed + 1)
    hash_table[hashed] = key

print(hash_table)
