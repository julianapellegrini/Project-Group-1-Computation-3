import pygame
import random
from powerups.powerup import PowerUp


# despawner power-up
class DeSpawner(PowerUp):

    """
    A class to represent the DeSpawner power-up.

    Attributes:
    -----------
    reduction_factor : float
        The factor by which the spawn rate of enemies is reduced.
    active : bool
        Whether the power-up is currently active.
    start_time : int
        The time at which the power-up was activated.
    duration : int
        The duration for which the power-up is active.
    """

    def __init__(self):

        """
        Initializes the DeSpawner power-up with default attributes.
        """

        super().__init__('powerup_images/despawner_icon.png',
                         'powerup_images/despawner_image.png', 0.6)
        self.reduction_factor = 0.5
        self.active = False
        self.start_time = None
        self.duration = 5  # Duration for which the power-up is active

    def affect_player(self, surface, player):

        """
        No effect on the player.

        Parameters:
        -----------
        surface : pygame.Surface
            The Pygame display surface.
        player : object
            The player object.
        """
         
        pass  # no effect on the player

    def affect_game(self, surface, enemies, spawn_chances, player):
        
        """
        Activates the power-up and affects the game by reducing the spawn rate of enemies.

        Parameters:
        -----------
        surface : pygame.Surface
            The Pygame display surface.
        enemies : list
            The list of enemies in the game.
        spawn_chances : dict
            The dictionary of spawn chances for each enemy type.
        player : object
            The player object.

        Returns:
        --------
        int
            The number of enemies removed.
        """
         
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

        """
        Updates the position of the power-up image to follow the player.

        Parameters:
        -----------
        player : object
            The player object.
        """

        # update the position of the invincibility image to follow the player
        self.image_rect = self.image.get_rect(center=player.rect.center)

    def deactivate(self, spawn_chances, player):

        """
        Deactivates the power-up and restores the original spawn rates.

        Parameters:
        -----------
        spawn_chances : dict
            The dictionary of spawn chances for each enemy type.
        player : object
            The player object.
        """

        self.active = False
        # restore the original spawn rates
        for enemy_type in spawn_chances:
            spawn_chances[enemy_type] /= self.reduction_factor
        # update the player
        player.powerup = None
        player.load_images()
        print("DeSpawner deactivated")

    
    def __repr__(self):
        return "DeSpawner"
