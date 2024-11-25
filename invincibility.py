from config import *
import math
import pygame
from player import Player
from enemy import Enemy
from shed import shed
import random
from powerup import PowerUp
from despawner import DeSpawner

class Invincibility(PowerUp):
    def __init__(self, duration, image_path):
        super().__init__(image_path)
        self.duration = duration
        self.active = False
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (170,170))  # Scale the image
        self.rect = self.image.get_rect()


    def affect_player(self,surface, player):
        self.image= pygame.transform.scale(self.image, (150,150))
        player.invincible = True
        self.active = True
        if player:
            # Position the power-up image around the player
            self.rect.center = player.rect.center
            surface.blit(self.image, self.rect.topleft)


    def affect_game(self, spawn_rate):
        return spawn_rate  # No change to spawn rate

    def deactivate(self, player, spawn_rate):
        player.invincible = False
        self.active = False
        return spawn_rate
    
    def draw(self, surface,player):
        # Define map boundaries
        map_width, map_height = surface.get_size()
        
        # Generate random position within map boundaries
        random_x = random.randint(0, map_width - self.rect.width)
        random_y = random.randint(0, map_height - self.rect.height)
        
        # Set the rect position to the random coordinates
        self.rect.topleft = (random_x, random_y)
        
        # Draw the power-up at the new position
        surface.blit(self.image, self.rect.topleft)
        