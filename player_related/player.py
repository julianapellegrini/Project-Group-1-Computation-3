import pygame.image

from config import *
import math
from player_related.bullet import Bullet
from player_related.inventory import Inventory
from player_related.weapons import Snowball, Slingshot, Watergun
from powerups.extra_fish import Extra_Fish

ptypes = ['gray', 'brown', 'eyebrow']  # just for reference


# making Player a child of the Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # calling the mother class' init
        super().__init__()

        self.ptype = 'gray'  # default penguin type
        self.load_images()  # actually loading the images

        # Set the default image
        self.image = self.image_d_stop
        self.image = pygame.transform.scale(self.image, (player_size[0], player_size[1]))

        # drawing the image of the player_related

        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

        # GAMEPLAY VARIABLES
        self.speed_cap = 6
        self.speed = 6
        self.health_cap = 100
        self.health = 100
        self.bullet_cooldown = 0

        # Level

        self.level = 1

        # Player has an inventory
        self.inventory = Inventory()

        # Player has a Watergun in his inventory
        watergun = Watergun()
        self.inventory.add_item(watergun)

        # Player has currency
        self.balance = 0

        # Weapons
        self.weapon = watergun  # default weapon

        # Powerups
        self.powerup = None  # current powerup, default is None

        # Powerup timer
        self.powerup_start = None

        # counter so we can cycle through the images for movement
        self.animation_counter = 0

    # function to load images so the skin change works
    def load_images(self):
        # load images for different directions and to switch between them
        self.image_up = pygame.image.load(f'images_penguins/{self.ptype}up.png')
        self.image_d_stop = pygame.image.load(f'images_penguins/{self.ptype}downstop.png')
        self.image_d_1 = pygame.image.load(f'images_penguins/{self.ptype}down1.png')
        self.image_d_2 = pygame.image.load(f'images_penguins/{self.ptype}down2.png')
        self.image_l_1 = pygame.image.load(f'images_penguins/{self.ptype}left1.png')
        self.image_l_2 = pygame.image.load(f'images_penguins/{self.ptype}left2.png')
        self.image_r_1 = pygame.image.load(f'images_penguins/{self.ptype}right1.png')
        self.image_r_2 = pygame.image.load(f'images_penguins/{self.ptype}right2.png')

        # scaling the images
        self.image_up = pygame.transform.scale(self.image_up, player_size)
        self.image_d_stop = pygame.transform.scale(self.image_d_stop, player_size)
        self.image_d_1 = pygame.transform.scale(self.image_d_1, player_size)
        self.image_d_2 = pygame.transform.scale(self.image_d_2, player_size)
        self.image_l_1 = pygame.transform.scale(self.image_l_1, player_size)
        self.image_l_2 = pygame.transform.scale(self.image_l_2, player_size)
        self.image_r_1 = pygame.transform.scale(self.image_r_1, player_size)
        self.image_r_2 = pygame.transform.scale(self.image_r_2, player_size)

    def load_images_pow(self):
        # load images for different directions and to switch between them
        self.image_up = pygame.image.load(f'images_penguins/{self.ptype}uppow.png')
        self.image_d_stop = pygame.image.load(f'images_penguins/{self.ptype}downstoppow.png')
        self.image_d_1 = pygame.image.load(f'images_penguins/{self.ptype}down1pow.png')
        self.image_d_2 = pygame.image.load(f'images_penguins/{self.ptype}down2pow.png')
        self.image_l_1 = pygame.image.load(f'images_penguins/{self.ptype}left1pow.png')
        self.image_l_2 = pygame.image.load(f'images_penguins/{self.ptype}left2pow.png')
        self.image_r_1 = pygame.image.load(f'images_penguins/{self.ptype}right1pow.png')
        self.image_r_2 = pygame.image.load(f'images_penguins/{self.ptype}right2pow.png')

        # scaling the images
        self.image_up = pygame.transform.scale(self.image_up, player_size)
        self.image_d_stop = pygame.transform.scale(self.image_d_stop, player_size)
        self.image_d_1 = pygame.transform.scale(self.image_d_1, player_size)
        self.image_d_2 = pygame.transform.scale(self.image_d_2, player_size)
        self.image_l_1 = pygame.transform.scale(self.image_l_1, player_size)
        self.image_l_2 = pygame.transform.scale(self.image_l_2, player_size)
        self.image_r_1 = pygame.transform.scale(self.image_r_1, player_size)
        self.image_r_2 = pygame.transform.scale(self.image_r_2, player_size)

    # Inventory of fish caught
    def add_fish(self, fish):
        self.inventory.add_item(fish)

    # Inventory methods
    def load_data(self, data):
        # load player data from save file
        self.inventory.items = eval(data[0])
        self.balance = int(data[1])
        self.level = int(data[3])
        self.ptype = data[4]
        self.load_images()
        self.health_cap = int(data[5])
        self.speed_cap = int(data[6])

        # Load the weapon
        weapon_name = data[2].split("(")[0]
        if weapon_name == "Snowball":
            self.weapon = Snowball()
        else:
            self.weapon = Slingshot()

    def add_item(self, item):
        # Add the item to the inventory
        self.inventory.add_item(item)
        print(f"Added {item.name} to inventory")
        print(self.inventory.items)

    # Weapon methods

    def change_weapon(self, weapon):
        self.weapon = weapon

    def update(self, surface):
        keys = pygame.key.get_pressed()

        # add to animation counter
        self.animation_counter += 1

        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
            if self.animation_counter % 20 < 10:
                self.image = self.image_d_1
            else:
                self.image = self.image_d_2
        if keys[pygame.K_s] and self.rect.bottom < height:
            self.rect.y += self.speed
            if self.animation_counter % 20 < 10:
                self.image = self.image_d_1
            else:
                self.image = self.image_d_2
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
            if self.animation_counter % 20 < 10:
                self.image = self.image_l_1
            else:
                self.image = self.image_l_2
        if keys[pygame.K_d] and self.rect.right < width:
            self.rect.x += self.speed
            if self.animation_counter % 20 < 10:
                self.image = self.image_r_1
            else:
                self.image = self.image_r_2

    def shoot(self, bullets):
        """

        bullets --> pygame group where I will add bullets
        """

        if self.alive():
            # cooldown ==> how many frames I need until I can shoot again
            if self.bullet_cooldown <= 0:
                # defining the directions in which the bullets will fly
                # these 4 directions are, in order, right, left, up, down
                angles = [0, math.pi, math.pi / 2, 3 * math.pi / 2]

                # If the extra fish powerup is active, add the diagonal angles
                if isinstance(self.powerup, Extra_Fish):
                    # Add angles for the corners
                    # in order: top right diagonal, top left diagonal, bottom left diagonal, bottom right diagonal
                    angles.extend([math.pi / 4, 3 * math.pi / 4, 5 * math.pi / 4, 7 * math.pi / 4])
                
                for angle in angles:
                    # creating a bullet for each angle
                    bullet = Bullet(self.rect.centerx, self.rect.centery, angle)
                    # adding the bullet to the bullets pygame group
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
