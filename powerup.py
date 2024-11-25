from abc import ABC, abstractmethod
import pygame

class PowerUp(ABC):
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.active = False

    @abstractmethod
    def affect_player(self, player):
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

