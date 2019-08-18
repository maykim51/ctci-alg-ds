'''
CTCI 8.6. Towers of Hanoi: 
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes 
which can slide onto any tower. 
The puzzle starts with disks sorted in ascending order of size from top to bottom 
(i.e., each disk sits on top of an even larger one). 

You have the following constraints: 
(1) Only one disk can be moved at a time. 
(2) A disk is slid off the top of one tower onto another tower. 
(3) A disk cannot be placed on top of a smaller disk. 

Write a program to move the disks from the first tower to the last using stacks. 
'''

# Move the blocks on tower1(origin) to tower3(destination).

def towers_of_hanoi(origin, _buffer, destination, n=None):
  if n is None:
    n = len(origin.discs)
  if n == 0:
    return
  towers_of_hanoi(origin, destination, _buffer, n - 1)
  #가장 위의 원판을 destination으로 옮겨준다
  disc = origin.discs.pop() 
  destination.discs.append(disc)
  towers_of_hanoi(_buffer, origin, destination, n - 1)

class Tower(object):
  def __init__(self, name, discs=None):
    self.name = name
    if discs:
      self.discs = discs
    else:
      self.discs = []
  
  def __str__(self):
    return self.name

import unittest

class Test(unittest.TestCase):
  def test_towers_of_hanoi(self):
    tower1 = Tower("Tower1", ["6", "5", "4", "3", "2", "1"])
    tower2 = Tower("Tower2")
    tower3 = Tower("Tower3")
    towers_of_hanoi(tower1, tower2, tower3)
    self.assertEqual(tower1.discs, [])
    self.assertEqual(tower2.discs, [])
    self.assertEqual(tower3.discs, ["6", "5", "4", "3", "2", "1"])

if __name__ == "__main__":
  unittest.main()
