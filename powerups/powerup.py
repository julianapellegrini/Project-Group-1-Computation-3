from abc import ABC, abstractmethod
import pygame
import random


class PowerUp(ABC, pygame.sprite.Sprite):
    def __init__(self, icon_path, image_path, probability):
        super().__init__()
        # probability of powerup appearing
        self.probability = probability
        # powerup state, default is inactive
        self.active = False
        # check if powerup is spawned already
        self.spawned = False
        # time player got the powerup, default is empty
        self.start_time = None
        # load the icon
        self.icon = pygame.image.load(icon_path)
        self.icon = pygame.transform.scale(self.icon, (50, 50))
        self.icon_rect = self.icon.get_rect()
        # load the image
        # TO CHANGE
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (150, 150))  # scale the image
        self.image_rect = self.image.get_rect()
        # powerup rect
        self.rect = self.image.get_rect()

    @abstractmethod
    def affect_player(self, surface, player):
        pass

    @abstractmethod
    def affect_game(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

    def spawn(self, surface):
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

        # draw the powerup
        surface.blit(self.icon, self.icon_rect.topleft)
