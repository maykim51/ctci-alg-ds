'''
Intern
Given a string consisting of only 0, 1, A, B, C where
A = AND
B = OR
C = XOR
Calculate the value of the string assuming no order of precedence and evaluation is done from left to right.

Constraints – The length of string will be odd. It will always be a valid string.
Example, 1AA0 will not be given as an input.

Examples:

Input : 1A0B1
Output : 1
1 AND 0 OR 1 = 1

Input : 1C1B1B0A0
Output : 0
https://www.geeksforgeeks.org/evaluate-a-boolean-expression-represented-as-string/
'''

import math as mt


def evaluateBoolExpr(s):
    n = len(s)

    for i in range(0, n - 2, 2): #부호를 확인하기때문에 n-2까지만. 숫자만 읽기 때문에 2 간격으로 하고, i+2에 결과값 저장.

        # AND
        if (s[i + 1] == "A"):

            if (s[i + 2] == "0" or s[i] == "0"):
                s[i + 2] = "0"
            else:
                s[i + 2] = "1"

        #OR
        elif (s[i + 1] == "B"):
            if (s[i + 2] == "1" or s[i] == "1"):
                s[i + 2] = "1"
            else:
                s[i + 2] = "0"

        #XOR
        else:
            if (s[i + 2] == s[i]):
                s[i + 2] = "0"
            else:
                s[i + 2] = "1"

    # return ord(s[n - 1]) - ord("0") ##?? Why ord?
    return s[n-1]


# Driver code
s = "1C1B1B0A0"
string = [s[i] for i in range(len(s))]
print(evaluateBoolExpr(string))
