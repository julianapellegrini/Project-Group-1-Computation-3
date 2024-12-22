import pygame
import random
from powerups.powerup import PowerUp

class DeSpawner(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/despawner_icon.png',
                         'powerup_images/despawner_image.png', 0.6)
        self.reduction_factor = 0.5
        self.active = False
        self.start_time = None
        self.duration = 5  # Duration for which the power-up is active


        

    def affect_player(self, surface, player):
        pass

    def affect_game(self, surface, enemies, spawn_chances, player):
        # Activate the power-up
        self.active = True
        self.start_time = pygame.time.get_ticks()

        # track enemies before removal, so we can update the current enemies and not crash enemy cap
        enemies_before_remove = len(enemies)

        # Remove a certain number of monsters probabilistically
        for enemy in list(enemies):
            if random.random() < 0.5:  # 50% chance to remove each enemy
                enemies.remove(enemy)

        # count after removal
        enemies_after_remove = len(enemies)
        # calculate the number of enemies removed
        enemies_removed = enemies_before_remove - enemies_after_remove

        # change the player's image
        player.load_images_pow()

        # Reduce the spawn rate of monsters
        for enemy_type in spawn_chances:
            spawn_chances[enemy_type] *= self.reduction_factor

        # Position the power-up image around the player
        self.image = pygame.image.load('powerup_images/despawner_image.png')
        self.image = pygame.transform.scale(self.image, (player.rect.width + 60, player.rect.height + 60))
        self.image_rect = self.image.get_rect(center=player.rect.center)
        surface.blit(self.image, self.image_rect.topleft)

        return enemies_removed

    def update_position(self, player):
        # Update the position of the invincibility image to follow the player
        self.image_rect = self.image.get_rect(center=player.rect.center)

    def deactivate(self, spawn_chances, player):
        self.active = False
        # Restore the original spawn rates
        for enemy_type in spawn_chances:
            spawn_chances[enemy_type] /= self.reduction_factor
        player.powerup = None
        player.load_images()
        print("DeSpawner deactivated")

    # For open chest method
    def __repr__(self):
        return "DeSpawner"