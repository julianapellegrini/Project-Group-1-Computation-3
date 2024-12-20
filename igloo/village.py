import pygame
from igloo.shed import shed
from config import *


def area(player, map_layout, interface_w_save, interface_no_save):
    # Setup
    current_state = "main"  # Start in the main area

    while True:
        if current_state == "main":
            current_state = village(player, map_layout)
        elif current_state == "shed":
            current_state = shed(player)
        elif current_state == "map":
            current_state = map_layout(player, interface_w_save, interface_no_save)


def village(player, map_layout):

    # set the background
    background = pygame.image.load("images/village.png")
    background = pygame.transform.scale(background, resolution)

    # set clock for fps
    clock = pygame.time.Clock()

    # set the screen
    screen = pygame.display.set_mode(resolution)

    # start player on the left side of the screen
    player.rect.left = 5

    # set the special area
    special_area = pygame.Rect(753, 522, 140, 140)

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
        player.rect.y = 522

        if special_area.colliderect(player.rect):
            shed(player)
            player.rect.top = 200
            player.rect.left = 560

        if player.rect.left <= 0:
            player.rect.left = width - player.rect.width
            return "map"

        # draw the player
        screen.blit(player.image, player.rect)

        # update the display
        pygame.display.flip()
