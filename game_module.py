import pygame
import sys

# start the game
pygame.init()

# constant
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BACKGROUND = (0, 0, 0)

# player variable
player_pos = [400, 500]  # [x, y]
player_size = 50

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#game condition
game_over = False

while not game_over:

    #game loop
    for event in pygame.event.get():

        x = player_pos[0]
        y = player_pos[1]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]

        if event.type == pygame.QUIT:
            sys.exit()

    # fill the background color
    screen.fill(BACKGROUND)

    # make the player
    pygame.draw.rect(screen, RED,
                     (player_pos[0], player_pos[1], player_size, player_size))

    # updating the game screen
    pygame.display.update()
