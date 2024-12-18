from powerups.powerup import PowerUp
from config import *


class Extra_Fish(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/extra_fish_icon.png',
                         'powerup_images/despawner_image.png', 0.12, 5)
    
    def affect_player(self, surface, player):
        # the affect player_related logic will be in the player_related class when dealing with the shoot method
        self.active = True
        player.image = player_image_powered
        player.extra_fish = True

    def affect_game(self):
        pass

    def deactivate(self, player):
        self.active = False
        player.extra_fish = False
        player.image = player_image_normal
        print("Extra Fish deactivated")

    # For open chest method
    def __repr__(self):
        return "Extra Fish"
