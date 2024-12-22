from powerups.powerup import PowerUp
from config import *
import pygame


# extra fish power-up
class Extra_Fish(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/extra_fish_icon.png',
                         'powerup_images/despawner_image.png', 0.12)
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
        self.image = pygame.image.load('powerup_images/despawner_image.png')
        self.image = pygame.transform.scale(self.image, (player.rect.width + 30, player.rect.height + 30))
        self.image_rect = self.image.get_rect(center=player.rect.center)
        surface.blit(self.image, self.image_rect.topleft)

    def affect_game(self):
        pass  # no change to game

    def deactivate(self, player):
        # deactivate the power-up and update player image
        self.active = False
        player.load_images()
        player.powerup = None
        print("Extra Fish deactivated")

    # for open chest method and save game
    def __repr__(self):
        return "Extra Fish"
