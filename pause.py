from interface import *

# creating the pause game button
def pause_screen(screen, resolution):
    # Load the pause button image
    icon_image = pygame.image.load('images/pause_button.png')
    icon_image = pygame.transform.scale(icon_image, (80, 80))
    icon_position = (resolution[0] - icon_image.get_width() - 10, 10)

    # Load the play button image
    play_image = pygame.image.load('images/play_button.png')
    play_image = pygame.transform.scale(play_image, (120, 120))
    play_position = (resolution[0] // 4 - play_image.get_width() // 2, resolution[1] // 2 - play_image.get_height() // 2)

    # Load the pause background image
    background = pygame.image.load('images/pause__background.png')
    background = pygame.transform.scale(background, resolution)

    # Loop to maintain the pause
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False # Exit the pause loop instead of quitting the game
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse clicks
                mouse_pos = pygame.mouse.get_pos()
                if (play_position[0] <= mouse_pos[0] <= play_position[0] + play_image.get_width() and
                        play_position[1] <= mouse_pos[1] <= play_position[1] + play_image.get_height()):
                    paused = False

        # Render the pause screen
        screen.blit(background, (0, 0))
        screen.blit(play_image, play_position)

        pygame.display.update()