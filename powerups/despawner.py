from powerups.powerup import PowerUp
import time
import pygame
from player_related.player import player_size


class DeSpawner(PowerUp):

    def __init__(self):
        super().__init__('powerup_images/despawner_icon.png',
                         'powerup_images/despawner_image.png', 0.6, 5)
        self.reduction_factor = 0.5

    def affect_player(self, surface, player):
        pass

    def affect_game(self, surface, spawn_rate, player):
        # The affect game logic is in this method
        self.active = True
        self.start_time = time.time()
        if self.active:
            # Position the power-up image around the player_related
            self.image = pygame.image.load('powerup_images/despawner_image.png')
            self.image =pygame.transform.scale(self.image, (player_size[0] + 30, player_size[-1] + 30))
            self.image_rect.center = player.rect.center
            surface.blit(self.image, self.image_rect.topleft)
            # Check if the power-up has been active for 5 seconds
            if self.active and time.time() - self.start_time >= 5:
                self.deactivate()
        return spawn_rate * self.reduction_factor

    def deactivate(self, spawn_rate):
        self.active = False
        return spawn_rate / self.reduction_factor
