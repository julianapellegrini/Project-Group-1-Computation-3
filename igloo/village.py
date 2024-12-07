import pygame
from igloo.shed import shed
from config import *


def area(player):
    # Setup
    current_state = "main"  # Start in the main area

    while True:
        if current_state == "main":
            current_state = village(player)
        elif current_state == "shed":
            current_state = shed(player)


def village(player):

    # set the background
    background = pygame.image.load("images/village.jpg")
    background = pygame.transform.scale(background, resolution)

    # set clock for fps
    clock = pygame.time.Clock()

    # set the screen
    screen = pygame.display.set_mode(resolution)

    # start player on the left side of the screen
    player.rect.left = 0

    # set the special area
    special_area = pygame.Rect(530, 30, 140, 140)

    running = True
    while running:
        # set clock
        clock.tick(fps)

        # display the background
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # update the player's position
        player.update(screen)

        if special_area.colliderect(player.rect):
            shed(player)
            player.rect.top = 200
            player.rect.left = 560

        if player.rect.left <= 0:
            player.rect.left = width - player.rect.width
            return "main"

        # draw the player
        pygame.draw.rect(screen, bice_blue, player.rect)

    # update the display
    print('flip')
    pygame.display.flip()
