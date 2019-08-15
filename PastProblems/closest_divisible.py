'''
Internship Q.

Find the number closest to n and divisible by m
Given two integers n and m. The problem is to find the number closest to n and divisible by m. 
If there are more than one such number, then output the one having maximum absolute value. 
If n is completely divisible by m, then output n only. Time complexity of O(1) is required.

https://www.geeksforgeeks.org/find-number-closest-n-divisible-m/

'''
'''
Constraints: m != 0

Examples:

Input : n = 13, m = 4
Output : 12

Input : n = -15, m = 6
Output : -18
Both -12 and -18 are closest to -15, but
-18 has the maximum absolute value.
'''

def closest_divisible(n, m):
    q = int(n/m)
    
    n1 = m*q
    
    #n2
    

def closestNumber(n, m) : 
    q = int(n / m) 
      
    # 1st possible closest number 
    n1 = m * q 
      
    # 2nd possible closest number 
    if((n * m) > 0) : 
        n2 = (m * (q + 1)) 
    else : 
        n2 = (m * (q - 1)) 
      
    # if true, then n1 is the required closest number 
    if (abs(n - n1) < abs(n - n2)) : 
        return n1 
      
    # else n2 is the required closest number  
    return n2 
      
      
# Driver program to test above 
n = 13; m = 4
print(closestNumber(n, m)) 
  
n = -15; m = 6
print(closestNumber(n, m)) 
  
n = 0; m = 8
print(closestNumber(n, m)) 
  
n = 18; m = -7
print(closestNumber(n, m)) 