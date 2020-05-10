import random as rand
from constants import *

class Enemy:

    #Init
    def __init__(self, 
        color: tuple = None, 
        size: int = None,
        sprite = None, 
        pos_x: int = None, 
        pos_y: int = None, 
        position: list = None ):
        """ Initialize enemy class

        Keyword Arguments:
            color {tuple} -- the color of this enemy in rgb (r,g,b) (default: {None})
            size {int} -- the size of this enemy (default: {None})
            pos_x {int} -- initialize position of this enemy in x-axis (default: {None})
            pos_y {int} -- initialize position of this enemy in y-axis (default: {None})
            position {list} -- position of this enemy in x and y axis [x.position, y position] (default: {None})
        """        
        self.color = color if color is not None else COLOR_BLUE
        self.size = size if size is not None else SIZE
        self.sprite = sprite  
        self.pos_x = pos_x if pos_x is not None else 10
        self.pos_y = pos_y if pos_x is not None else 10
        self.position = position if position is not None else [self.pos_x, self.pos_y]
        self.set_random_horizontal_position(0, SCREEN_WIDTH - self.size)

    def set_random_horizontal_position(self, start: int = 0, end: int = 0):
        """ Set random enemy position in horizontal axis

        Keyword Arguments:
            start {int} --  Start of the range (default: {0})
            end {int} -- End of the range (default: {0})

        Raises:
            ValueError: End value should not exceed the width of the window
        """

        if end >= SCREEN_WIDTH:
            print("End value should not exceed or equal to width")
            raise ValueError("End value should not exceed or equal to width") 
        else:     
            self.position = [rand.randint(start,end), self.pos_y]



