from powerups.powerup import PowerUp
import time
import random
from config import *


class DeSpawner(PowerUp):

    def __init__(self):
        super().__init__('powerup_images/despawner_icon.png',
                         'powerup_images/despawner_image.png', 0.6, 5)
        self.reduction_factor = 0.5
        self.active = False
        self.start_time = None
        self.duration = 5  # Duration for which the power-up is active

    def affect_player(self, surface, player):
        pass

    def affect_game(self, surface, enemies, spawn_chances, player):
        # Activate the power-up
        self.active = True
        self.start_time = time.time()

        # Remove a certain number of monsters probabilistically
        for enemy in list(enemies):
            if random.random() < 0.5:  # 50% chance to remove each enemy
                enemies.remove(enemy)

        # Reduce the spawn rate of monsters
        for enemy_type in spawn_chances:
            spawn_chances[enemy_type] *= self.reduction_factor

        # Position the power-up image around the player
        if self.active:
            player.image = penguin_infinity_stone

    def update(self, surface, enemies, spawn_chances, player):
        # Check if the power-up has been active for the specified duration
        if self.active and time.time() - self.start_time >= self.duration:
            self.deactivate(spawn_chances)

    def deactivate(self, spawn_chances):
        self.active = False
        # Restore the original spawn rates
        for enemy_type in spawn_chances:
            spawn_chances[enemy_type] /= self.reduction_factor

    def __repr__(self):
        return "DeSpawner"