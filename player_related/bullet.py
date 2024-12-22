from config import *
import pygame
import math
from powerups.extra_fish import Extra_Fish

# bullet class
class Bullet(pygame.sprite.Sprite):
    
    
    """
    A class to represent a bullet in the game.

    Attributes:
    -----------
    direction : float
        The direction in which the bullet is moving.
    radius : int
        The radius of the bullet.
    color : tuple
        The color of the bullet.
    rect : pygame.Rect
        The rectangle representing the bullet's position and size.
    speed : int
        The speed of the bullet.
    """

    def __init__(self, x, y, direction):

        """
        Initializes the Bullet with the given parameters.

        Parameters:
        -----------
        x : int
            The x-coordinate of the bullet's starting position.
        y : int
            The y-coordinate of the bullet's starting position.
        direction : float
            The direction in which the bullet is moving.
        """

        super().__init__()

        self.direction = direction
        self.radius = bullet_size
        self.color = oxford_blue
        self.powered_color = glowing_light_red
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.speed = 8

    def update(self):

        """
        Updates the bullet's position based on its speed and direction.

        This method also checks if the bullet is out of the screen and removes it if it is.
        """


        #   updating the bullet's position based on the speed and direction
        #   (x,y) --> (cos, sin)
        self.rect.x += int(self.speed * math.cos(self.direction))
        self.rect.y += int(self.speed * math.sin(self.direction))

        #   checking if the bullet is out of the screen and removing it if it is
        if self.rect.x < 0 or self.rect.x > width or self.rect.y < 0 or self.rect.y > height:
            self.kill()

    #  drawing the bullet on screen
    def draw(self, screen,player):

        """
        Draws the bullet on the screen.

        Parameters:
        -----------
        screen : pygame.Surface
            The Pygame display surface.
        """

        # drawing the bullet on screen
        # drawing the bullet on screen
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
        if not isinstance(player.powerup, Extra_Fish):
            pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
        else:
            pygame.draw.circle(screen, self.powered_color, self.rect.center, self.radius)
