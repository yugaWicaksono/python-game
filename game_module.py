import pygame
import random
import sys

#import classes
from player import *
from enemy import *

# initialize pygame
pygame.init()

# constant
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# player variable

player = Player()
player.color = RED
player.pos_x = 4 * player.size
player.pos_y = HEIGHT - (2* player.size)
player.set_player_position(player.pos_x, player.pos_y)


#enemy
enemy = Enemy()



# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#game condition
game_over = False


# define functions for the game 
def player_movement(e): 

    if e is None:
        raise ValueError

    x = player.position[0]
    y = player.position[1]

    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_a or e.key == pygame.K_LEFT:
            x -= player.size
        elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
            x += player.size

        player.position = [x, y]

def quit_game():
     sys.exit()

#game loop
while not game_over:


    for event in pygame.event.get():

        # movement loop
        player_movement(event)

        if event.type == pygame.QUIT:
           quit_game()

    # fill the background color
    screen.fill(BACKGROUND_COLOR)

    # make the player
    pygame.draw.rect(screen, player.color,(player.position[0], player.position[1], player.size, player.size))

    # create the enemy rect 
    pygame.draw.rect(screen, enemy.color, (enemy.position[0], enemy.position[1], enemy.size, enemy.size))

    # updating the game screen
    pygame.display.update()
