from utils import *
from config import *
from interfaces_menus.button import Button, select_sound


def player_info_screen(player):
    """
    Display the player information screen where the player can see their stats and balance

    It renders a screen with:
    - Player's penguin image (depending on the player's penguin type) and text
    - Player's weapon image and text
    - Player's balance and coin image
    - Player's health cap and heart image
    - Player's speed cap and speed image
    - A back button to return to the main

    Parameters
    ----------
    player : object
        The player object that contains the player's balance and stats

    Returns
    -------
    None
        The function does not return anything. It exits on ESC key press or back button click.
    """

    pygame.init()
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    # load the background image
    background_image = pygame.image.load("images/chest_background.png")
    background_image = pygame.transform.scale(background_image, resolution)

    # load image to put the info on
    info_image = pygame.image.load("images/textbg.png")
    info_image = pygame.transform.scale(info_image, (600, 600))

    # font for text
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)
    small_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 20)

    # load and scale coin image and text
    coin_image = pygame.image.load("images/snowflake_coin.png")
    coin_image = pygame.transform.scale(coin_image, (40, 40))
    coin_text = pixel_font.render(f"Coins: {player.balance}", True, deep_black)

    # penguin image and text
    penguin_image = pygame.image.load(f"images_penguins/{player.ptype}up.png")
    penguin_image = pygame.transform.scale(penguin_image, (100, 100))
    penguin_text = pixel_font.render(f"This is you!", True, deep_black)
    penguin_text2 = small_font.render(f"And these are your stats!", True, deep_black)

    # weapon image and text
    weapon_image = pygame.image.load(f"images_weapons/{player.weapon}.png")
    weapon_image = pygame.transform.scale(weapon_image, (100, 100))
    weapon_text = pixel_font.render(f"Weapon: {player.weapon}", True, deep_black)

    # health image and text
    heart_image = pygame.image.load("images/heart.png")
    heart_image = pygame.transform.scale(heart_image, (40, 40))
    heart_text = pixel_font.render(f"Health Cap: {player.health_cap}", True, deep_black)

    # speed image and text
    speed_image = pygame.image.load("images/speed.png")
    speed_image = pygame.transform.scale(speed_image, (40, 40))
    speed_text = pixel_font.render(f"Speed Cap: {player.speed_cap}", True, deep_black)

    # set up the buttons
    back_button = Button(950, 600, 200, 100, "Back", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown,
                         image="images/Wood-button1.png")

    running = True
    while running:
        clock.tick(fps)
        screen.blit(background_image, (0, 0))

        # drawing the info image
        screen.blit(info_image, (200, 50))

        # getting the mouse position
        mouse = pygame.mouse.get_pos()

        # drawing the penguin image and text
        screen.blit(penguin_image, (250, 100))
        screen.blit(penguin_text, (370, 120))
        screen.blit(penguin_text2, (380, 170))

        # drawing the weapon image and text
        screen.blit(weapon_image, (222, 210))
        screen.blit(weapon_text, (350, 240))

        # drawing the coin image
        screen.blit(coin_image, (250, 310))
        screen.blit(coin_text, (350, 310))

        # drawing the heart image and text
        screen.blit(heart_image, (250, 380))
        screen.blit(heart_text, (350, 380))

        # drawing the speed image and text
        screen.blit(speed_image, (250, 450))
        screen.blit(speed_text, (350, 450))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return
            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            # putting visual effects on buttons
            for button in [back_button]:
                if button.is_hovered(pygame.mouse.get_pos()):
                    button.scale_up()
                else:
                    button.scale_down()

        # drawing the back button
        back_button.draw(screen, mouse)

        pygame.display.update()
