import time
from powerups.powerup import PowerUp
from config import *


class Speed_Boost(PowerUp):

    def __init__(self):
        super().__init__('powerup_images/speed_boost_icon.png', 'powerup_images/despawner_image.png', 0.3)
        self.active = False
        

    def affect_player(self, surface, player):
        # the affect player_related logic is in this method
        self.active = True
        player.powerup_start_time = pygame.time.get_ticks()
        player.speed *= 2
        if self.active:
            # position the power-up image around the player
            player.image = player_image_powered
            # check if the power-up has been active for 5 seconds
            # if self.active and time.time() - self.start_time >= 5:
            #     self.deactivate(player)


    def affect_game(self):
        pass  # No change to game

    def deactivate(self, player):
        self.active = False
        player.speed /= 2
        print("Speed Boost deactivated")
        player.image = player_image_normal
        
    
    # For open chest method
    def __repr__(self):
        return "Speed Boost"
