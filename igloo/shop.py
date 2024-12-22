from igloo.fish_info_screen import fish_info_screen
from igloo.improve_combat_shop import improve_combat_screen
from igloo.weapon_shop import weapon_shop
from interfaces_menus.interface import *
from interfaces_menus.button import Button, select_sound


def shop_layout(player):
    """
    Display the shop layout screen where the player can access different screens to buy weapons, improve weapons, and
    sell fish for coins. Coin balance is displayed on the screen.

    Parameters
    ----------
    player : object
        The player object that contains the player's balance, weapons, update progress, and inventory.

    Returns
    -------
    None
        The function does not return anything. It exits on ESC key press or back button click and responds to the
        on-screen actions.
    """

    # initializing pygame
    pygame.init()

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # setting up buttons
    back_button = Button(950, 600, 200, 100, "Back", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown,
                         image="images/Wood-button1.png")

    fish_info_button = Button(338, 434, 100, 100, "", None, "fonts/Grand9KPixel.ttf", 45, True, bice_blue,
                              image="images_shop/packet_fishes.png")

    weapon_button = Button(830, 320, 100, 100, "", None, "fonts/Grand9KPixel.ttf", 45, True, bice_blue,
                           image="images_shop/icon_weapon.png")

    improve_combat_button = Button(331, 310, 100, 100, "", None, "fonts/Grand9KPixel.ttf", 45, True, bice_blue,
                           image="images_shop/combat_improvements.png")

    # load coin image
    coin_image = pygame.image.load("images/snowflake_coin.png")
    coin_image = pygame.transform.scale(coin_image, (90, 90))

    # font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 50)

    while True:

        # displaying the screen
        background = pygame.image.load('images/shop_layout.png')

        # scale the background to the resolution
        background = pygame.transform.scale(background, (resolution[0], resolution[1]))

        # display the background
        screen.blit(background, (0, 0))

        # draw the coin image
        screen.blit(coin_image, (505, 310))

        # showing the text of total coins
        total_coins_text = pixel_font.render(f"{player.balance}", True, oxford_blue)
        screen.blit(total_coins_text, (630, 312))

        # get player's mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return
            if fish_info_button.is_clicked(mouse, ev):
                select_sound()
                fish_info_screen(player)
            if weapon_button.is_clicked(mouse, ev):
                select_sound()
                weapon_shop(player)
            if improve_combat_button.is_clicked(mouse, ev):
                select_sound()
                improve_combat_screen(player)

            # clear the button's previous position
            previous_rect = pygame.Rect(back_button.x, back_button.y, back_button.width, back_button.height)
            # clear the previous area
            screen.blit(background, previous_rect, previous_rect)

            # putting visual effects on buttons
            for button in [back_button, fish_info_button, weapon_button, improve_combat_button]:
                if button.is_hovered(pygame.mouse.get_pos()):
                    button.scale_up()
                else:
                    button.scale_down()

            # draw the button after updating
            back_button.draw(screen, mouse)

        # drawing buttons
        back_button.draw(screen, mouse)
        fish_info_button.draw(screen, mouse)
        weapon_button.draw(screen, mouse)
        improve_combat_button.draw(screen, mouse)

        # update the display
        pygame.display.update()
