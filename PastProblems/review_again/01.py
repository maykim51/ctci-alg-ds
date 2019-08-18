'''
Leetcode mock MS 01: palindromic 
https://leetcode.com/problems/palindromic-substrings/solution/
https://algospot.com/wiki/read/Manacher%27s_algorithm

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.

SOLUTION
1) extend around center (think about how i will iterate centers!!!)
'''

##option 1. extend around center
class Solution:
    def countSubstrings(self, S):
        N = len(S)
        res = 0
        
        #because there are (2N-1) possible centers...
        for center in range(2*N-1):
            left = center //2
            right = left + center%2
            while left >= 0 and right < N and S[left] == S[right]:
                left -= 1
                right += 1
                res +=1
        
        return res
    # def countSubstrings(self, S):
    #     N = len(S)
    #     ans = 0
    #     #because there are (2N-1) possible centers...
    #     for center in range(2*N - 1):
    #         left = center // 2
    #         right = left + center % 2
    #         while left >= 0 and right < N and S[left] == S[right]:
    #             ans += 1
    #             left -= 1
    #             right += 1
    #     return ans


#option2 # manacher's algorithm : returns max len palindrome
def countSubstrings(S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in range(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)/2 for v in manachers(S))
# #Driver
# sol = Solution()
# print(sol.countSubstrings('banana'))
countSubstrings('banana')
