class Player:

    #Init
    def __init__(self, color=None, size=None, pos_x = None, pos_y = None, position = None):
        self.color = color if color is not None else (245,245,245)
        self.size = size if size is not None else 50 
        self.pos_x = pos_x if pos_x is not None else self.size
        self.pos_y = pos_y if pos_y is not None else self.size
        self.position = position if position is not None else [self.pos_x, self.pos_y]



    def set_player_position(self, x: int = 0, y: int = 0):
        self.position = [x,y]
