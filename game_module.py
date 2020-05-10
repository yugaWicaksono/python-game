#import internal python modules
import datetime
import pygame
import random
import sys

#import classes as OOP
from constants import *
from enemy import *
from player import *



class GameModule: 
    """ Game engine module as class
    """

    #init
    def __init__(self, enemy = None, player = None, screen = None, clock = None, game_over = None, enemies = None ):

        """ 
        Initialize the game module 
        """        

        # initialize pygame
        pygame.init()

        # player 
        self.player = Player()

        self.enemy = Enemy()

        # Screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        #clock
        self.clock = pygame.time.Clock() 

        #set game over state 
        self.game_over = game_over if game_over is not None else False 

        #set enemies list 
        self.enemies = enemies if enemies is not None else [self.enemy]

    # methods
    def check_collision_x_axis(self, enemy):
        collision = False
        e_x = enemy.position[0]
        p_x = self.player.position[0]

        left_collision = (e_x >= p_x and e_x < p_x + self.player.size)
        right_collision = (p_x >= e_x and  p_x < e_x + enemy.size)

        if left_collision or right_collision:
            collision = True

        return collision

    def check_collision_y_axis(self, enemy):
        collision = False
        e_y = enemy.position[1]
        p_y = self.player.position[1]

        left_collision = (e_y >= p_y and e_y < (p_y + self.player.size))
        right_collision = (p_y >= e_y and p_y < (e_y + enemy.size))

        if left_collision or right_collision:
            if left_collision:
                print(" ->> left Y collision detected")
            else:
                print(" ->> right Y collision detected")
            collision = True

        return collision

    def collision_detection(self, enemy):
        if self.check_collision_x_axis(enemy):
            if self.check_collision_y_axis(enemy):
                print("you have been hit")
                return True

        return False        

    def check_multiple_collision(self):
        for enemy in self.enemies: 
            if self.collision_detection(enemy):
                return True
        return False        

    def draw_enemies(self):
        for enemy in self.enemies:    
        # create the enemy rect 
            pygame.draw.rect(self.screen, enemy.color, (enemy.position[0], enemy.position[1], enemy.size, enemy.size))

    def generate_enemies(self):
        delay = random.random()
        if len(self.enemies) < QUANTITY and delay < 0.1:
            enemy = Enemy()
            self.enemies.append(enemy)

    def get_current_time(self):
        """ Get current date and time as string

        Returns:
            string -- string of date and time
        """        
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def player_movement(self, e): 
        """ handle the button left right and the a and d button press to moove player

        Arguments:
            e {pygame.event} -- pygame event that need to be passe

        Raises:
            ValueError: no event being passed
        """
        if e is None:
            print("No event provided")
            raise ValueError("No event provided")

        x = self.player.position[0]
        y = self.player.position[1]

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                x -= self.player.size
            elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                x += self.player.size

            self.player.set_player_position(x,y)

    def quit_game(self):
        """
        Call sys exit when the game quit event is triggered
        """    
        print("=== Exiting game ===")
        sys.exit()

    def start(self):

        #print game start
        print(f"=== Game started: {self.get_current_time()} ===")

        #game loop
        while not self.game_over:
            # player movement
            for event in pygame.event.get():
                # movement loop
                self.player_movement(event)

                #handle the game quit
                if event.type == pygame.QUIT:
                    self.quit_game()

            # fill the background color
            self.screen.fill(COLOR_BACKGROUND)

            # draw the player
            pygame.draw.rect(self.screen, self.player.color,(self.player.position[0], self.player.position[1], self.player.size, self.player.size))

            #draw the enemies 
            self.generate_enemies()
            self.update_enemy_movement()
            self.draw_enemies()
 
            #check collision
            if self.check_multiple_collision():
                self.game_over = True 
                break

            #framerate 
            self.set_frame_rate()

            # updating the game screen
            pygame.display.update()

    def update_enemy_movement(self):
        for idx, enemy in enumerate(self.enemies):
            if enemy.position[1] >= 0 and enemy.position[1] < SCREEN_HEIGHT:
                enemy.position[1] += GAME_SPEED
            else:
                self.enemies.pop(idx)

    def set_frame_rate(self, fr: int = FRAMERATE):
        FRAMERATE = fr 
        self.clock.tick(FRAMERATE)
