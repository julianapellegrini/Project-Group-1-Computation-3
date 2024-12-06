from utils import *
from config import *
from button import Button, select_sound
from igloo.fishes import Salmon, Cod, ClownFish
from player import Player
import random


def fishing(player):
    # setting up the background
    background = pygame.image.load("images/fishing_background.png")

    # scaling the background to resolution
    background = pygame.transform.scale(background, resolution)

    # setting up the screen
    screen = pygame.display.set_mode(resolution)

    # setting up the clock
    clock = pygame.time.Clock()

    # setting up the buttons
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")
    fish_button = Button(700, 200, 150, 60, "Fish", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")

    # game loop
    running = True
    while running:

        # setting the fps
        clock.tick(fps)

        # displaying the background
        screen.blit(background, (0, 0))

        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        # event handling
        for ev in pygame.event.get():

            # quit game
            if ev.type == pygame.QUIT:
                pygame.quit()

            # escape key returns
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            # back button returns
            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            # go to fishing minigame
            if fish_button.is_clicked(mouse, ev):
                select_sound()
                fishing_minigame(player)

        # drawing the buttons
        back_button.draw(screen, mouse)
        fish_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()


def fishing_minigame(player):

    # setting up the background
    background = pygame.image.load("images/fishing_background.png")

    # scaling the background to resolution
    background = pygame.transform.scale(background, resolution)

    # setting up the screen
    screen = pygame.display.set_mode(resolution)

    # setting up the clock
    clock = pygame.time.Clock()

    # hide the mouse cursor
    pygame.mouse.set_visible(False)

    # define the fish types
    fish_types = [Salmon, Cod, ClownFish]

    # progress of the fishing minigame
    progress = 0

    # setting the text font
    chiller_font = pygame.font.SysFont("chiller", 30)

    # set the progress text
    progress_text = chiller_font.render(f"{progress}%", True, white)

    # function to spawn a fish based on their probabilities
    def spawn_fish():
        fish_selected = random.choices(fish_types, [little_guy().probability for little_guy in fish_types])[0]
        return fish_selected()

    # select fish and add to fish group
    current_fish = spawn_fish()
    fish_group = pygame.sprite.Group(current_fish)

    # game loop
    running = True
    while running:

        # set game clock
        clock.tick(fps)

        # displaying the background
        screen.blit(background, (0, 0))

        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        # event handling
        for ev in pygame.event.get():

            # quit game
            if ev.type == pygame.QUIT:
                pygame.quit()

            # escape key returns and shows the mouse cursor again
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                pygame.mouse.set_visible(True)
                return

        # drawing the fishing minigame

        # drawing the fishing bar
        fishing_bar = draw_chasing_rectangle(screen, mouse, 30, 100, white, pink)

        # display the progress text after the chasing rectangle
        screen.blit(progress_text, (fishing_bar.right + 10, fishing_bar.centery - progress_text.get_height() // 2))

        # drawing the fish
        for fish in fish_group:

            # make the fish move
            fish.update_position()

            # draw the fish
            screen.blit(fish.image, fish.rect)

            # check if the fish is in the fishing bar and update the progress
            if fish.rect.colliderect(fishing_bar) and progress < 100:
                progress += 0.2
            elif progress > 0:
                progress -= 0.2

        # check if fish is caught and add to player's inventory
        if progress >= 100:
            # add the fish to the player's inventory
            player.add_item(current_fish)

            # reset progress after catching a fish
            progress = 0

            # spawn a new fish
            current_fish = spawn_fish()
            fish_group = pygame.sprite.Group(current_fish)

        # update the progress text
        progress_text = chiller_font.render(f"{int(progress)}%", True, white)

        # updating the display
        pygame.display.update()
