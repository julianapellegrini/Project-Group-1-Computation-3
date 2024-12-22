import pygame
from utils import *
from config import *


# create weapon class
class Weapon(pygame.sprite.Sprite):
    def __init__(self, name, cooldown, damage, image_path):
        super().__init__()

        self.name = name

        # load the weapon image
        weapon_image = pygame.image.load(image_path)
        weapon_image = pygame.transform.scale(weapon_image, (26, 26))

        # create a background surface for the weapon image
        background_size = (30, 30)  # slightly larger than the weapon image
        self.image = pygame.Surface(background_size, pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 0))  # transparent background

        # draw a rectangle as the background
        pygame.draw.rect(self.image, (0, 0, 0), self.image.get_rect(),
                         border_radius=5)  # black background with rounded corners

        # blit the weapon image onto the background
        weapon_rect = weapon_image.get_rect(center=self.image.get_rect().center)
        self.image.blit(weapon_image, weapon_rect.topleft)

        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

        # gameplay variables
        self.cooldown = cooldown
        self.damage = damage


# create the different weapons


class Watergun(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Watergun", fps * 2, 4, "images_weapons/watergun.png")
        self.damage = 4

    def __repr__(self):
        return "Watergun"


class Snowball(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Snowball", fps * 2, 5, "images_weapons/snowball.png")
        self.damage = 5

    def __repr__(self):
        return "Snowball"


class Slingshot(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Slingshot", fps * 1, 3, "images_weapons/slingshot.png")
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


class Sardine_Shooter(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Sardine Shooter", fps * 1, 6, "images_weapons/sardine_shooter.png")
        self.damage = 6

    def __repr__(self):
        return "Sardine Shooter"
