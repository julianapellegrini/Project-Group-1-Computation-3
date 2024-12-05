from utils import *
from config import *
import random

# Measures of the centered rectangle
height_centered = 30

rect_width = resolution[0] * 2 // 3
rect_height = height_centered

rect_x = (resolution[0] - rect_width) // 2
rect_y = (resolution[1] - rect_height) // 2

# Boundaries of the centered rectangle
x_start = rect_x
x_end = rect_x + rect_width


# Creating the fish class
class Fish(pygame.sprite.Sprite):
    def __init__(self, name, price, speed, image_path, probability):
        super().__init__()
        self.name = name
        self.price = price
        self.speed = speed
        self.probability = probability
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (26, 26))
        self.rect = self.image.get_rect()

        # Initialize position within the centered rectangle
        self.rect.x = random.randint(x_start, x_end - self.rect.width)
        self.rect.y = rect_y

    def update_position(self):
        self.rect.x += random.randint(-self.speed, self.speed)
        # Ensure the fish stays within the centered rectangle bounds
        self.rect.x = max(x_start, min(self.rect.x, x_end - self.rect.width))

    def __str__(self):
        return f"{self.name} costs {self.price}"


class Salmon(Fish, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Salmon", 10, 10, "images/salmon.png", 0.5)


class Cod(Fish, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("Cod", 5, 5, "images/cod.png", 0.5)
