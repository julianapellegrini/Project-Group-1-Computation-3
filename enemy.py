from config import *
import random
import math


# create the enemy class
class Enemy(pygame.sprite.Sprite):

    def __init__(self, enemy_type, max_health=10):
        super().__init__()
        # loading the image
        self.image1 = pygame.image.load(f'images_enemies/{enemy_type}1.png')
        self.image2 = pygame.image.load(f'images_enemies/{enemy_type}2.png')

        # scale images
        self.image1 = pygame.transform.scale(self.image1, (enemy_size[0], enemy_size[1]))
        self.image2 = pygame.transform.scale(self.image2, (enemy_size[0], enemy_size[1]))

        # set the default image
        self.image = self.image1

        # get rectangle for positioning
        self.rect = self.image.get_rect()

        # starting the enemy at a random valid location on the screen
        self.rect.x = random.randint(0, width - enemy_size[0])
        self.rect.y = random.randint(0, height - enemy_size[1])

        # setting a random initial speed for the enemy
        self.speed = random.randint(1, 3)

        # set the health bar
        self.health = max_health
        self.max_health = max_health

    # enemy movement and image update
    def update(self, player):
        """
        receiving the player as input so that we can assure the enemies move in the players' direction

        """

        # determining the direction of the movement based on the player_related location
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y

        # get the direction in radians
        direction = math.atan2(dy, dx)

        # move the enemy towards the player
        self.rect.x += self.speed * math.cos(direction)
        self.rect.y += self.speed * math.sin(direction)

        # image changes periodically
        if pygame.time.get_ticks() % 500 < 250:
            self.image = self.image1
        else:
            self.image = self.image2

    def draw_health_bar(self, surface):
        # define the size and position of the health bar
        bar_width = self.rect.width
        bar_height = 10
        bar_x = self.rect.x
        bar_y = self.rect.y - bar_height - 5

        # ensure health does not go below 0
        health = max(self.health, 0)

        # calculate the health ratio
        health_ratio = health / self.max_health

        # draw the background of the health bar
        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height), border_radius=5)

        # draw the foreground of the health bar
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height), border_radius=5)

        # add the health percentage text in the middle of the health bar
        font = pygame.font.Font(None, 18)
        health_percentage = int(health_ratio * 100)
        text = font.render(f'{health_percentage}%', True, (255, 255, 255))
        text_rect = text.get_rect(center=(bar_x + bar_width // 2, bar_y + bar_height // 2))
        surface.blit(text, text_rect)


# create the enemy types


class Seal(Enemy):
    def __init__(self):
        super().__init__(enemy_type='cinza', max_health=8)
        self.speed = 3


class Seal2(Enemy):
    def __init__(self):
        super().__init__(enemy_type='marrom', max_health=13)
        self.speed = 3


class Seal_with_a_hat(Enemy):
    def __init__(self):
        super().__init__(enemy_type='pirata', max_health=20)
        self.speed = random.randint(1, 2)


class Polar_bear(Enemy):
    def __init__(self):
        super().__init__(enemy_type='urso', max_health=25)
        self.speed = random.randint(1, 2)

        # should be bigger than the seals
        self.image1 = pygame.transform.scale(self.image1, (enemy_size[0] * 2, enemy_size[1] * 2))
        self.image2 = pygame.transform.scale(self.image2, (enemy_size[0] * 2, enemy_size[1] * 2))


class Orca(Enemy):
    def __init__(self):
        super().__init__(enemy_type='orca', max_health=50)
        self.speed = 1

        # bigger than the seals
        self.image1 = pygame.transform.scale(self.image1, (enemy_size[0] * 2, enemy_size[1] * 2))
        self.image2 = pygame.transform.scale(self.image2, (enemy_size[0] * 2, enemy_size[1] * 2))
