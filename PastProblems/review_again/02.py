'''
Leetcode mock MS 02: maximum abs
https://leetcode.com/problems/maximum-of-absolute-value-expression/

Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 

Example 1:
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13

Example 2:
Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 

Constraints:
2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
'''

##brute force

def maxi(arr1, arr2):
    L = len(arr1)
    mx = 0
    for j in range(L):
        for i in range(j):
            temp = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)
            if temp > mx:
                mx = temp
    return mx


def maxAbsValExpr(self, x, y):
        res, n = 0, len(x)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            closest = p * x[0] + q * y[0] + 0
            for i in range(n):
                cur = p * x[i] + q * y[i] + i
                res = max(res, cur - closest)
                closest = min(closest, cur)
        return res

#Drvier
arr1 = [1,2,3,4]
arr2 = [-1,4,5,6]
print(maxi(arr1, arr2))     