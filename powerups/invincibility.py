from powerups.powerup import PowerUp
from config import *

class Invincibility(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/invincibility_icon.png',
                         'powerup_images/invincibility_image.png', 0.18, 5)

    def affect_player(self, surface, player):
        # the affect player_related logic will be in the game loop when dealing with the collisions between enemies
        # and players
        player.invincible = True
        self.active = True
        if self.active:
            # Change player color
            player.image = player_image_powered

    def affect_game(self):
        pass  # No change to game

    def deactivate(self, player):
        player.invincible = False
        player.image = player_image_normal
        self.active = False

    # For open chest method
    def __repr__(self):
        return "Invincibility"
