from utils import *
from config import *
from button import Button, select_sound
from fishes import Salmon, Cod
import random


def fishing():
    # setting up the background and the screen
    background = pygame.image.load("images/fishing_background.png")

    # scaling the background image into our selected resolution
    background = pygame.transform.scale(background, resolution)

    # setting up the screen
    screen = pygame.display.set_mode(resolution)

    # setting up the clock for fps
    clock = pygame.time.Clock()

    # setting up the buttons
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")
    fish_button = Button(700, 200, 150, 60, "Fish", None, "chiller", 35, True, bice_blue,
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

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            if fish_button.is_clicked(mouse, ev):
                select_sound()
                fishing_minigame()

        # drawing the buttons
        back_button.draw(screen, mouse)
        fish_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()


def fishing_minigame():
    # setting up the background and the screen
    background = pygame.image.load("images/fishing_background.png")

    # scaling the background image into our selected resolution
    background = pygame.transform.scale(background, resolution)

    # setting up the screen
    screen = pygame.display.set_mode(resolution)

    # setting up the clock for fps
    clock = pygame.time.Clock()

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Define the fish types
    fish_types = [Salmon, Cod]

    # Function to spawn a fish based on probabilities
    def spawn_fish():
        fish_selected = random.choices(fish_types, [little_guy().probability for little_guy in fish_types])[0]
        return fish_selected()

    # Create the fish
    current_fish = spawn_fish()
    fish_group = pygame.sprite.Group(current_fish)

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
                pygame.mouse.set_visible(True)
                return  # return to the fishing screen

        # drawing the fishing minigame

        # drawing the fishing bar
        draw_chasing_rectangle(screen, mouse, 30, 100, white, pink)

        # drawing the fish
        for fish in fish_group:
            fish.update_position()
            screen.blit(fish.image, fish.rect)

        # updating the display
        pygame.display.update()
