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

    # set up back button
    back_button = Button(950, 600, 200, 100, "Back", None, "fonts/Grand9KPixel.ttf", 45, True, bice_blue,
                         image="images/ice-banner.png")

    # font for text
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)
    small_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 20)

    running = True
    while running:
        clock.tick(fps)
        screen.blit(background_image, (0, 0))

        # draw small fish images and quantities at the top
        screen.blit(salmon_image_small, (50, 10))
        screen.blit(cod_image_small, (150, 10))
        screen.blit(clownfish_image_small, (250, 10))

        salmon_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['Salmon']}", True, oxford_blue)
        cod_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['Cod']}", True, oxford_blue)
        clownfish_quantity_text = small_font.render(f"{player.inventory.items['Fishes']['ClownFish']}", True,
                                                    oxford_blue)

        screen.blit(salmon_quantity_text, (110, 25))
        screen.blit(cod_quantity_text, (210, 25))
        screen.blit(clownfish_quantity_text, (310, 25))

        # Draw fish images and text
        screen.blit(salmon_image, (100, 100))
        screen.blit(cod_image, (100, 250))
        screen.blit(clownfish_image, (100, 400))

        salmon_text = pixel_font.render("Salmon: 10 needed for 5 coins", True, oxford_blue)
        cod_text = pixel_font.render("Cod: 5 needed for 3 coins", True, oxford_blue)
        clownfish_text = pixel_font.render("ClownFish: 15 needed for 10 coins", True, oxford_blue)

        screen.blit(salmon_text, (250, 130))
        screen.blit(cod_text, (250, 280))
        screen.blit(clownfish_text, (250, 430))

        # Get mouse position
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

        # Draw back button
        back_button.draw(screen, mouse)

        pygame.display.update()
