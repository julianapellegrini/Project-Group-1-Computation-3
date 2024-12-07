from powerups.powerup import PowerUp
import time


class Extra_Fish(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/Despawner_icon.png', 'powerup_images/Despawner_image.png', 0.12)

    def affect_player(self, surface, player):
        # the affect player_related logic will be in the player_related class when dealing with the shoot method
        self.active = True
        player.extra_fish = True
        self.start_time = time.time()
        if self.active:
            # Position the power-up image around the player_related
            self.image_rect.center = player.rect.center
            surface.blit(self.image, self.image_rect.topleft)
            # Check if the power-up has been active for 5 seconds
            if self.active and time.time() - self.start_time >= 5:
                self.deactivate(player)

    def affect_game(self):
        pass

    def deactivate(self, player):
        self.active = False
        player.extra_fish = False
