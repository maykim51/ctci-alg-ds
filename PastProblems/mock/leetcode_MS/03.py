'''
!!어려움 ㅠㅠ
Leetcode mock MS 03: shortest common sequence
https://leetcode.com/problems/shortest-common-supersequence/

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  
If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T 
(possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.

SOLUTION: LCS를 찾아서 거기서 이어 붙인다
'''

def shortestCommonSupersequence(A, B): ##그냥 관례>... WHY??
        def lcs(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(m):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            return dp[-1][-1]

        res, i, j = "", 0, 0
        for c in lcs(A, B):
            while A[i] != c:
                res += A[i]
                i += 1
            while B[j] != c:
                res += B[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + A[i:] + B[j:]
    
shortestCommonSupersequence("abac", "cab")