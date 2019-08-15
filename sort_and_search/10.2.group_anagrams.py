'''
CTCI 10.2. Group Anagrams: 

Write a method to sort an array of strings so that all the anagrams are next to each other. 

SOLUTION
bucket sort
'''
#### option 1 str별로 다 정렬
# Group string anagrams together.

# def group_anagrams(strings): ####!!!!! python's advantage!!!
#     pairs = [(s, sorted(s)) for s in strings]
#     pairs.sort(key=lambda p: p[1])
#     return [p[0] for p in pairs]
  
# import unittest

# class Test(unittest.TestCase):
#     def test_group_anagrams(self):
#     strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
#     self.assertEqual(group_anagrams(strings),
#             ["bat", "tab", "car", "cat", "arts", "star", "rat", "tar"])

# if __name__ == "__main__":
# unittest.main()


#### option 2 딕셔너리에 자기 그룹별로 묶어준다음에 배열로 반환 - bucket sort

def GroupAnagrams():
    strings = initialise_anagrams()
    anagrams = {}
    for i in range(len(strings)):
        word = "".join(sorted(strings[i].lower()))
        if word not in anagrams:
            anagrams[word] = []
        anagrams[word].append(strings[i])
    keys = anagrams.keys()
    index = 0
    for i in range(len(keys)):
        values = anagrams[keys[i]]
        for j in range(len(values)):
            strings[index] = values[j]
            index += 1
    print(strings)


def initialise_anagrams():
    strings = [0] * 8
    strings[0] = "abed"
    strings[1] = "later"
    strings[2] = "bead"
    strings[3] = "alert"
    strings[4] = "altered"
    strings[5] = "bade"
    strings[6] = "alter"
    strings[7] = "alerted"
    return strings

GroupAnagrams()

