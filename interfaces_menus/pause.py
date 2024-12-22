from interfaces_menus.button import Button, select_sound
from igloo.village import area
from config import *


# creating the pause game button
def pause_screen(screen, resolution, player, map_layout, interface_w_save, interface_no_save):

    """
    Displays the pause screen.

    This function sets up a Pygame window with the pause menu, including buttons for resuming the game, accessing settings, returning to the map, and quitting.

    Parameters:
    -----------
    screen : pygame.Surface
        The Pygame display surface.
    resolution : tuple
        The resolution of the game window.
    player : object
        The player object.
    map_layout : function
        The function to call to display the map layout.
    interface_w_save : function
        The function to call if a save file is present.
    interface_no_save : function
        The function to call if no save file is present.
    """
    
    from interfaces_menus.interface import settings

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
    background1 = pygame.image.load("images/ice-background2.png")
    background1 = pygame.transform.scale(background1, (width, height))

    background = pygame.image.load('images/smaller_box.png')
    background = pygame.transform.scale(background, (750, 200))
    background_rect = background.get_rect(center=(resolution[0] // 2, (resolution[1] // 2) + 15))

    # create the confirmation buttons
    yes_button = Button(resolution[0] // 2.5 - 100, resolution[1] // 2, 150, 60, "Yes", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown, 'images/Wood-button1.png')
    no_button = Button(resolution[0] // 2.2 + 100, resolution[1] // 2, 150, 60, "No", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown, 'images/Wood-button1.png')

    # set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)

    # create confirmation text
    text = pixel_font.render("Are you sure you want to quit?", True, brown)

    # main loop to maintain the pause
    paused = True
    confirming = False
    action = None
    while paused:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if confirming:
                    if yes_button.is_clicked(mouse_pos, ev):
                        select_sound()
                        if action == "map":
                            map_layout(player, interface_w_save, interface_no_save)
                        elif action == "igloo":
                            area(player, map_layout, interface_w_save, interface_no_save)
                        return
                    elif no_button.is_clicked(mouse_pos, ev):
                        select_sound()
                        confirming = False
                        action = None
                else:
                    if play_button.is_clicked(mouse_pos, ev):
                        select_sound()
                        paused = False
                    elif setting_button.is_clicked(mouse_pos, ev):
                        select_sound()
                        settings(player)
                    elif igloo_button.is_clicked(mouse_pos, ev):
                        select_sound()
                        confirming = True
                        action = "igloo"
                    elif map_button.is_clicked(mouse_pos, ev):
                        select_sound()
                        confirming = True
                        action = "map"

        # render the pause screen
        screen.blit(background1, (0, 0))
        screen.blit(background, background_rect)

        if confirming:
            # draw the confirmation text and buttons
            text_rect = text.get_rect(center=(resolution[0] // 2, resolution[1] // 2 - 50))
            screen.blit(text, text_rect)
            yes_button.draw(screen, pygame.mouse.get_pos())
            no_button.draw(screen, pygame.mouse.get_pos())
        else:
            # draw the other buttons in the main pause screen
            for button in [play_button, setting_button, igloo_button, map_button]:
                button.draw(screen, pygame.mouse.get_pos())

        # putting visual effects on buttons
        for button in [play_button, setting_button, igloo_button, map_button, yes_button, no_button]:
            if button.is_hovered(pygame.mouse.get_pos()):
                button.scale_up()
            else:
                button.scale_down()

        pygame.display.update()
