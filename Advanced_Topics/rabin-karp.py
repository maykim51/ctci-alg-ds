'''
CTCI Advanced - Rabin-Karp
https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/


Rabin karp hash function
This is simple mathematics, we compute decimal value of current window from previous window.
For example pattern length is 3 and string is “23456”
You compute the value of first window (which is “234”) as 234.
How how will you compute value of next window “345”? You will do (234 – 2*100)*10 + 5 and get 345.
'''
# Following program is the python implementation of # Rabin Karp Algorithm given in CLRS book 

# d is the number of characters in the input alphabet 
d = 256

# pat -> pattern 
# txt -> text 
# q -> A prime number 

def my_search(word, txt, q):
    M = len(word)
    N = len(txt)
    h = 1 #자릿수 곱할때 쓰이는 hash 상수
    w = 0
    t = 0
    
    #set up consts for hashing
    for i in range(M-1):
        h = (h*d)%q
    
    #첫번째 해시를 구한다
    for i in range(M):
        w = (d*w + ord(txt[i]))%q
        t = (d*t + ord(txt[i]))%q
    
    #비교해서 찾으러 간다!
    for i in range(N-M+1):        
        if w == t:
            for j in range(M):
                if txt[i+j] != word[j]:
                    break
            j += 1
            if j == M:
                print('word found at index {}.'.format(str(i)))
        
        #rehash
        if i < N-M:
            t = (d*(t - ord(txt[i])*h) + ord(txt[i+M]))%q
            
            if t < 0:
                t += q
            

# Driver program to test the above function 
txt = "GEEKS FOR GEEKS"
word = "GEEK"
q = 101 # A prime number 

my_search(word,txt,q) 



def search(pat, txt, q): 
	M = len(pat) 
	N = len(txt) 
	i = 0
	j = 0
	p = 0 # hash value for pattern 
	t = 0 # hash value for txt 
	h = 1

    ##256^3 만드는것. 대신 mod를 해줌.
	# The value of h would be "pow(d, M-1)%q" 
	for i in range(M-1): 
		h = (h*d)%q 

	# 이 자리에서 이 다음자리로 갈 수 있음.
    # Calculate the hash value of pattern and first window 
	# of text 
	for i in range(M): 
		p = (d*p + ord(pat[i]))%q 
		t = (d*t + ord(txt[i]))%q 

	# Slide the pattern over text one by one 
	for i in range(N-M+1): 
		# Check the hash values of current window of text and 
		# pattern if the hash values match then only check 
		# for characters on by one 
		if p==t: 
			# Check for characters one by one 
			for j in range(M): 
				if txt[i+j] != pat[j]: 
					break

			j+=1
			# if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1] 
			if j==M: 
				print ('Pattern found at index',str(i))

		# Calculate hash value for next window of text: Remove 
		# leading digit, add trailing digit 
		if i < N-M: 
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q 

			# We might get negative values of t, converting it to 
			# positive 
			if t < 0: 
				t = t+q 

# Driver program to test the above function 
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101 # A prime number 
search(pat,txt,q) 

