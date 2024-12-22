from config import *
from utils import *
from interfaces_menus.button import Button, select_sound
from igloo.shop import shop_layout
from igloo.fishing import fishing
from save_system.SaveLoadGame import SaveManager
from igloo.weapon_selector import weapon_selector
from igloo.skin_selector import skin_selector
from igloo.player_screen import player_info_screen


def shed(player):
    """
    Display the shed screen where the player can access different features of the game like the shop, skins, weapons,
    fishing hole, save game, and player info.

    Parameters
    ----------
    player : object
        The player object that interacts with the shed screen and the features it provides.

    Returns
    -------
    None
        The function does not return anything. It exits on ESC key press or back button click and responds to the
        on-screen actions.
    """
    # setting up the background and the screen
    background = pygame.image.load("images/igloo_bar.png")

    # scaling the background image into our selected resolution
    background = pygame.transform.scale(background, resolution)

    # setting up the screen
    screen = pygame.display.set_mode(resolution)

    # setting up the clock for fps
    clock = pygame.time.Clock()

    # set save manager
    save_manager = SaveManager()

    # setting up the buttons
    back_button = Button(1000, 650, 150, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")

    shop_button = Button(580, 240, 100, 60, "Shop", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")

    skin_button = Button(50, 310, 150, 60, "Skins", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")

    fish_button = Button(830, 250, 150, 60, "Fishing Hole", brown, "fonts/Grand9KPixel.ttf", 18, True, light_brown,
                         image="images/Wood-button1.png")

    weapons_button = Button(50, 380, 150, 60, "Weapons", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                            image="images/Wood-button1.png")

    save_game_button = Button(270, 190, 150, 60, "Save Game", brown, "fonts/Grand9KPixel.ttf", 18, True, light_brown,
                              image="images/Wood-button1.png")

    player_info_button = Button(270, 120, 150, 60, "Player Info", brown, "fonts/Grand9KPixel.ttf", 18, True,
                                light_brown, image="images/Wood-button1.png")

    running = True

    while running:
        clock.tick(fps)
        # displaying the background on the entirety of the screen
        screen.blit(background, (0, 0))

        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            if shop_button.is_clicked(mouse, ev):
                select_sound()
                shop_layout(player)

            if skin_button.is_clicked(mouse, ev):
                select_sound()
                skin_selector(player)

            if fish_button.is_clicked(mouse, ev):
                select_sound()
                fishing(player)

            if weapons_button.is_clicked(mouse, ev):
                select_sound()
                weapon_selector(player)

            if save_game_button.is_clicked(mouse, ev):
                select_sound()
                save_manager.save_game(player)
                print(player.inventory.items, player.balance, player.weapon, player.level)

            if player_info_button.is_clicked(mouse, ev):
                select_sound()
                player_info_screen(player)

            # clear the button's previous position
            previous_rect = pygame.Rect(back_button.x, back_button.y, back_button.width, back_button.height)
            screen.blit(background, previous_rect, previous_rect)  # clear the previous area

            # update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            if shop_button.is_hovered(mouse):
                shop_button.scale_up()
            else:
                shop_button.scale_down()

            if skin_button.is_hovered(mouse):
                skin_button.scale_up()
            else:
                skin_button.scale_down()

            if fish_button.is_hovered(mouse):
                fish_button.scale_up()
            else:
                fish_button.scale_down()

            if weapons_button.is_hovered(mouse):
                weapons_button.scale_up()
            else:
                weapons_button.scale_down()

            if save_game_button.is_hovered(mouse):
                save_game_button.scale_up()
            else:
                save_game_button.scale_down()

            if player_info_button.is_hovered(mouse):
                player_info_button.scale_up()
            else:
                player_info_button.scale_down()

            # draw the buttons after updating
            back_button.draw(screen, mouse)
            skin_button.draw(screen, mouse)
            shop_button.draw(screen, mouse)
            fish_button.draw(screen, mouse)
            weapons_button.draw(screen, mouse)
            save_game_button.draw(screen, mouse)
            player_info_button.draw(screen, mouse)

        # drawing the buttons
        back_button.draw(screen, mouse)
        skin_button.draw(screen, mouse)
        shop_button.draw(screen, mouse)
        fish_button.draw(screen, mouse)
        weapons_button.draw(screen, mouse)
        save_game_button.draw(screen, mouse)
        player_info_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()
