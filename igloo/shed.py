from config import *
from utils import *
from interfaces_menus.button import Button, select_sound
from utils import under_construction
from igloo.shop import shop_layout
from igloo.fishing import fishing
from save_system.SaveLoadGame import SaveManager
from igloo.weapon_selector import weapon_selector


def shed(player):
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
    back_button = Button(1000, 650, 150, 60, "Back", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                         image="images/ice-banner.png")

    shop_button = Button(460, 370, 150, 60, "Shop", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                         image="images/ice-banner.png")

    table_button = Button(750, 600, 150, 60, "Skins", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                          image="images/ice-banner.png")

    fish_button = Button(700, 200, 150, 60, "Fishing Hole", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                         image="images/ice-banner.png")

    weapons_button = Button(850, 455, 150, 60, "Weapons", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                            image="images/ice-banner.png")

    save_game_button = Button(662, 364, 150, 60, "Save Game", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                              image="images/ice-banner.png")

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
                shop_layout()

            if table_button.is_clicked(mouse, ev):
                select_sound()
                under_construction()

            if fish_button.is_clicked(mouse, ev):
                select_sound()
                fishing(player)

            if weapons_button.is_clicked(mouse, ev):
                select_sound()
                weapon_selector()

            if save_game_button.is_clicked(mouse, ev):
                select_sound()
                save_manager.save_game(player)
                print(player.inventory.items)

            # clear the button's previous position
            previous_rect = pygame.Rect(back_button.x, back_button.y, back_button.width, back_button.height)
            screen.blit(background, previous_rect, previous_rect)  # Clear the previous area

            # update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            if shop_button.is_hovered(mouse):
                shop_button.scale_up()
            else:
                shop_button.scale_down()

            if table_button.is_hovered(mouse):
                table_button.scale_up()
            else:
                table_button.scale_down()

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

            # draw the buttons after updating
            back_button.draw(screen, mouse)
            table_button.draw(screen, mouse)
            shop_button.draw(screen, mouse)
            fish_button.draw(screen, mouse)
            weapons_button.draw(screen, mouse)
            save_game_button.draw(screen, mouse)

        # drawing the buttons
        back_button.draw(screen, mouse)
        table_button.draw(screen, mouse)
        shop_button.draw(screen, mouse)
        fish_button.draw(screen, mouse)
        weapons_button.draw(screen, mouse)
        save_game_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()
