from powerups.powerup import PowerUp
import time


class Invincibility(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/snow_globe.jpg', 'powerup_images/invincibility.png', 0.18)

    def affect_player(self, surface, player):
        # the affect player_related logic will be in the game loop when dealing with the collisions between enemies
        # and players
        player.invincible = True
        self.active = True
        self.start_time = time.time()
        if self.active:
            # Position the power-up image around the player_related
            self.image_rect.center = player.rect.center
            surface.blit(self.image, self.image_rect.topleft)
            # Check if the power-up has been active for 5 seconds
            if self.active and time.time() - self.start_time >= 5:
                self.deactivate(player)

    def affect_game(self):
        pass  # No change to game

    def deactivate(self, player):
        player.invincible = False
        self.active = False
        self.start_time = time.time()
        return
