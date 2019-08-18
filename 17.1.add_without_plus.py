'''
CTCI 17.1 Add without plus
Write a function that adds two numbers. You should not use+ or any arithmetic operators. 

SOLUTION
연산을 비트 연산자로 분리하면 된다!
 +   = 올림수 없이 계산 + 올림수만 계산 = XOR + ADD 한후 <<1
'''
def add(num1, num2):
    sum = num1 ^ num2 # 올림수 없이 그냥 계산 = XOR
    carry = (num1 & num2) << 1  #올림수만 계산
    if carry == 0:
        return sum
    else: 
        return add(sum, carry)

print(add(8, 9))