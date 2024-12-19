from powerups.powerup import PowerUp
from config import *


class Extra_Fish(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/extra_fish_icon.png',
                         'powerup_images/despawner_image.png', 0.12)
        self.active = False
        
    
    def affect_player(self, surface, player):
        # the affect player_related logic will be in the player_related class when dealing with the shoot method
        self.active = True
        player.image = player_image_powered
        player.powerup_start_time = pygame.time.get_ticks()
        if self.active:
            # position the power-up image around the player
            player.image = player_image_powered
            # check if the power-up has been active for 5 seconds
            # if self.active and time.time() - self.start_time >= 5:
            #     self.deactivate(player)
        

    def affect_game(self):
        pass

    def deactivate(self, player):
        self.active = False
        player.image = player_image_normal
        print("Extra Fish deactivated")

    # For open chest method
    def __repr__(self):
        return "Extra Fish"
