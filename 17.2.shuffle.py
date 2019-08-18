'''
#popular!!
CTCI 17.2 Shuffle: 

Write a method to shuffle a deck of cards. It must be a perfect shuffle-
in other words, each of the 52! permutations of the deck has to be equally likely. 
Assume that you are given a random number generator which is perfect.

SOLUTION (2options)
option 1
recursion : n-1을 섞은 결과물 + 이중 하나를 랜덤으로 골라 n과 바꾸면 됨
option 2 - iterative (recommended)
i 번째 원소는 앞선 원소 중 아무거나와 랜덤하게 교환한다.
'''
###Option 1 : Recursion
from random import randint

def shuffle(cards, i):
    #base case
    if i == 0:
        return cards
    
    cards = shuffle(cards, i-1)
    k = randint(0, i)
    
    temp = cards[k]
    cards[k] = cards[i]
    cards[i] = temp
    
    return cards

#option 2 : Iterative
def shuffle_iterative(cards):
    #base case
    for i in range(len(cards)):
        k = randint(0, i)
    
        temp = cards[k]
        cards[k] = cards[i]
        cards[i] = temp
