'''
Graph - Boggle
https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
https://seongjaemoon.github.io/algorithm/2018/01/27/algorithmBoggleGame.html 

Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character. 
Find all possible words that can be formed by a sequence of adjacent characters. 
Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.

Example:

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G', 'I', 'Z'},
                       {'U', 'E', 'K'},
                       {'Q', 'S', 'E'}};
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ
         
SOLUTION
1) DFS
2) Trie (below)

'''
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        tn = self.root   # tn = TrieNode
        for c in word:
            tn = tn.nodes[c]
        tn.word = word
        
class Solution(object):
    def findWords(self, board, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        tn = trie.root
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, tn, res)
        return res
    
    def dfs(self, i, j, board, tn, res):
        if tn.word:
            res.append(tn.word)
            tn.word = None # rain and rainy in words

        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] in tn.nodes:
            c = board[i][j]
            board[i][j] = '#'
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.dfs(i+x, j+y, board, tn.nodes[c], res)
            board[i][j] = c
        

#Driver
words = ["GEEKS", "FOR", "QUIZ", "GO"]
board   = [
    ['G','I','Z'],
    ['U','E','K'],
    ['Q','S','E']
]

sol = Solution()
print(sol.findWords(board, words))