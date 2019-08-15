'''
CTCTI 1.4. Palindrome Permutation: 

Palindrome Permutation: 
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words. 

EXAMPLE 
Input: Tact Coa 
Output: True (permutations: "taco cat", "atco eta", etc.) 

'''
import unittest 
from collections import Counter

def pal_perm(s):
    s = s.replace(" ", "").lower() ##!!! save it to new variable!!
    print(s)
    counter = Counter(s)
    flag = 0
    for c in counter:
        if counter[c] %2 != 0:
            flag += 1
        if flag > 1:
            return False
    return True


# unit test
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()