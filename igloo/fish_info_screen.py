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
    salmon_image_small = pygame.image.load("images/salmon.png")
    cod_image_small = pygame.image.load("images/cod.png")
    clownfish_image_small = pygame.image.load("images/clown_fish.png")

    salmon_image_small = pygame.transform.scale(salmon_image_small, (50, 50))
    cod_image_small = pygame.transform.scale(cod_image_small, (50, 50))
    clownfish_image_small = pygame.transform.scale(clownfish_image_small, (50, 50))

    # load and scale fish images in the main
    salmon_image = pygame.image.load("images/salmon.png")
    cod_image = pygame.image.load("images/cod.png")
    clownfish_image = pygame.image.load("images/clown_fish.png")

    salmon_image = pygame.transform.scale(salmon_image, (100, 100))
    cod_image = pygame.transform.scale(cod_image, (100, 100))
    clownfish_image = pygame.transform.scale(clownfish_image, (100, 100))

    # load and scale coin image
    coin_image = pygame.image.load("images/snowflake_coin.png")
    coin_image = pygame.transform.scale(coin_image, (40, 40))

    # set up back button
    back_button = Button(950, 600, 200, 100, "Back", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown,
                         image="images/Wood-button1.png")

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

        screen.blit(salmon_image_small, (250, 10))
        screen.blit(cod_image_small, (350, 10))
        screen.blit(clownfish_image_small, (450, 10))

        salmon_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['Salmon']}", True, oxford_blue)
        cod_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['Cod']}", True, oxford_blue)
        clownfish_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['ClownFish']}", True,
                                                    oxford_blue)

        screen.blit(salmon_quantity_text, (310, 25))
        screen.blit(cod_quantity_text, (410, 25))
        screen.blit(clownfish_quantity_text, (510, 25))

        # drawing fish images and text in middle
        screen.blit(salmon_image, (100, 100))
        screen.blit(cod_image, (100, 250))
        screen.blit(clownfish_image, (100, 400))

        salmon_text = pixel_font.render("Salmon: 10 for 25", True, oxford_blue)
        cod_text = pixel_font.render("Cod: 5 for 10", True, oxford_blue)
        clownfish_text = pixel_font.render("ClownFish: 15 for 40", True, oxford_blue)

        screen.blit(salmon_text, (250, 130))
        screen.blit(cod_text, (250, 280))
        screen.blit(clownfish_text, (250, 430))

        # drawing coin images next to the text
        screen.blit(coin_image, (540, 135))
        screen.blit(coin_image, (450, 280))
        screen.blit(coin_image, (579, 447))

        # getting the mouse position
        mouse = pygame.mouse.get_pos()
        print(mouse)

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
            if back_button.is_hovered(pygame.mouse.get_pos()):
                back_button.scale_up()
            else:
                back_button.scale_down()

        # drawing the back button
        back_button.draw(screen, mouse)

        pygame.display.update()
