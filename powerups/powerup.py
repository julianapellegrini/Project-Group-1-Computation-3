from abc import ABC, abstractmethod
import pygame


class PowerUp(ABC):
    def __init__(self, icon_path, image_path, probability):
        super().__init__()
        # probability of powerup appearing
        self.probability = probability
        # powerup state, default is inactive
        self.active = False
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

    @abstractmethod
    def affect_player(self, surface, player):
        pass

    @abstractmethod
    def affect_game(self, spawn_rate):
        pass

    @abstractmethod
    def deactivate(self, player):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
