from powerups.powerup import PowerUp
import time


class Extra_Fish(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/extra_fish_icon.png', 'powerup_images/Despawner_image.png', 0.12)
    
    def affect_player(self, surface, player):
        # the affect player_related logic will be in the player_related class when dealing with the shoot method
        self.active = True
        player.extra_fish = True
        if self.active:
            # Position the power-up image around the player_related
            self.image_rect.center = player.rect.center
            surface.blit(self.image, self.image_rect.topleft)

    def affect_game(self):
        pass

    def deactivate(self, player):
        self.active = False
        player.extra_fish = False
