from utils import *
from config import *
from interfaces_menus.button import Button, select_sound
from igloo.fishes import Salmon, Cod, ClownFish
import random


def fishing(player):
    """
    Display the fishing screen where the player can fish for different types of fish.

    Parameters
    ----------
    player : object
        The player object that interacts with the fishing minigame and updates the player's inventory.

    Returns
    -------
    None
        The function does not return anything. It exits on ESC key press or back button click.
    """

    # setting up the background
    background = pygame.image.load("images/fishing_background.png")

    # scaling the background to resolution
    background = pygame.transform.scale(background, resolution)

    # setting up the screen
    screen = pygame.display.set_mode(resolution)

    # setting up the clock
    clock = pygame.time.Clock()

    # setting up the buttons
    back_button = Button(1000, 650, 150, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 35, True, light_brown,
                         image="images/Wood-button1.png")
    fish_button = Button(700, 200, 150, 60, "Fish", brown, "fonts/Grand9KPixel.ttf", 35, True, light_brown,
                         image="images/Wood-button1.png")

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

        # putting visual effects to buttons
        for button in [back_button, fish_button]:
            if button.is_hovered(mouse):
                button.scale_up()
            else:
                button.scale_down()

        # drawing the buttons
        back_button.draw(screen, mouse)
        fish_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()


def fishing_minigame(player):
    """
    Display the fishing minigame where the player can catch fish by moving a fishing bar.

    Parameters
    ----------
    player : object
        The player object that interacts with the fishing minigame catching fish and adding them to the inventory.

    Returns
    -------
    None
        The function does not return anything. It exits on ESC key press.
    """

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

    # instruction text and font
    instruction_font = pygame.font.SysFont("fonts/Grand9KPixel.ttf", 40)
    instruction_text = instruction_font.render("Catch the fish in the fishing bar!", True, oxford_blue)
    instruction_text2 = instruction_font.render("Press ESC to return", True, oxford_blue)

    # define the fish types
    fish_types = [Salmon, Cod, ClownFish]

    # progress of the fishing minigame
    progress = 0

    # setting the text font
    pixel_font = pygame.font.SysFont("fonts/Grand9KPixel.ttf", 30)

    # set the progress text
    progress_text = pixel_font.render(f"{progress}%", True, white)

    # function to spawn a fish based on their probabilities
    def spawn_fish():
        """
        Spawns a fish based on their probabilities.

        Returns
        -------
        fish : object
            The fish object that is spawned.
        """
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

        # display the instruction text
        screen.blit(instruction_text, (100, 20))
        screen.blit(instruction_text2, (185, 70))

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

        # check if fish is caught and add to player_related's inventory
        if progress >= 100:
            # add the fish to the player_related's inventory
            player.add_fish(current_fish)

            # reset progress after catching a fish
            progress = 0

            # spawn a new fish
            current_fish = spawn_fish()
            fish_group = pygame.sprite.Group(current_fish)

        # update the progress text
        progress_text = pixel_font.render(f"{int(progress)}%", True, white)

        # updating the display
        pygame.display.update()
