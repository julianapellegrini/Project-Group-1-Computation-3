from utils import *
from config import *
from button import Button, select_sound


def weapon_selector():

    # set background
    background = pygame.image.load("../images/weapon_selector.png")
    # scale background
    background = pygame.transform.scale(background, resolution)

    # set screen
    screen = pygame.display.set_mode(resolution)

    # set clock
    clock = pygame.time.Clock()

    # set buttons
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")
    select_button = Button(1000, 550, 150, 60, "Select", None, "chiller", 35, True, bice_blue,
                           image="images/ice-banner.png")


