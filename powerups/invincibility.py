from powerups.powerup import PowerUp
from config import *
import pygame

class Invincibility(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/invincibility_icon.png',
                         'powerup_images/invincibility_image.png', 0.18)
        self.active = False
        self.start_time = None
        self.duration = 5  # Duration for which the power-up is active


    def affect_player(self, surface, player):
        # Activate the power-up
        self.active = True
        self.start_time = pygame.time.get_ticks()

        

        # Position the power-up image around the player
        # Load and scale the invincibility image
        self.image = pygame.image.load('powerup_images/invincibility_image.png')
        self.image = pygame.transform.scale(self.image, (player.rect.width + 30, player.rect.height + 30))
        

    def update_position(self, player):
        # Update the position of the invincibility image to follow the player
        self.image_rect = self.image.get_rect(center=player.rect.center)


    def affect_game(self):
        pass  # No change to game

    def deactivate(self, player):
        self.active = False
        player.image = player_image_normal
        player.invincible = False
        player.powerup = None
        print("Invincibility deactivated")

    # For open chest method
    def __repr__(self):
        return "Invincibility"