import pygame
from igloo.shed import shed
from config import *


def area(player, map_layout, interface_w_save, interface_no_save):
    """
    Area where the player can interact with the igloo special area and the map.
    The function changes the state of the game based on the player's location.

    Parameters
    ----------
    player : object
        The player object that interacts with the igloo/shed and the map.

    map_layout : function
        The function that displays the map layout screen.

    interface_w_save : function
        The function that displays the interface if the player has a save.

    interface_no_save : function
        The function that displays the interface if the player does not have a save.

    Returns
    -------
    None
        The function does not return anything. It updates the player's location and the state of the game.
    """
    current_state = "main"  # start in the main area

    # change the state of the game based on the player's location
    while True:
        if current_state == "main":
            current_state = village(player, map_layout)
        elif current_state == "shed":
            current_state = shed(player)
        elif current_state == "map":
            current_state = map_layout(player, interface_w_save, interface_no_save)


def village(player, map_layout):
    """
    Display the village area where the player can interact with the special area of the igloo/shed.

    Parameters
    ----------
    player : object
        The player object that interacts with the village area.

    map_layout : function
        The function that displays the map layout screen.

    Returns
    -------
    str
        The string that represents the next state of the game like the map or the shed.
    """

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
    special_area = pygame.Rect(822, 0, 80, 310)

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

        # don't let the player go into the lake or push the other pengus
        if player.rect.bottom <= 300:
            player.rect.bottom = 300

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
