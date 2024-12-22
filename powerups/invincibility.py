from powerups.powerup import PowerUp
from config import *
import pygame


# invincibility power-up
class Invincibility(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/invincibility_icon.png',
                         'powerup_images/invincibility_image.png', 0.18)
        self.active = False
        self.start_time = None
        self.duration = 5  # duration for which the power-up is active

    def affect_player(self, surface, player):
        # activate the power-up
        self.active = True
        self.start_time = pygame.time.get_ticks()

        # change the player's image
        player.load_images_pow()

        # position the power-up image around the player
        # load and scale the invincibility image
        self.image = pygame.image.load('powerup_images/invincibility_image.png')
        self.image = pygame.transform.scale(self.image, (player.rect.width + 30, player.rect.height + 30))

    def update_position(self, player):
        # update the position of the invincibility image to follow the player
        self.image_rect = self.image.get_rect(center=player.rect.center)

    def affect_game(self):
        pass  # no change to game

    def deactivate(self, player):
        # deactivate the power-up and update player image
        self.active = False
        player.load_images()
        player.invincible = False
        player.powerup = None
        print("Invincibility deactivated")

    # for open chest method and save game
    def __repr__(self):
        return "Invincibility"
