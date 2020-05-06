import random


class Enemy:

    #Init
    def __init__(self, color: tuple = None, size: int = None, pos_x: int = None, pos_y: int = None, position: list = None ):
        self.color = color if color is not None else (245,245,245)
        self.size = size if size is not None else 50  
        self.pos_x = pos_x if pos_x is not None else 10
        self.pos_y = pos_y if pos_x is not None else 10
        self.position = position if position is not None else [self.pos_x, self.pos_y]

    def set_random_position():
        pass



