from utils import *
from config import *


# create weapon class
class Weapon(pygame.sprite.Sprite):
    def __init__(self, name, cooldown, damage, image_path):
        super().__init__()

        self.name = name

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (26, 26))
        self.rect = self.image.get_rect()

        self.rect.center = (width // 2, height // 2)

        # gameplay variables

        self.cooldown = cooldown
        self.damage = damage


class Snowball(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Snowball", fps * 2, 5, "images/snowball.png")


class Slingshot(Weapon, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Slingshot", fps * 1, 10, "images/slingshot.png")
