from interface import *
from button import Button


# creating the pause game button
def pause_screen(screen, resolution):
    # Load the pause button image
    pause_button = Button(resolution[0] - 90, 10, 80, 80, "", None, None, 0, False, None, 'images/pause_button.png')

    # Load the play button image
    play_button = Button(resolution[0] // 4 - 60, resolution[1] // 2 - 60, 120, 120, "", None, None, 0, False, None,
                         'images/play_button.png')

    # Load the pause background image
    background = pygame.image.load('images/pause__background.png')
    background = pygame.transform.scale(background, resolution)

    # Loop to maintain the pause
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False  # Exit the pause loop instead of quitting the game
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse clicks
                mouse_pos = pygame.mouse.get_pos()
                if play_button.is_clicked(mouse_pos, event):  # Check if the play button is clicked
                    paused = False

        # Render the pause screen
        screen.blit(background, (0, 0))
        play_button.draw(screen, pygame.mouse.get_pos())

        pygame.display.update()
