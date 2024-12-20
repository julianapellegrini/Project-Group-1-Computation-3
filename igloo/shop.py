from interfaces_menus.interface import *
from interfaces_menus.button import Button, select_sound
import coin_tracker


def shop_layout():

    # initializing pygame
    pygame.init()

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # setting up the back button
    back_button = Button(950, 600, 200, 100, "Back", None, "fonts/Grand9KPixel.ttf", 45, True, bice_blue,
                         image="images/ice-banner.png")

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

        # Showing the text of total coins
        total_coins_text = pixel_font.render(f"{coin_tracker.get_total_coins()}", True, oxford_blue)
        screen.blit(total_coins_text, (630, 312))

        # get player_related's mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            # clear the button's previous position
            previous_rect = pygame.Rect(back_button.x, back_button.y, back_button.width, back_button.height)
            # clear the previous area
            screen.blit(background, previous_rect, previous_rect)

            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            # draw the button after updating
            back_button.draw(screen, mouse)

        # drawing the back button
        back_button.draw(screen, mouse)

        # update the display
        pygame.display.update()
