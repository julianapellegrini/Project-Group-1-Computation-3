from powerups.powerup import PowerUp
from config import *
import time

class Invincibility(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/invincibility_icon.png',
                         'powerup_images/invincibility_image.png', 0.18)
        self.active = False


    def affect_player(self, surface, player):
        # the affect player_related logic will be in the game loop when dealing with the collisions between enemies
        # and players
        
        self.active = True
        player.powerup_start_time = pygame.time.get_ticks()
        if self.active:
            # Change player color
            player.image = player_image_powered

    def affect_game(self):
        pass  # No change to game

    def deactivate(self, player):
        player.image = player_image_normal
        self.active = False
        print("Invincibility deactivated")
        player.powerup = None

    # For open chest method
    def __repr__(self):
        return "Invincibility"
