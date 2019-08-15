'''
CTCI 8.1 Triple step

https://www.geeksforgeeks.org/count-ways-reach-nth-stair-using-step-1-2-3/
'''
#recursive, brute force >> + memoization

# A decorator function for function 'f' passed as parameter 
# decorator @ runs before function?, and returns ITS OWN INNER FUNCTION!!!!!!!!!!!!!!
# https://bluese05.tistory.com/30
def memoize(f): 
	memory = {} 
	# This inner function has access to memory 
	# and 'f' 
	def inner(num): 
		if num not in memory:		 
			memory[num] = f(num) 
		return memory[num] 
	return inner 

@memoize
def TripleHop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return TripleHop(x - 1) + TripleHop(x - 2) + TripleHop(x - 3)


	


###Option 2
#Top down DP, memoization
def Method2(x):
    memo = [-1] * (x + 1) # 왜 한 개 더 만들지..?
    return TripleHopRecursive(x, memo)




def TripleHopRecursive(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]

# print (TripleHop(1))
# print( TripleHop(2))
# print( TripleHop(3))
# print( TripleHop(4))
# print( TripleHop(5))
# print( TripleHop(6))
print(TripleHop(40))

# print( Method2(1))
# print( Method2(2))
# print( Method2(3))
# print( Method2(4))
# print( Method2(5))
# print( Method2(6))