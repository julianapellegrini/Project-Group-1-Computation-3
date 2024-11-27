from config import *
import math
import pygame
from player import Player
from enemy import Enemy
from shed import shed
<<<<<<< Updated upstream
=======
import random
from powerup import PowerUp
from invincibility import Invincibility
from despawner import DeSpawner

#initializd pygame
pygame.init()

# Define the probability of power-up appearance
invincibility_probability = 0.7

# Initialize power-ups
invincibility_powerup = Invincibility(duration=10000)  # 10 seconds


# Initial spawn rate for power ups
spawn_rate = 1.0

# Set up a timer event for every 5 seconds (5000 milliseconds)
invincibility_event = pygame.USEREVENT + 1
pygame.time.set_timer(invincibility_event, 5000)
invincibility_deactivation_event = pygame.USEREVENT + 2


>>>>>>> Stashed changes


def game_loop():
    # creating the player for the game:
    player = Player()

    # by default i start the game in the main area
    current_state = "main"

    # "endless" game loop:
    while True:
        if current_state == "main":
            current_state = execute_game(player)
        elif current_state == "shed":
            current_state = shed(player)


def execute_game(player):

    # setup:

    # setting up the background:
    background = pygame.image.load("images/ice-background2.png")
    background = pygame.transform.scale(background, (width, height))

    # using the clock to control the time frame
    clock = pygame.time.Clock()

    # screen setup:
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Endless Wilderness Explorer")

    # setting up the player
    player = Player()
    player_group = pygame.sprite.Group()

    # adding the player to the group
    player_group.add(player)

    # creating an empty bullet group that will be given as input to the player.shoot() method
    bullets = pygame.sprite.Group()

    # creating an enemy group
    enemies = pygame.sprite.Group()

    # before starting our main loop, setup the enemy cooldown
    enemy_cooldown = 0

    # MAIN GAME LOOP

    running = True

    while running:

        # controlling the frame rate
        clock.tick(fps)

        # setting up the background
        screen.blit(background, (0,0))

        # handling events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # automatically shoot bullets from the player
        player.shoot(bullets)

        # spawning enemies every two seconds
        if enemy_cooldown <= 0:
            # creating an enemy
            enemy = Enemy()

            # adding the enemy to the group
            enemies.add(enemy)

            enemy_cooldown = fps * 2

            # in bullets, we use fps to spawn every second. Here we double that to spawn every 2 seconds

        # updating the enemy cooldown
        enemy_cooldown -= 1

        # updating positions and visuals:
        # calling the .update( method of all the instance in the player group
        player_group.update()

        # updating the bullets and enemy groups
        bullets.update()
        enemies.update(player)

        # checking if the player moved off-screen from the right to the next area
        if player.rect.right >= width:
            return "shed"

        # drawing the bullet sprites on the screen
        player_group.draw(screen)
        enemies.draw(screen)

        # drawing the bullet sprites:
        for bullet in bullets:
            bullet.draw(screen)

        # checking for collisions between player bullets and enemies
        for bullet in bullets:
            collided_enemies = pygame.sprite.spritecollide(bullet, enemies, False)

            for enemy in collided_enemies:

                # every hit enemy needs to lose life...
                # every bullet hit will reduce the life by 5hp
                enemy.health -= 5

                # removing the bullet from the screen (as it's lodged in the enemy's heart)
                bullet.kill()

                # checking if enemy is dead
                if enemy.health <= 0:
                    enemy.kill()

        pygame.display.flip()

    # the main while game loop has terminated and the game ends
    pygame.quit()
