from constants import *

class Player:

    #Init
    def __init__(self,
        color=None, 
        size=None,
        sprite = None,
        pos_x = None, 
        pos_y = None, 
        position = None):
        """ Initialize player class

        Keyword Arguments:
            color {tuple} -- the color of this player in rgb (r,g,b) (default: {None})
            size {int} -- the size of this player (default: {None})
            pos_x {int} -- initialize position of this player in x-axis (default: {None})
            pos_y {int} -- initialize position of this player in y-axis (default: {None})
            position {list} -- position of this player in x and y axis [x.position, y position] (default: {None})
        """        
        self.color = color if color is not None else COLOR_RED
        self.size = size if size is not None else SIZE
        self.sprite = sprite
        self.pos_x = pos_x if pos_x is not None else 4 * self.size
        self.pos_y = pos_y if pos_y is not None else SCREEN_HEIGHT - (2 * self.size)
        self.position = position if position is not None else [self.pos_x, self.pos_y]


    def set_player_position(self, x: int = 0, y: int = 0):
        self.position = [x,y]
