import pygame
from powerups.powerup import PowerUp
import time


class Extra_Fish(PowerUp):
    def __init__(self,image_path):
        super().__init__(image_path)
        
        self.active = False
        # load the icon
        self.icon = pygame.image.load('powerup_images/Despawner_icon.png')
        self.icon = pygame.transform.scale(self.icon, (50, 50))
        self.icon_rect = self.icon.get_rect()
        # load the image
        self.image = pygame.image.load('powerup_images/Despawner_image.png')
        self.image = pygame.transform.scale(self.image, (150, 150))  # Scale the image
        self.image_rect = self.image.get_rect()

    def affect_player(self,surface, player):
        #the affect player logic will be in the player class when dealing with the shoot method
        self.active = True
        player.extra_fish = True
        self.start_time = time.time()
        if self.active:
            # Position the power-up image around the player
            self.image_rect.center = player.rect.center
            surface.blit(self.image, self.rect.topleft)
            # Check if the power-up has been active for 5 seconds
            if self.active and time.time() - self.start_time >= 5:
                self.deactivate(player)

    def affect_game(self, surface,spawn_rate,player):
        pass

    def deactivate(self, player, spawn_rate):
        self.active = False
        player.extra_fish = False
        