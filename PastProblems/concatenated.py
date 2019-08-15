'''
Concatenated string with uncommon characters of two strings
Two strings are given and you have to modify 1st string such that 
1) all the common characters of the 2nd strings have to be removed and 
2) the uncommon characters of the 2nd string have to be concatenated with uncommon characters of the 1st string.

Examples:

Input : S1 = "aacdb"
        S2 = "gafd"
Output : "cbgf"

Input : S1 = "abcs";
        S2 = "cxzca";
Output : "bsxz"

!!!!!!! set 조작, string 출력

'''


def concatenate(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    
    res = set1-set2
    res.update(set2-set1)
    
    return "".join(list(res))


s1 = 'aacdb'
s2 = 'gafd'
print(concatenate(s1, s2))

s3 = "abcs"
s4 = "cxzca"
print(concatenate(s3, s4))