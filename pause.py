from interface import *

# creating the pause game button
def pause_screen(screen, resolution):
    # Load the pause button image
    icon_image = pygame.image.load('images/botton_pause.png')
    icon_image = pygame.transform.scale(icon_image, (50, 50))
    icon_position = (resolution[0] - icon_image.get_width() - 10, 10)

    # Load the pause background image
    background = pygame.image.load('images/pause__background.png')
    background = pygame.transform.scale(background, (700, 550))
    background_position = (resolution[0] - background.get_width() - 10, 10)

    # Loop to maintain the pause
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False # Exit the pause loop instead of quitting the game
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse clicks
                mouse_pos = pygame.mouse.get_pos()
                if (icon_position[0] <= mouse_pos[0] <= icon_position[0] + icon_image.get_width() and
                        icon_position[1] <= mouse_pos[1] <= icon_position[1] + icon_image.get_height()):
                    paused = False

        # Render the pause screen
        screen.blit(background, (300, 100))
        screen.blit(icon_image, icon_position)

        pygame.display.update()