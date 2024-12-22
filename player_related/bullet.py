from config import *
import pygame
import math


# bullet class
class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        super().__init__()

        self.direction = direction
        self.radius = bullet_size
        self.color = oxford_blue

        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.speed = 8

    def update(self):

        #   updating the bullet's position based on the speed and direction
        #   (x,y) --> (cos, sin)
        self.rect.x += int(self.speed * math.cos(self.direction))
        self.rect.y += int(self.speed * math.sin(self.direction))

        #   checking if the bullet is out of the screen and removing it if it is
        if self.rect.x < 0 or self.rect.x > width or self.rect.y < 0 or self.rect.y > height:
            self.kill()

    #  drawing the bullet on screen
    def draw(self, screen):
        # drawing the bullet on screen
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
