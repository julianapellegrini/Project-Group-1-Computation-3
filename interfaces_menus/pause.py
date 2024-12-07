from interfaces_menus.interface import *
from interfaces_menus.button import Button


# creating the pause game button
def pause_screen(screen, resolution):

    # load the pause button image
    pause_button = Button(resolution[0] - 90, 10, 80, 80, "", None, None, 0, False, None, 'images/pause_button.png')

    # load the play button image
    play_button = Button(resolution[0] // 4 - 60, resolution[1] // 2 - 60, 140, 140, "", None, None, 0, False, None,
                         'images/play_button.png')

    # load the setting button image
    setting_button = Button(resolution[0] // 2.5 - 60, resolution[1] // 2 - 60, 140, 140, "", None, None, 0, False, None,
                            'images/setting_button.png')

    # load the igloo button image
    igloo_button = Button(resolution[0] // 1.8 - 60, resolution[1] // 2 - 60, 142, 142, "", None, None, 0, False, None,
                          'images/igloo_wood_button.png')

    # load the map button image
    map_button = Button(resolution[0] // 1.4 - 60, resolution[1] // 2 - 60, 140, 140, "", None, None, 0, False, None,
                        'images/map_button.png')

    # load the pause background image
    background = pygame.image.load('images/pause__background.png')
    background = pygame.transform.scale(background, resolution)

    # main loop to maintain the pause
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False  # exit the pause loop instead of quitting the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.is_clicked(mouse_pos, event):
                    paused = False
                elif setting_button.is_clicked(mouse_pos, event):
                    print("Settings menu")
                elif igloo_button.is_clicked(mouse_pos, event):
                    print("Igloo")
                elif map_button.is_clicked(mouse_pos, event):
                    print("Map")

        # Render the pause screen
        screen.blit(background, (0, 0))
        play_button.draw(screen, pygame.mouse.get_pos())
        setting_button.draw(screen, pygame.mouse.get_pos())
        igloo_button.draw(screen, pygame.mouse.get_pos())
        map_button.draw(screen, pygame.mouse.get_pos())

        pygame.display.update()
