import pygame
from powerups.powerup import PowerUp
from config import *


# speed boost power-up
class Speed_Boost(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/speed_boost_icon.png', 'powerup_images/despawner_image.png', 0.3)
        self.active = False
        self.start_time = None
        self.duration = 5  # duration for which the power-up is active

    def affect_player(self, surface, player):
        # activate the power-up
        self.active = True
        self.start_time = pygame.time.get_ticks()
        player.speed *= 2

        # change the player's image
        player.load_images_pow()

        # position the power-up image around the player
        # load and scale the invincibility image
        self.image = pygame.image.load('powerup_images/speed_boost_image.png')
        self.image = pygame.transform.scale(self.image, (player.rect.width + 200, player.rect.height + 50))

    def update_position(self, player):
        # update the position of the speed boost image to keep the player in the bottom middle
        self.image_rect = self.image.get_rect()  # get the rectangle for the image
        self.image_rect.centerx = player.rect.centerx  # align the center of the image with the center of the player
        self.image_rect.bottom = player.rect.bottom + (self.image_rect.height - player.rect.height) // 2

    def affect_game(self):
        pass  # no change to game

    def deactivate(self, player):
        # deactivate the power-up and update player image
        self.active = False
        player.speed = player.speed_cap
        player.load_images()
        player.powerup = None
        print("Speed Boost deactivated")

    # for open chest method and save game
    def __repr__(self):
        return "Speed Boost"
