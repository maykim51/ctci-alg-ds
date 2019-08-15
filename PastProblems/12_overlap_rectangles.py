'''
MS:Intern

We were asked only one question in our group fly round.
N rectangles in 2-D space were given to us and we were given (x, y) coordinates of the bottom left corner of each rectangle 
and height and width of each rectangle. We had to return (x, y) coordinates of the bottom left corner of 
overlapping rectangle and also give its height and width.

https://www.geeksforgeeks.org/find-two-rectangles-overlap/
'''

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


class Rectagle:
    def __init__(self, lb=Point(0,0), height=0, width=0):
        self.lb = lb
        self.lt = Point(lb.x, lb.y+height)
        self.rb = Point(lb.x+width, lb.y)
        self.rt = Point(lb.x+width, lb.y+height)        
    
    
def doOverlap(rec1, rec2): #receives 2 Rectagle(), returns False or True
    if rec1 is None or rec2 is None:
        return None
    
    if rec1.rb.x < rec2.lb.x or rec2.rb.x < rec1.lb.x :
        return False
    
    if rec1.lb.y > rec2.lt.y or rec2.lb.y > rec1.lt.y :
        return False
    
    return True

p1 = Point(0,0)
p2 = Point(3,0)
rec1 = Rectagle(p1, 5, 5)
rec2 = Rectagle(p2, 1, 1)

# if __name__ == '__init__':
if doOverlap(rec1, rec2):
    print('rec1 and rec2 overlap.')
else: print('rec1 and rec 2 do not overlap.')