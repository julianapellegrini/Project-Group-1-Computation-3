

from config import *
import math
import pygame
from player import Player
from enemy import Enemy
from shed import shed
import random
from powerup import PowerUp
from despawner import DeSpawner
import time


class Invincibility(PowerUp):
    def __init__(self):
        super().__init__()
        self.active = False
        # load the icon
        self.icon = pygame.image.load('powerup_images/snow_globe.jpg')
        self.icon = pygame.transform.scale(self.icon, (50, 50))
        self.icon_rect = self.icon.get_rect()
        # load the image
        self.image = pygame.image.load('powerup_images/invincibility.png')
        self.image = pygame.transform.scale(self.image, (150, 150))  # Scale the image
        self.image_rect = self.image.get_rect()

    def affect_player(self, surface, player):
        #the affect player logic will be in the game loop when dealing with the collisions between enemies and players
        player.invincible = True
        self.active = True
        self.start_time = time.time()
        if self.active:
            # Position the power-up image around the player
            self.image_rect.center = player.rect.center
            surface.blit(self.image, self.rect.topleft)
            # Check if the power-up has been active for 5 seconds
            if self.active and time.time() - self.start_time >= 5:
                self.deactivate(player)
        

        


    def affect_game(self):
        return  # No change to game

    def deactivate(self, player):
        player.invincible = False
        self.active = False
        self.start_time = time.time()
        return
    

    def draw(self, surface):
        # Define map boundaries
        map_width, map_height = surface.get_size()

        # Generate random position within map boundaries
        random_x = random.randint(0, map_width - self.icon_rect.width)
        random_y = random.randint(0, map_height - self.icon_rect.height)

        # Set the rect position to the random coordinates
        self.icon_rect.topleft = (random_x, random_y)

        # Draw the power-up at the new position
        surface.blit(self.icon, self.icon_rect.topleft)

