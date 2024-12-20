from powerups.powerup import PowerUp
from config import *
import pygame

class Extra_Fish(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/extra_fish_icon.png',
                         'powerup_images/despawner_image.png', 0.12)
        self.active = False
        self.start_time = None
        self.duration = 5  # Duration for which the power-up is active

    def affect_player(self, surface, player):
        # Activate the power-up
        self.active = True
        self.start_time = pygame.time.get_ticks()
        player.image = player_image_powered

        # Position the power-up image around the player
        self.image = pygame.image.load('powerup_images/despawner_image.png')
        self.image = pygame.transform.scale(self.image, (player.rect.width + 30, player.rect.height + 30))
        self.image_rect = self.image.get_rect(center=player.rect.center)
        surface.blit(self.image, self.image_rect.topleft)

    def affect_game(self):
        pass  # No change to game

    def deactivate(self, player):
        self.active = False
        player.image = player_image_normal
        player.powerup = None
        print("Extra Fish deactivated")

    # For open chest method
    def __repr__(self):
        return "Extra Fish"