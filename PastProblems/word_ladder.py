'''
[MS SDE] Word-ladder
https://leetcode.com/problems/word-ladder but with a complex description. Same idea, and process.

SOLUTION
1) Use bfs in graph, but key is intermediate_word!!!!!! like d*g, *og!
traverse 할때는 내가 만들 수 있는 intermediate_word를 기반으로 딕셔너리를 탐색!

2) Bidirecition BFS
'''
import unittest


####Option 1 - mine
# def ladderLength(beginWord, endWord, wordList):
#     if endWord not in wordList:
#         return 0
#     wordList.append(beginWord)
    
#     #Create graph
#     ladders = {}   
#     for word in wordList:
#         if word not in ladders:
#             ladders[word] = set([])
#         visited = set([word])
        
#         for dest in wordList:
#             if dest in visited or word in ladders[dest]:
#                 break
#             else:
#                 if is_one_edit(word, dest):
#                     ladders[word].add(dest)
#                     ladders[dest].add(word)        
#             visited.add(dest)
            
#     '''remove later'''
#     print(ladders)
    
#     #BFS
#     queue = [beginWord]
#     visited = set([beginWord])
#     level = 1
    
#     while queue:
#         curr = queue.pop(0)
#         if curr == 's':
#             level += 1
#         elif curr == endWord:
#             return level
        
#         else:
#             visited.add(curr)          
#             for word in ladders[curr] - visited:
#                 queue.append(word)
#             queue.append('s')
            
        
#     return 0     
    
            
            
# def is_one_edit(word1, word2):
#     count = 0
#     #assume len(word1) == len(word2)
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#         if count > 1: 
#             return False
#     return True
        

###Option 2: Leetcode
from collections import defaultdict
import collections


def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    L = len(beginWord)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time. 
    '''
    key is d*g, *og!!
    '''    
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            # Key is the generic word
            # Value is a list of words which have the same intermediate generic word.
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


    # Queue for BFS
    queue = collections.deque([(beginWord, 1)])
    # Visited to make sure we don't repeat processing same word.
    visited = {beginWord: True}
    while queue:
        current_word, level = queue.popleft()      
        for i in range(L):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in all_combo_dict[intermediate_word]:
                # If at any point if we find what we are looking for
                # i.e. the end word - we can return with the answer.
                if word == endWord:
                    return level + 1
                # Otherwise, add it to the BFS Queue. Also mark it visited
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            all_combo_dict[intermediate_word] = []
    return 0


#Driver
class Test(unittest.TestCase):
    def test_ladderLength(self):
        
        self.assertEqual(ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]), 0)

if __name__ == "__main__":
    unittest.main()
                     