from utils import *
from config import *
import pygame
import math
from bullet import Bullet
from inventory import Inventory
from weapons import Snowball


# making Player a child of the Sprite class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        # calling the mother class' init
        super().__init__()

        # VISUAL VARIABLES

        # character attempt
        # (FAIL) character = pygame.image.load("images/girl.jpeg")
        # FAIL self.image.blit(character)

        # we call surface to represent the player image
        self.image = pygame.Surface(player_size)

        # drawing the image of the player
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

        # GAMEPLAY VARIABLES

        self.speed = 3
        self.health = 100
        self.bullet_cooldown = 0

        # Player has an inventory
        self.inventory = Inventory()

        # Weapons
        self.weapon = Snowball()  # Default weapon

    # Inventory methods
    def add_item(self, item):
        self.inventory.add_item(item)

    # Weapon methods

    def change_weapon(self, weapon):
        self.weapon = weapon

    def update(self):

        # getting the keys input:

        keys = pygame.key.get_pressed()

        # checking which keys were pressed and moving the player accordingly
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < height:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < width:
            self.rect.x += self.speed

    def shoot(self, bullets):
        """

        bullets --> pygame group where I will add bullets
        """

        if self.alive():
            # cooldown ==> how many frames I need until I can shoot again
            if self.bullet_cooldown <= 0:
                # defining the directions in which the bullets will fly
                # these 4 directions are, in order, right, left, up, down
                for angle in [0, math.pi, math.pi / 2, 3 * math.pi / 2]:
                    # creating a bullet for each angle
                    # I will use self.rect.centerx to make the x position of the bullet the same as the
                    # x position of the player, thus making the bullet come out of them
                    # finally, the direction of the bullet is the angle
                    bullet = Bullet(self.rect.centerx, self.rect.centery, angle)
                    # adding  the bullet to the bullets pygame group
                    bullets.add(bullet)

                # resetting the cooldown according to the weapon's cooldown
                self.bullet_cooldown = self.weapon.cooldown

            self.bullet_cooldown -= 1

    def draw_health_bar(self, surface):
        # Define the size and position of the health bar
        bar_width = self.rect.width
        bar_height = 10  # Increase the height of the health bar
        bar_x = self.rect.x
        bar_y = self.rect.y - bar_height - 5  # Adjust the position

        # Ensure health does not go below 0
        health = max(self.health, 0)

        # Calculate the health ratio
        health_ratio = health / 100

        # Draw the background of the health bar
        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height), border_radius=5)

        # Draw the foreground of the health bar
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height), border_radius=5)

        # Add the health ratio text in the middle of the health bar
        font = pygame.font.Font(None, 18)
        text = font.render(f'{int(health)}%', True, (255, 255, 255))
        text_rect = text.get_rect(center=(bar_x + bar_width // 2, bar_y + bar_height // 2))
        surface.blit(text, text_rect)

