'''
CTCI 1.1. Is Unique


If you can't use other data structure! (below we used a list)
1. O(N^2) : iterate, compare with all other elements
2. O(nlogn)sort  + linearly check O(N) 

https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/1_Is%20Unique/IsUnique.py

'''
#O(N)


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char) #returns unicode of the char
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True
