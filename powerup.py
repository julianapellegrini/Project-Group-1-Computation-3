from abc import ABC, abstractmethod
import pygame

class PowerUp(ABC):

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

