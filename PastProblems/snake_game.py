'''
[MS L60 Round4] "Design Snake Game"

https://www.geeksforgeeks.org/design-snake-game/

SOLUTION: clarify > objects > relationship > actions
objects: Snake, Board, Cell, Game

'''
from enum import Enum
from linked_list import LinkedList
class CellStatus(Enum):
    EMPTY = 1
    FOOD = 2
    SNAKE = 3


class Cell:
    def __init__(self, row, col):
        self.row, self.col = row, col
        self.status = CellStatus.EMPTY
        print(self.status)        
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

class Snake:
    def __init__(self, initPos:Cell):
        self.head = initPos #head: saves row and col of head
        self.body = LinkedList(self.head)
    
    def grow(self):
        self.body.insert()
    
    def move(self, nextCell:Cell):
        print('Snake is moving to {row}, {col}'.format(row=nextCell.row, col = nextCell.col))
        self.head = nextCell
        self.body.addFirst(nextCell)
        tail = self.body.removeLast().value #type is Cell
        tail.set_status = CellStatus.EMPTY
    
    def checkCrush(self, nextCell:Cell):
        print('checking for crash')
        ############WIP
        
class Board:
    def __init__(self, rows, cols):
        pass
    
print(Cell(0,10))
