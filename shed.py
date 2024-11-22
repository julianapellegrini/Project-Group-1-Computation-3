import pygame

from config import *
from utils import *


def shed(player):
    # setting up the background and the screen
    background = pygame.image.load("images/inside-igloo.png")

    # scaling the background image into our selected resolution
    background = pygame.transform.scale(background, resolution)

    # setting up the screen
    screen = pygame.display.set_mode(resolution)

    # setting up the clock for fps
    clock = pygame.time.Clock()

    # since i left the previous area from the right, here i begin on the left
    player.rect.left = 0

    # creating the player group and adding the player to it
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # setting up the shed area as a special area in the shed map location
    special_area =  pygame.Rect(530, 30, 140, 140)

    # normal ,main game loop
    # this is our base implementation and u are allowed to change this

    running = True

    while running:
        clock.tick(fps)
        # displaying the farm background on the entirety of the screen
        screen.blit(background, (0, 0))

        # allowing the user to quit even tho they shouldn't because our game is perfect
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # update player position
        player_group.update()

        # detect if the user walked in to the special area (which is the house)
        if special_area.colliderect(player.rect):
            under_construction()

            # changing the players position <tbd>
            player.rect.top = 200
            player.rect.left = 560
            player.rect.left = 560

        # allowing the player to return back to the previous area/screen
        if player.rect.left <= 0:
            # position the player to the right of the screen
            player.rect.left = width - player.rect.width

            # switching the player to the right of the screen
            player.rect.left = width - player.rect.width

            # switching back to the main game
            return "main"

        # drawing the player
        player_group.draw(screen)
        # updating the screen
        pygame.display.flip()