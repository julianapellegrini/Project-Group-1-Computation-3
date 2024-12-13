from config import *
import pygame
import math


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        super().__init__()

        self.direction = direction
        self.radius = bullet_size
        self.color = yellow
        self.image = None  # none for now, changes later depending on the direction

        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.speed = 8

    def update(self):

        #   updating the bullet's position based on the speed and direction
        #   (x,y) --> (cos, sin)
        self.rect.x += int(self.speed * math.cos(self.direction))
        self.rect.y += int(self.speed * math.sin(self.direction))

        if self.rect.x < 0 or self.rect.x > width or self.rect.y < 0 or self.rect.y > height:
            self.kill()

    def draw(self, screen):
        # bullet image changes based on the direction of the bullet
        if self.direction == 0:
            image = pygame.image.load('images/bullet_right.png')
            image = pygame.transform.scale(image, (bullet_size, bullet_size))
            self.image = image
        elif self.direction == math.pi / 2:
            image = pygame.image.load('images/bullet_down.png')
            image = pygame.transform.scale(image, (bullet_size, bullet_size))
            self.image = image
        elif self.direction == math.pi:
            image = pygame.image.load('images/bullet_left.png')
            image = pygame.transform.scale(image, (bullet_size, bullet_size))
            self.image = image
        elif self.direction == 3 * math.pi / 2:
            image = pygame.image.load('images/bullet_up.png')
            image = pygame.transform.scale(image, (bullet_size, bullet_size))
            self.image = image
        elif self.direction == math.pi / 4:
            image = pygame.image.load('images/bullet_up.png')
            image = pygame.transform.scale(image, (bullet_size, bullet_size))
            self.image = image
        elif self.direction == 3 * math.pi / 4:
            image = pygame.image.load('images/bullet_up.png')
            image = pygame.transform.scale(image, (bullet_size, bullet_size))
            self.image = image
        elif self.direction == 5 * math.pi / 4:
            image = pygame.image.load('images/bullet_up.png')
            image = pygame.transform.scale(image, (bullet_size, bullet_size))
            self.image = image
        elif self.direction == 7 * math.pi / 4:
            image = pygame.image.load('images/bullet_up.png')
            image = pygame.transform.scale(image, (bullet_size, bullet_size))
            self.image = image

        # drawing the bullet on the screen
        screen.blit(self.image, self.rect)
