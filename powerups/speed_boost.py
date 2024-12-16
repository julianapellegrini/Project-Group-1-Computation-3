import time
from powerups.powerup import PowerUp


class Speed_Boost(PowerUp):

    def __init__(self):
        super().__init__('powerup_images/speed_boost_icon.png', 'powerup_images/speed_boost.png', 0.3,5)

    def affect_player(self, surface, player):
        # the affect player_related logic is in this method
        self.active = True
        player.speed *= 2
        self.start_time = time.time()
        if self.active:
            # position the power-up image around the player
            self.image_rect.center = player.rect.center
            surface.blit(self.image, self.image_rect.topleft)
            # check if the power-up has been active for 5 seconds
            if self.active and time.time() - self.start_time >= 5:
                self.deactivate(player)

    def affect_game(self):
        pass  # No change to game

    def deactivate(self, player):
        self.active = False
        player.speed /= 2
        return
    
    # For open chest method
    def __repr__(self):
        return "Speed Boost"
