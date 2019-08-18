'''
REF: https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
SOLUTION 
2를 곱한다
1보다 크면 1표기, 아니면 0 표기

'''

# Return a binary string representation of the given floating point number
# between 0 and 1 as long as it accurately fits in 32 bits.
import unittest

def num_to_string(num):
    if num <= 0 or num >= 1:
        return -1
    binary = '0.'
    length = length_of_num(num)
    print('length: {}'.format(length))
    for _ in range(length):
        num *= 2
        if num >= 1:
            binary += '1'
            num -= 1
        else: 
            binary += '0'
    print('binary: {}'.format(binary))
    return binary

def length_of_num(num):
    s = str(num)
    return len(s) - s.index('.') -1

class Test(unittest.TestCase):
  def test_num_to_string(self):
    self.assertEqual(num_to_string(0.75), "0.11")
    self.assertEqual(num_to_string(0.625), "0.101")
    # self.assertEqual(binary_to_string(0.3), Exception("Insufficient precision"))

if __name__ == "__main__":
  unittest.main()