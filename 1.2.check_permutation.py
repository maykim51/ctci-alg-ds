'''
CTCTI 1.2. check permutation(순열)
같은 문자로 구성되어있고 순서만 다르다. 대소문자 구문.

Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. 

'''
'''
Python has its own function for permutation:

import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
'''

import unittest 

def check_permutation(s1, s2):
    #check length
    if len(s1) != len(s2):
        return False
        
    #sorted > must be identifcal
    l1 = list(s1)
    l2 = list(s2)
    l1.sort() ### sort() 는 수행만 하고, 결과는 return하지 않는다. 확실히 알아둘것.
    l2.sort()
    print('l1: {}, l2: {}'. format(l1, l2))
    
    if l1 == l2:
        return True


# CTCI Solution
from collections import Counter

def check_permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter() ##!!!!!!!!!!
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True



# unit test
class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation2(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()