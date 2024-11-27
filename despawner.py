from config import *
import math
import pygame
from player import Player
from enemy import Enemy
from shed import shed
import random
from powerup import PowerUp



class DeSpawner(PowerUp):
    def __init__(self, duration, reduction_factor, image_path):
        super().__init__(image_path)
        self.duration = duration
        self.reduction_factor = reduction_factor

    def affect_player(self, player):
        pass

    def affect_game(self, spawn_rate):
        self.active = True
        pygame.time.set_timer(pygame.USEREVENT + 2, self.duration)
        return spawn_rate * self.reduction_factor

    def deactivate(self, player, spawn_rate):
        self.active = False
        return spawn_rate / self.reduction_factor