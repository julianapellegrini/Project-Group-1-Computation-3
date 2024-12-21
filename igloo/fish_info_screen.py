from utils import *
from config import *
from interfaces_menus.button import Button, select_sound
from igloo.fishes import Salmon, Cod, ClownFish


def fish_info_screen(player):
    pygame.init()
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    # load the background image
    background_image = pygame.image.load("images/textbg.png")
    background_image = pygame.transform.scale(background_image, resolution)

    # load and scale fish images at the top
    cod_image_small = pygame.image.load("images/cod.png")
    salmon_image_small = pygame.image.load("images/salmon.png")
    clownfish_image_small = pygame.image.load("images/clown_fish.png")

    cod_image_small = pygame.transform.scale(cod_image_small, (50, 50))
    salmon_image_small = pygame.transform.scale(salmon_image_small, (50, 50))
    clownfish_image_small = pygame.transform.scale(clownfish_image_small, (50, 50))

    # load and scale fish images in the main
    cod_image = pygame.image.load("images/cod.png")
    salmon_image = pygame.image.load("images/salmon.png")
    clownfish_image = pygame.image.load("images/clown_fish.png")

    cod_image = pygame.transform.scale(cod_image, (100, 100))
    salmon_image = pygame.transform.scale(salmon_image, (100, 100))
    clownfish_image = pygame.transform.scale(clownfish_image, (100, 100))

    # load and scale coin image
    coin_image = pygame.image.load("images/snowflake_coin.png")
    coin_image = pygame.transform.scale(coin_image, (40, 40))

    # set up back button
    back_button = Button(950, 600, 200, 100, "Back", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown,
                         image="images/Wood-button1.png")

    sell_cod_button = Button(900, 280, 200, 50, "SELL", royal_blue, "fonts/Grand9KPixel.ttf", 20, True, light_blue,
                             image="images/Wood-button1.png")

    sell_salmon_button = Button(900, 130, 200, 50, "SELL", royal_blue, "fonts/Grand9KPixel.ttf", 20, True,
                                light_blue, image="images/Wood-button1.png")

    sell_clownfish_button = Button(900, 430, 200, 50, "SELL", royal_blue, "fonts/Grand9KPixel.ttf", 20, True,
                                   light_blue, image="images/Wood-button1.png")

    # font for text
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)
    small_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 20)

    running = True
    while running:
        clock.tick(fps)
        screen.blit(background_image, (0, 0))

        # drawing small fish images and quantities at the top
        fishing_bucket_text = small_font.render("Fishing bucket:", True, oxford_blue)
        screen.blit(fishing_bucket_text, (50, 20))

        screen.blit(cod_image_small, (250, 10))
        screen.blit(salmon_image_small, (350, 10))
        screen.blit(clownfish_image_small, (450, 10))

        cod_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['Cod']}", True, oxford_blue)
        salmon_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['Salmon']}", True, oxford_blue)
        clownfish_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['ClownFish']}", True,
                                                    oxford_blue)

        screen.blit(cod_quantity_text, (310, 25))
        screen.blit(salmon_quantity_text, (410, 25))
        screen.blit(clownfish_quantity_text, (510, 25))

        # drawing fish images and text in middle
        screen.blit(cod_image, (100, 100))
        screen.blit(salmon_image, (100, 250))
        screen.blit(clownfish_image, (100, 400))

        cod_text = pixel_font.render("Cod: 5 for 10", True, oxford_blue)
        salmon_text = pixel_font.render("Salmon: 10 for 25", True, oxford_blue)
        clownfish_text = pixel_font.render("ClownFish: 15 for 40", True, oxford_blue)

        screen.blit(cod_text, (250, 130))
        screen.blit(salmon_text, (250, 280))
        screen.blit(clownfish_text, (250, 430))

        # drawing coin images next to the text
        screen.blit(coin_image, (450, 132))
        screen.blit(coin_image, (527, 282))
        screen.blit(coin_image, (573, 432))

        # getting the mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return
            if back_button.is_clicked(mouse, ev):
                select_sound()
                return
            if sell_cod_button.is_clicked(mouse, ev):
                if player.inventory.items['Fishes']['Cod'] >= 5:
                    player.inventory.items['Fishes']['Cod'] -= 5
                    player.balance += 10
            if sell_salmon_button.is_clicked(mouse, ev):
                if player.inventory.items['Fishes']['Salmon'] >= 10:
                    player.inventory.items['Fishes']['Salmon'] -= 10
                    player.balance += 25
            if sell_clownfish_button.is_clicked(mouse, ev):
                if player.inventory.items['Fishes']['ClownFish'] >= 15:
                    player.inventory.items['Fishes']['ClownFish'] -= 15
                    player.balance += 40

            # putting visual effects on buttons
            for button in [back_button, sell_cod_button, sell_salmon_button, sell_clownfish_button]:
                if button.is_hovered(pygame.mouse.get_pos()):
                    button.scale_up()
                else:
                    button.scale_down()

        # drawing the back button
        back_button.draw(screen, mouse)
        sell_cod_button.draw(screen, mouse)
        sell_salmon_button.draw(screen, mouse)
        sell_clownfish_button.draw(screen, mouse)

        pygame.display.update()
