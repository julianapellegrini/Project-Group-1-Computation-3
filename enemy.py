from config import *
import pygame
import random
import math


class Enemy(pygame.sprite.Sprite):

    def __init__(self,max_health=10):
        super().__init__()
        # creating a surface for the enemy
        self.image = pygame.image.load('images/seal1.png')
        self.image = pygame.transform.scale(self.image, (enemy_size[0], enemy_size[-1]))

        # getting rectangle for positioning
        self.rect = self.image.get_rect()

        # starting the enemy at a random valid location on the screen
        self.rect.x = random.randint(0, width - enemy_size[0])
        self.rect.y = random.randint(0, height - enemy_size[-1])

        # setting a random initial speed for the enemy
        self.speed = random.randint(1, 3)

        # set the healthbar
        self.health = max_health
        self.max_health = max_health

    def update(self, player):
        """
        receiving the player as input so that we can assure the enemies move in the players' direction

        """

        # determining the direction of the movement based on the player location
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y

        # getting the direction in radians
        direction = math.atan2(dy, dx)

        # moving the enemy towards the player --> like bullet
        self.rect.x += self.speed * math.cos(direction)
        self.rect.y += self.speed * math.sin(direction)

        self.rect.x = int(self.rect.x)
        self.rect.y = int(self.rect.y)

    def draw_health_bar(self, surface):
        # Define the size and position of the health bar
        bar_width = self.rect.width
        bar_height = 10  # Increase the height of the health bar
        bar_x = self.rect.x
        bar_y = self.rect.y - bar_height - 5  # Adjust the position

        # Ensure health does not go below 0
        health = max(self.health, 0)

        # Calculate the health ratio
        health_ratio = health / self.max_health

        # Draw the background of the health bar
        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height), border_radius=5)

        # Draw the foreground of the health bar
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height), border_radius=5)

        # Add the health percentage text in the middle of the health bar
        font = pygame.font.Font(None, 18)
        health_percentage = int(health_ratio * 100)
        text = font.render(f'{health_percentage}%', True, (255, 255, 255))
        text_rect = text.get_rect(center=(bar_x + bar_width // 2, bar_y + bar_height // 2))
        surface.blit(text, text_rect)
