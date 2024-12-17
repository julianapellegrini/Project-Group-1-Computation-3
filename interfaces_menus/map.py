from interfaces_menus.choose_interface import choose_interface
from interfaces_menus.button import Button, select_sound
from interfaces_menus.confirm_screen import confirm
from game import game_loop
from igloo.village import area
import pygame
from config import *
from interfaces_menus.levels import Level

def map_layout(player, interface_w_save, interface_no_save):
    # initializing pygame
    pygame.init()

    pygame.mixer.music.load("audio/nocturne-of-ice.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # path for the images of the buttons
    button_sprite = "images/ice-banner.png"
    igloo_sprite = "images/igloo_button.png"

    # setting up the back button
    back_button = Button(950, 600, 150, 60, "Back", None, "fonts/Grand9KPixel.ttf", 20, True, bice_blue,
                         image=button_sprite)

    # setting up the igloo button
    igloo_button = Button(990, 0, 190, 190, None, None, None, 35, False, None,
                          image=igloo_sprite)

    # creating level buttons
    level_buttons = [
        Level(1, 50, 250, 100, 100, royal_blue, "images/level-button.png"),
        Level(2, 225, 175, 100, 100, royal_blue, "images/level-button.png"),
        Level(3, 520, 310, 100, 100, royal_blue, "images/level-button.png"),
        Level(4, 830, 200, 100, 100, royal_blue, "images/level-button.png"),
        Level(5, 610, 30, 100, 100, royal_blue, "images/level-button.png")
        ]

    while True:
        # displaying the screen
        background = pygame.image.load('images/map_layout.png')
        background = pygame.transform.scale(background, (resolution[0], resolution[1]))
        screen.blit(background, (0, 0))

        # get mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            if back_button.is_clicked(mouse, ev):
                select_sound()
                if confirm():
                    choose_interface(player, interface_w_save, interface_no_save)

            if igloo_button.is_clicked(mouse, ev):
                select_sound()
                area(player, map_layout, interface_w_save, interface_no_save)

            # check if any level button is clicked by iterating through them rather than creating 1908393 if cases
            for i, level_button in enumerate(level_buttons):
                if level_button.is_clicked(mouse, ev):
                    select_sound()
                    # pass the level number and player_related instance to game_loop
                    game_loop(level=i + 1, player=player, map_layout=map_layout, interface_w_save=interface_w_save,
                              interface_no_save=interface_no_save)

        # update button visuals
        for level_button in level_buttons:
            if level_button.is_hovered(mouse):
                level_button.scale_up()
            else:
                level_button.scale_down()

        if back_button.is_hovered(mouse):
            back_button.scale_up()
        else:
            back_button.scale_down()

        if igloo_button.is_hovered(mouse):
            igloo_button.scale_up()
        else:
            igloo_button.scale_down()

        # draw all buttons
        for level_button in level_buttons:
            level_button.draw(screen, mouse)

        back_button.draw(screen, mouse)
        igloo_button.draw(screen, mouse)

        # update the display
        pygame.display.update()
