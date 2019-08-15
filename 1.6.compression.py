'''
CTCTI 1.6. String Compression:

Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, 
your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a -z). 

'''
import unittest 


def string_compression(s):
    if len(s) <= 1:
        return s
    
    compressed = []
    count = 0
    
    for i in range(len(s)): ### !!! 0부터, 차근차근하게 세기...
        if i != 0 and s[i] != s[i-1]:
            count = 0
            compressed.append(s[i-1]+str(count))
        count += 1
        
    compressed.append(s[-1]+str(count))
    
    return min(s, ''.join(compressed), key = len) ###!!!!!!! learn to use min and key!!
    

# unit test
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()