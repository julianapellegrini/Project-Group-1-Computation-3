import pygame.time

from utils import *
from config import *
import math
from player import Player


def execute_game():

    # SETUP
    # using the clock to control the time frame
    clock = pygame.time.Clock()

    # screen setup
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption('Endless Wilderness Explorer')

    # setting up the player
    player = Player()
    # creating a group for the player
    player_group = pygame.sprite.Group()
    # adding the player to the group
    player_group.add(player)

    # MAIN GAME LOOP

    running = True

    while running:

        # controlling the frame rate
        clock.tick(fps)

        # setting up the background
        screen.fill(forest_green)

        # handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # updating positions and visuals

        player_group.update()
        player_group.draw(screen)
        pygame.display.flip()


