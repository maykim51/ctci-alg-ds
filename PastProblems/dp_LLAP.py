'''
MS Intern: Longest Arithmetic Progression  - Dynamic Programming in O(N^2)

Longest Arithmetic Progression | DP-35
Given a set of numbers, find the Length of the Longest Arithmetic Progression (LLAP) in it.
Examples:

set[] = {1, 7, 10, 15, 27, 29}
output = 3
The longest arithmetic progression is {1, 15, 29}

set[] = {5, 10, 15, 20, 25, 30}
output = 6
The whole set is in AP

https://www.geeksforgeeks.org/longest-arithmetic-progression-dp-35/
'''

#Assume the set is sorted.

###Option 1 
# i < j < k , Given set[j], find i and k that 2*set[j] = set[i] + set[k]
'''
Initialize i as j-1 and k as j+1
Do following while i >= 0 and j <= n-1
If set[i] + set[k] is equal to 2*set[j], then we are done.
If set[i] + set[k] > 2*set[j], then decrement i (do i–).
Else if set[i] + set[k] < 2*set[j], then increment k (do k++).
'''

###Option 2 - DP!

'''
How to extend the above solution for the original problem?
The above function returns a boolean value. The required output of original problem is Length of the Longest Arithmetic Progression (LLAP) which is an integer value. If the given set has two or more elements, then the value of LLAP is at least 2 (Why?).
The idea is to create a 2D table L[n][n]. An entry L[i][j] in this table stores LLAP with set[i] and set[j] as first two elements of AP and j > i. The last column of the table is always 2 (Why – see the meaning of L[i][j]). Rest of the table is filled from bottom right to top left. To fill rest of the table, j (second element in AP) is first fixed. i and k are searched for a fixed j. If i and k are found such that i, j, k form an AP, then the value of L[i][j] is set as L[j][k] + 1. Note that the value of L[j][k] must have been filled before as the loop traverses from right to left columns.

Following is the implementation of the Dynamic Programming algorithm.
'''

# Python 3 program to find Length of the 
# Longest AP (llap) in a given sorted set. 
# The code strictly implements the algorithm 
# provided in the reference 

# Returns length of the longest AP 
# subset in a given set 
def lenghtOfLongestAP(set, n): 

	if (n <= 2): 
		return n 

	# Create a table and initialize all 
	# values as 2. The value of L[i][j] 
	# stores LLAP with set[i] and set[j] 
	# as first two elements of AP. Only 
	# valid entries are the entries where j>i 
	L = [[0 for x in range(n)] 
			for y in range(n)] 
	llap = 2 # Initialize the result 

	# Fill entries in last column as 2. 
	# There will always be two elements 
	# in AP with last number of set as 
	# second element in AP 
	for i in range(n): 
		L[i][n - 1] = 2

	# Consider every element as second 
	# element of AP 
	for j in range(n - 2, 0, -1): 

		# Search for i and k for j 
		i = j - 1
		k = j + 1
		while(i >= 0 and k <= n - 1): 

			if (set[i] + set[k] < 2 * set[j]): 
				k += 1

			# Before changing i, set L[i][j] as 2 
			elif (set[i] + set[k] > 2 * set[j]): 
				L[i][j] = 2
				i -= 1

			else: 

				# Found i and k for j, LLAP with i and j 
				# as first two elements are equal to LLAP 
				# with j and k as first two elements plus 1. 
				# L[j][k] must have been filled before as 
				# we run the loop from right side 
				L[i][j] = L[j][k] + 1

				# Update overall LLAP, if needed 
				llap = max(llap, L[i][j]) 

				# Change i and k to fill more L[i][j] 
				# values for current j 
				i -= 1
				k += 1

				# If the loop was stopped due to k 
				# becoming more than n-1, set the 
				# remaining entties in column j as 2 
				while (i >= 0): 
					L[i][j] = 2
					i -= 1
	return llap 

# Driver Code 
if __name__ == "__main__": 
	
	set1 = [1, 7, 10, 13, 14, 19] 
	n1 = len(set1) 
	print(lenghtOfLongestAP(set1, n1)) 

	set2 = [1, 7, 10, 15, 27, 29] 
	n2 = len(set2) 
	print(lenghtOfLongestAP(set2, n2)) 

	set3 = [2, 4, 6, 8, 10] 
	n3 = len(set3) 
	print(lenghtOfLongestAP(set3, n3)) 

# This code is contributed by ita_c 
