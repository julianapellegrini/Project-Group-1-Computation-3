from interfaces_menus.interface import *
from interfaces_menus.button import Button, select_sound
from utils import under_construction
from igloo.shed import shed

# creating the pause game button
def pause_screen(screen, resolution, player):

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
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.is_clicked(mouse_pos, ev):
                    select_sound()
                    paused = False
                elif setting_button.is_clicked(mouse_pos, ev):
                    select_sound()
                    under_construction()
                elif igloo_button.is_clicked(mouse_pos, ev):
                    select_sound()
                    shed(player)
                elif map_button.is_clicked(mouse_pos, ev):
                    select_sound()
                    from interfaces_menus.map import map_layout
                    map_layout(player)

        # putting visual effects on buttons
        for button in [play_button, setting_button, igloo_button, map_button]:
            if button.is_hovered(pygame.mouse.get_pos()):
                button.scale_up()
            else:
                button.scale_down()

        # render the pause screen
        screen.blit(background, (0, 0))
        for button in [play_button, setting_button, igloo_button, map_button]:
            button.draw(screen, pygame.mouse.get_pos())

        pygame.display.update()
