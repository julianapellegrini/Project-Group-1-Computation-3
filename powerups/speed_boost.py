import pygame
import random
import time
from powerups.powerup import PowerUp


class Speed_Boost(PowerUp):

    def __init__(self):
        super().__init__('powerup_images/rollerblades.jpg', 'powerup_images/speed_boost.png', 0.3)

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

    def affect_game(self, spawn_rate):
        return  # No change to game

    def deactivate(self, player):
        self.active = False
        player.speed /= 2
        return

    def draw(self, surface):
        # define map boundaries
        map_width, map_height = surface.get_size()

        # generate random position within boundaries
        random_x = random.randint(0, map_width - self.icon_rect.width)
        random_y = random.randint(0, map_height - self.icon_rect.height)

        # set the rect position to the random coordinates, using the top left corner of the icon
        self.icon_rect.topleft = (random_x, random_y)

        # Draw the power-up at the new position
        surface.blit(self.icon, self.icon_rect.topleft)
