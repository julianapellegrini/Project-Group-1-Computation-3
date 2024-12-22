import pygame.image

from config import *
import math
from player_related.bullet import Bullet
from player_related.inventory import Inventory
from player_related.weapons import Snowball, Slingshot, Watergun, Fish_bazooka, Ice_Ninja_Stars, Sardine_Shooter
from powerups.extra_fish import Extra_Fish

ptypes = ['gray', 'brown', 'eyebrow']  # just for reference, not used


# creating the player class and making it a sprite
class Player(pygame.sprite.Sprite):

    """
    A class to represent the player in the game.

    Attributes:
    -----------
    ptype : str
        The type of penguin (default is 'gray').
    image_up : pygame.Surface
        The image of the player facing up.
    image_d_stop : pygame.Surface
        The image of the player facing down and stopped.
    image_d_1 : pygame.Surface
        The first image of the player facing down and moving.
    image_d_2 : pygame.Surface
        The second image of the player facing down and moving.
    image_l_1 : pygame.Surface
        The first image of the player facing left and moving.
    image_l_2 : pygame.Surface
        The second image of the player facing left and moving.
    image_r_1 : pygame.Surface
        The first image of the player facing right and moving.
    image_r_2 : pygame.Surface
        The second image of the player facing right and moving.
    image : pygame.Surface
        The current image of the player.
    rect : pygame.Rect
        The rectangle representing the player's position and size.
    speed_cap : int
        The maximum speed of the player.
    speed : int
        The current speed of the player.
    health_cap : int
        The maximum health of the player.
    health : int
        The current health of the player.
    bullet_cooldown : int
        The cooldown time for shooting bullets.
    level : int
        The current level of the player.
    """

    def __init__(self):

        """
        Initializes the Player with default attributes and images.

        This method sets up the player's images, position, speed, health, level, and inventory.
        """
        
        # calling the mother class' init
        super().__init__()

        self.ptype = 'gray'  # default penguin type

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

        # set the default image for before the player moves
        self.image = self.image_d_stop
        self.image = pygame.transform.scale(self.image, (player_size[0], player_size[1]))

        # player rectangle
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

        # GAMEPLAY VARIABLES
        self.speed_cap = 6
        self.speed = 6
        self.health_cap = 100
        self.health = 100
        self.bullet_cooldown = 0

        # what level the player is on
        self.level = 1  # default level is 1

        # giving the player an inventory
        self.inventory = Inventory()

        # player starts with a watergun in their inventory
        self.watergun = Watergun()
        self.inventory.add_item(self.watergun)

        # player has currency
        self.balance = 100  # starts with 100 coins as a little gift for the testers

        # weapons
        self.weapon = self.watergun  # default weapon

        # creates instances of all weapons so we can keep upgrades throughout the game
        self.snowball = Snowball()
        self.slingshot = Slingshot()
        self.fish_bazooka = Fish_bazooka()
        self.ice_ninja_stars = Ice_Ninja_Stars()
        self.sardine_shooter = Sardine_Shooter()

        # weapon upgrades keeps track of the upgrades for each weapon
        self.weapon_upgrades = {}

        # powerups
        self.powerup = None  # current powerup, default is None

        # powerup timer
        self.powerup_start = None

        # counter so we can cycle through the images for movement
        self.animation_counter = 0

    # function to load images so the skin change works
    def load_images(self):

        """
        Loads the images for different directions and states of the player.
        """
         
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

    # images for when powerup is active
    def load_images_pow(self):

        """
        Loads the images for the player when a powerup is active.

        This method sets up the player's images for different directions and states when a powerup is active, and scales them to the player's size.
        """

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

    # adds caught fish to the inventory
    def add_fish(self, fish):

        """
        Adds caught fish to the inventory.

        Parameters:
        -----------
        fish : object
            The fish object to be added to the inventory.
        """
        
        self.inventory.add_item(fish)

    # loads the player's data from the save file
    def load_data(self, data):

        """
        Loads the player's data from the save file.

        This method sets the player's attributes based on the saved data, including inventory, balance, level, type, health, speed, and weapon upgrades.

        Parameters:
        -----------
        data : list
            The list of data loaded from the save file.
        """
        
        # load player data from save file
        self.inventory.items = eval(data[0])
        self.balance = int(data[1])
        self.level = int(data[3])
        self.ptype = data[4]
        self.load_images()
        self.health_cap = int(data[5])
        self.speed_cap = int(data[6])

        # load the weapon
        weapon_name = data[2].split("(")[0]
        if weapon_name == "Snowball":
            self.weapon = Snowball()
        elif weapon_name == "Slingshot":
            self.weapon = Slingshot()
        elif weapon_name == "Watergun":
            self.weapon = Watergun()
        elif weapon_name == "Fish bazooka":
            self.weapon = Fish_bazooka()
        elif weapon_name == "Ice Ninja Stars":
            self.weapon = Ice_Ninja_Stars()
        elif weapon_name == "Sardine Shooter":
            self.weapon = Sardine_Shooter()

        # load damage for each weapon (so it doesn't lose upgrades)
        self.snowball.damage = float(data[7])
        self.slingshot.damage = float(data[8])
        self.fish_bazooka.damage = float(data[9])
        self.ice_ninja_stars.damage = float(data[10])
        self.sardine_shooter.damage = float(data[11])

        # load weapon upgrades
        self.weapon_upgrades = eval(data[12])

    # adds items to the inventory
    def add_item(self, item):

        """
        Adds items to the inventory.

        Parameters:
        -----------
        item : object
            The item object to be added to the inventory.
        """
        
        # Add the item to the inventory
        self.inventory.add_item(item)
        print(f"Added {item.name} to inventory")
        print(self.inventory.items)

    # changes the player's weapon
    def change_weapon(self, weapon):

        """
        Changes the player's weapon.

        Parameters:
        -----------
        weapon : object
            The new weapon object to be assigned to the player.
        """
        
        self.weapon = weapon

    # tracks movement and changes the player's image
    def update(self, surface):

        """
        Tracks movement and changes the player's image.

        This method updates the player's position and animation based on the keys pressed.

        Parameters:
        -----------
        surface : pygame.Surface
            The Pygame display surface.
        """

        # get the keys that are pressed
        keys = pygame.key.get_pressed()

        # add to animation counter
        self.animation_counter += 1

        # change the player's image based on the keys pressed
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

    # player shoots bullets in 4 directions periodically
    def shoot(self, bullets):
        
        """
        Player shoots bullets in 4 directions periodically.

        Parameters:
        -----------
        bullets : pygame.sprite.Group
            The group to which the bullets will be added.
        """

        if self.alive():
            # cooldown ==> how many frames I need until I can shoot again
            if self.bullet_cooldown <= 0:
                # defining the directions in which the bullets will fly
                # these 4 directions are, in order, right, left, up, down
                angles = [0, math.pi, math.pi / 2, 3 * math.pi / 2]

                # ff the extra fish powerup is active, add the diagonal angles
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

            # updates the cooldown
            self.bullet_cooldown -= 1

    # draws the player's health bar
    def draw_health_bar(self, surface):

        """
        Draws the player's health bar.

        Parameters:
        -----------
        surface : pygame.Surface
            The Pygame display surface.
        """

        # define the size and position of the health bar
        bar_width = self.rect.width
        bar_height = 10  # increase the height of the health bar
        bar_x = self.rect.x
        bar_y = self.rect.y - bar_height - 5  # adjust the position

        # ensure health does not go below 0 (into the negatives)
        health = max(self.health, 0)

        # calculate the health ratio
        health_ratio = health / 100

        # draw the background of the health bar
        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height), border_radius=5)

        # draw the foreground of the health bar (the green part)
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height), border_radius=5)

        # add the health ratio text in the middle of the health bar
        font = pygame.font.Font(None, 18)
        text = font.render(f'{int(health)}%', True, (255, 255, 255))
        text_rect = text.get_rect(center=(bar_x + bar_width // 2, bar_y + bar_height // 2))
        surface.blit(text, text_rect)

    def get_weapon_by_name(self, weapon_name):

        """
        Gets the weapon object by its name.

        Parameters:
        -----------
        weapon_name : str
            The name of the weapon.

        Returns:
        --------
        object
            The weapon object corresponding to the given name, or None if not found.
        """
        
        # map of weapon names to weapon objects
        weapon_map = {
            "Snowball": self.snowball,
            "Slingshot": self.slingshot,
            "Fish Bazooka": self.fish_bazooka,
            "Ice Ninja Stars": self.ice_ninja_stars,
            "Sardine Shooter": self.sardine_shooter
        }

        if weapon_name in weapon_map:
            return weapon_map[weapon_name]
        else:
            return None
