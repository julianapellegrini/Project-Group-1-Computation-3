import pygame
import random
from powerups.powerup import PowerUp


# despawner power-up
class DeSpawner(PowerUp):
    def __init__(self):
        super().__init__('powerup_images/despawner_icon.png',
                         'powerup_images/despawner_image.png', 0.6)
        self.reduction_factor = 0.5
        self.active = False
        self.start_time = None
        self.duration = 5  # Duration for which the power-up is active

    def affect_player(self, surface, player):
        pass  # no effect on the player

    def affect_game(self, surface, enemies, spawn_chances, player):
        # Activate the power-up
        self.active = True
        self.start_time = pygame.time.get_ticks()

        # track enemies before removal, so we can update the current enemies and not crash enemy cap
        enemies_before_remove = len(enemies)

        # remove a certain number of monsters probabilistically
        for enemy in list(enemies):
            if random.random() < 0.5:  # 50% chance to remove each enemy
                enemies.remove(enemy)

        # count after removal
        enemies_after_remove = len(enemies)
        # calculate the number of enemies removed
        enemies_removed = enemies_before_remove - enemies_after_remove

        # change the player's image
        player.load_images_pow()

        # reduce the spawn rate of monsters
        for enemy_type in spawn_chances:
            spawn_chances[enemy_type] *= self.reduction_factor

        # position the power-up image around the player
        self.image = pygame.image.load('powerup_images/despawner_image.png')
        self.image = pygame.transform.scale(self.image, (player.rect.width + 60, player.rect.height + 60))
        self.image_rect = self.image.get_rect(center=player.rect.center)
        surface.blit(self.image, self.image_rect.topleft)

        # return the number of enemies removed so we can get it in the game
        return enemies_removed

    def update_position(self, player):
        # update the position of the invincibility image to follow the player
        self.image_rect = self.image.get_rect(center=player.rect.center)

    def deactivate(self, spawn_chances, player):
        self.active = False
        # restore the original spawn rates
        for enemy_type in spawn_chances:
            spawn_chances[enemy_type] /= self.reduction_factor
        # update the player
        player.powerup = None
        player.load_images()
        print("DeSpawner deactivated")

    # for open chest method and save game
    def __repr__(self):
        return "DeSpawner"
