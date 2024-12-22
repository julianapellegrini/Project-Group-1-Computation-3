from utils import *
from config import *
import random

# rectangle measurements

height_centered = 30

rect_width = resolution[0] * 2 // 3
rect_height = height_centered

rect_x = (resolution[0] - rect_width) // 2
rect_y = (resolution[1] - rect_height) // 2

# boundaries of the centered rectangle so that things don't go out of it
x_start = rect_x
x_end = rect_x + rect_width


# creating the fish class
class Fish(pygame.sprite.Sprite):
    """
    Fish class for the fishing minigame. Inherits from the pygame sprite class.

    Attributes:
    ----------
    name: str
        name of the fish
    price: int
        price of the fish
    speed: int
        speed of the fish
    image_path: str
        path to the image of the fish
    probability: float
        probability of the fish appearing
    image: pygame image
        image of the fish
    rect: pygame rect
        rectangle of the fish, used for positioning and collision detection
    """

    def __init__(self, name, price, speed, image_path, probability):
        """
        Initializes the fish object with the given attributes.

        Parameters:
        -----------
        name: str
            name of the fish
        price: int
            price of the fish
        speed: int
            speed of the fish
        image_path: str
            path to the image of the fish
        probability: float
            probability of the fish appearing
        """
        super().__init__()
        self.name = name
        self.price = price
        self.speed = speed
        self.probability = probability
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (26, 26))
        self.rect = self.image.get_rect()

        # spawn fish in the centered rectangle
        self.rect.x = random.randint(x_start, x_end - self.rect.width)
        self.rect.y = rect_y

    # move fish randomly
    def update_position(self):
        """
        Moves the fish randomly within the centered rectangle.

        Returns
        -------
        None
        """
        move = random.randint(-self.speed, self.speed)
        if move < 0:
            self.rect.x += move - 2
        else:
            self.rect.x += move + 2
        # keep fish within the centered rectangle
        self.rect.x = max(x_start, min(self.rect.x, x_end - self.rect.width))

    def __str__(self):
        """
        Returns the string representation of the fish object, including the name and price.

        Returns
        -------
        str
            String representation of the fish object.
        """
        return f"{self.name} costs {self.price}"


# defining the types of fish

class Salmon(Fish, pygame.sprite.Sprite):
    """
    Salmon class, inherits from the Fish class.

    Attributes:
    -----------
    Inherits all the attributes from the Fish class.
    """
    def __init__(self):
        """
        Initializes the Salmon object with the given attributes.

        Parameters:
        -----------
        None
        """
        super().__init__("Salmon", 10, 10, "images/salmon.png", 0.4)


class Cod(Fish, pygame.sprite.Sprite):
    """
    Cod class, inherits from the Fish class.

    Attributes:
    -----------
    Inherits all the attributes from the Fish class.
    """
    def __init__(self):
        """
        Initializes the Cod object with the given attributes.

        Parameters:
        -----------
        None
        """
        super().__init__("Cod", 5, 5, "images/cod.png", 0.4)


class ClownFish(Fish, pygame.sprite.Sprite):
    """
    ClownFish class, inherits from the Fish class.

    Attributes:
    -----------
    Inherits all the attributes from the Fish class.
    """
    def __init__(self):
        """
        Initializes the ClownFish object with the given attributes.

        Parameters:
        -----------
        None
        """
        super().__init__("Tuna", 15, 15, "images/clown_fish.png", 0.2)
