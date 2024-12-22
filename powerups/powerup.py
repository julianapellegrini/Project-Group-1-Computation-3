from abc import ABC, abstractmethod
import pygame
import random


class PowerUp(ABC, pygame.sprite.Sprite):
    
    """
    An abstract base class to represent a power-up in the game.

    Attributes:
    -----------
    probability : float
        The probability of the power-up appearing.
    active : bool
        Whether the power-up is currently active.
    spawned : bool
        Whether the power-up has been spawned.
    icon : pygame.Surface
        The icon image of the power-up.
    icon_rect : pygame.Rect
        The rectangle representing the icon's position and size.
    image : pygame.Surface
        The image of the power-up.
    image_rect : pygame.Rect
        The rectangle representing the image's position and size.
    rect : pygame.Rect
        The rectangle representing the power-up's position and size.
    """

    def __init__(self, icon_path, image_path, probability):

        """
        Initializes the PowerUp with the given parameters.

        Parameters:
        -----------
        icon_path : str
            The path to the power-up's icon image file.
        image_path : str
            The path to the power-up's image file.
        probability : float
            The probability of the power-up appearing.
        """

        super().__init__()
        # probability of powerup appearing
        self.probability = probability

        # powerup state, default is inactive
        self.active = False
        # check if powerup is spawned already
        self.spawned = False
        # load the icon
        self.icon = pygame.image.load(icon_path)
        self.icon = pygame.transform.scale(self.icon, (80, 80))
        self.icon_rect = self.icon.get_rect()
        # load the image
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (150, 150))  # scale the image
        self.image_rect = self.image.get_rect()
        # powerup rect
        self.rect = self.image.get_rect()

    @abstractmethod
    def affect_game(self):

        """
        Abstract method to define the effect of the power-up on the game.
        """

        pass

    @abstractmethod
    def deactivate(self):

        """
        Abstract method to define the deactivation of the power-up.
        """

        pass

    def spawn(self, surface):

        """
        Spawns the power-up at a random position on the surface.

        Parameters:
        -----------
        surface : pygame.Surface
            The Pygame display surface.
        """
        
        # check if power-up is not already spawned and spawn it
        # if its already spawned it will be drawn again at the position it was spawned
        if not self.spawned:
            # define map boundaries
            map_width, map_height = surface.get_size()

            # generate random position within boundaries
            random_x = random.randint(0, map_width - self.icon_rect.width)
            random_y = random.randint(0, map_height - self.icon_rect.height)

            # set the rect position to the random coordinates, using the top left corner of the icon
            self.icon_rect.topleft = (random_x, random_y)

            # set spawned to True
            self.spawned = True

            print(f"powerup spawned {self.icon_rect.topleft}")

        # set the powerup rect to the position of the rect of the icon of the powerup
        self.rect.topleft = self.icon_rect.topleft
        # draw the powerup
        surface.blit(self.icon, self.icon_rect.topleft)
