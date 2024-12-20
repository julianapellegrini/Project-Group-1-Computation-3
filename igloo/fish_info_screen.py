# fish_info_screen.py
import pygame

from config import *
from interfaces_menus.button import Button, select_sound
from igloo.fishes import Salmon, Cod, ClownFish

def fish_info_screen():
    pygame.init()
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    # load the background image
    background_image = pygame.image.load("images/textbg.png")
    background_image = pygame.transform.scale(background_image, resolution)

    # Load fish images
    salmon_image = pygame.image.load("images/salmon.png")
    cod_image = pygame.image.load("images/cod.png")
    clownfish_image = pygame.image.load("images/clown_fish.png")

    # Scale fish images
    salmon_image = pygame.transform.scale(salmon_image, (100, 100))
    cod_image = pygame.transform.scale(cod_image, (100, 100))
    clownfish_image = pygame.transform.scale(clownfish_image, (100, 100))

    # Set up back button
    back_button = Button(950, 600, 200, 100, "Back", None, "fonts/Grand9KPixel.ttf", 45, True, bice_blue,
                         image="images/ice-banner.png")

    # Font for text
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)

    running = True
    while running:
        clock.tick(fps)
        screen.blit(background_image, (0, 0))

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