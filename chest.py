import pygame
import random
from powerups.despawner import DeSpawner
from powerups.invincibility import Invincibility
from powerups.extra_fish import Extra_Fish
from powerups.speed_boost import Speed_Boost
import numpy as np


# create a chest class
class Chest(pygame.sprite.Sprite):

    """
    Represents a chest that can spawn in the game and offer random powerups or upgrades to the player.

    Attributes
    ----------
    image : pygame.Surface
        The visual representation of the chest.
    rect : pygame.Rect
        The rectangle defining the chest's position and size.
    spawned : bool
        Indicates whether the chest is currently spawned on the surface.
    possible_items : dict
        A dictionary mapping item names to their spawn probabilities.
    options : list of str
        The selected options to be presented when the chest is opened.
    upgrades : list of str
        Items that permanently upgrade player attributes.
    powerups : list of str
        Temporary powerups affecting gameplay.
    """

    def __init__(self):

        """
        Initializes the Chest with an image, position, and possible items.
        """

        super().__init__()
        self.image = pygame.image.load("images/chest_image.png")  # load the image
        self.image = pygame.transform.scale(self.image, (150, 150))  # scale the image
        self.rect = self.image.get_rect()

        self.spawned = False

        # dictionary of possible items and their probabilities
        self.possible_items = {
            "Despawner": 0.25,
            "Invincibility": 0.2,
            "Extra Fish": 0.10,
            "Speed Boost": 0.15,
            "Permanent Speed Boost": 0.2,
            "Permanent Health Boost": 0.1
        }

        # list of options and their types
        self.options = []
        self.upgrades = ["Permanent Health Boost", "Permanent Speed Boost"]
        self.powerups = ["Despawner", "Invincibility", "Extra Fish", "Speed Boost"]

    def spawn(self, surface):

        """
        Spawns the chest at a random position within the boundaries of the given surface.

        Parameters
        ----------
        surface : pygame.Surface
            The surface where the chest should be spawned.
        """

        # check if chest is not already spawned and spawn it
        if not self.spawned:
            # define map boundaries
            map_width, map_height = surface.get_size()

            # generate random position within boundaries
            random_x = random.randint(0, map_width - self.rect.width)
            random_y = random.randint(0, map_height - self.rect.height)

            # set the rect position to the random coordinates
            self.rect.topleft = (random_x, random_y)

            # set spawned to True
            self.spawned = True

            print(f"Chest spawned at {self.rect.topleft}")

        # draw the chest
        surface.blit(self.image, self.rect.topleft)

    def select_options(self):

        """
        Randomly selects three distinct options from the possible items based on their probabilities.
        """

        # separate the items and probabilities to then choose the items based on their probabilities
        items = list(self.possible_items.keys())
        probabilities = list(self.possible_items.values())
        # using numpy random choice to choose the items based on their probabilities and also to be all different
        self.options = list(np.random.choice(items, size=3, replace=False, p=probabilities))
        print(f"Selected options: {self.options}")

    def display_options(self, surface, enemies, spawn_chances, player):
        
        """
        Displays the selected options on the screen and allows the player to choose one.

        Parameters
        ----------
        surface : pygame.Surface
            The surface where the options will be displayed.
        enemies : list
            The list of enemies in the game.
        spawn_chances : dict
            The spawn chances of various game elements.
        player : object
            The player object to apply upgrades or powerups.
        """

        # pause the game
        paused = True

        # create a semi-transparent overlay
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Black with 50% opacity

        # display the overlay
        surface.blit(overlay, (0, 0))

        # instructions for the player to skip
        pixel_font_small = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)
        instruction_text = pixel_font_small.render("Press ENTER to skip", True, (255, 255, 255))

        # display the instructions in the top right corner
        surface.blit(instruction_text, (surface.get_width() - 400, 20))

        # define dimensions for options images and their positions
        option_width = 150
        option_height = 150
        padding = 100  # Increased padding for better spacing
        total_width = len(self.options) * (option_width + padding) - padding
        start_x = (surface.get_width() - total_width) // 2
        y_position = (surface.get_height() - option_height) // 2 - 50  # Offset upward for names

        # load and display the options as images
        option_images = []
        for option in self.options:
            image_path = f"chest_option_images/{option.lower().replace(' ', '_')}.png"  # example image naming convention
            option_image = pygame.image.load(image_path).convert_alpha()
            option_image = pygame.transform.scale(option_image, (option_width, option_height))
            option_images.append(option_image)

        # get option rects and display the options
        option_rects = []
        font = pygame.font.Font(None, 36)
        for i, (option_image, option) in enumerate(zip(option_images, self.options)):
            # calculate x position for this option
            x_position = start_x + i * (option_width + padding)

            # draw the option image
            surface.blit(option_image, (x_position, y_position))

            # draw the option name below the image
            text = font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(center=(x_position + option_width // 2, y_position + option_height + 20))
            surface.blit(text, text_rect)

            # save the clickable area (the image)
            option_rects.append(pygame.Rect(x_position, y_position, option_width, option_height))

        # update the display
        pygame.display.flip()

        # wait for the player to select an item
        while paused:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # press Enter to continue without selecting
                        paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left mouse button
                        mouse_pos = event.pos
                        for rect, option in zip(option_rects, self.options):
                            if rect.collidepoint(mouse_pos):
                                # if user selects an upgrade, apply the upgrade
                                if option in self.upgrades:
                                    if option == "Permanent Health Boost":
                                        player.health_cap += 20
                                        player.health = player.health_cap
                                    elif option == "Permanent Speed Boost":
                                        player.speed_cap += 0.5
                                        player.speed = player.speed_cap
                                    print(f"Player upgrade {option}")
                                # if user selects a powerup, apply the powerup
                                elif option in self.powerups:
                                    if option == "Despawner":
                                        powerup = DeSpawner()
                                        powerup.affect_game(surface, enemies, spawn_chances, player)
                                        player.powerup = powerup
                                    elif option == "Invincibility":
                                        powerup = Invincibility()
                                        powerup.affect_player(surface, player)
                                        player.powerup = powerup
                                    elif option == "Extra Fish":
                                        powerup = Extra_Fish()
                                        powerup.affect_player(surface, player)
                                        player.powerup = powerup
                                    elif option == "Speed Boost":
                                        powerup = Speed_Boost()
                                        powerup.affect_player(surface, player)
                                        player.powerup = powerup
                                    # set the start time for the powerup
                                    player.powerup_start = pygame.time.get_ticks()
                                    print(f"Applied powerup: {option}")
                                paused = False  # exit the loop after selecting an item
                                break
                        if not paused:
                            break  # exit the outer loop as well

    # method to use when actually colliding with the chest
    def open(self, surface, enemies, spawn_chances, player):

        """
        Opens the chest and displays the selection menu for upgrades or powerups.

        Parameters
        ----------
        surface : pygame.Surface
            The surface where the options will be displayed.
        enemies : list
            The list of enemies in the game.
        spawn_chances : dict
            The spawn chances of various game elements.
        player : object
            The player object to apply upgrades or powerups.
        """
        
        self.select_options()
        self.display_options(surface, enemies, spawn_chances, player)
