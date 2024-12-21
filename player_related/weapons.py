import pygame
from utils import *
from config import *


# create weapon class
class Weapon(pygame.sprite.Sprite):
    def __init__(self, name, cooldown, damage, image_path):
        super().__init__()

        self.name = name

        # Load the weapon image
        weapon_image = pygame.image.load(image_path)
        weapon_image = pygame.transform.scale(weapon_image, (26, 26))

        # Create a background surface
        background_size = (30, 30)  # Slightly larger than the weapon image
        self.image = pygame.Surface(background_size, pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 0))  # Transparent background

        # Draw a rectangle as the background
        pygame.draw.rect(self.image, (0, 0, 0), self.image.get_rect(),
                         border_radius=5)  # Black background with rounded corners

        # Blit the weapon image onto the background
        weapon_rect = weapon_image.get_rect(center=self.image.get_rect().center)
        self.image.blit(weapon_image, weapon_rect.topleft)

        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

        # gameplay variables
        self.cooldown = cooldown
        self.damage = damage


class Watergun:
    def __init__(self):
        self.name = "Watergun"
        self.image = pygame.image.load("images_weapons/watergun.png")
        self.image = pygame.transform.scale(self.image, (150, 150))


class Snowball(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Snowball", fps * 2, 5, "images/snowball.png")
        self.damage = 5

    def __repr__(self):
        return "Snowball"


class Slingshot(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Slingshot", fps * 1, 3, "images/slingshot.png")
        self.damage = 3

    def __repr__(self):
        return "Slingshot"


class Fish_bazooka(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Fish Bazooka", fps * 3, 10, "images_weapons/fish_bazooka.png")
        self.damage = 10

    def __repr__(self):
        return "Fish Bazooka"


class Ice_Ninja_Stars(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Ice Ninja Stars", fps * 0.5, 2, "images_weapons/ice_ninja_stars.png")
        self.damage = 2

    def __repr__(self):
        return "Ice Ninja Stars"
