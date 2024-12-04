

from config import *
import math
import pygame
from player import Player
from enemy import Enemy
from shed import shed
import random
from powerup import PowerUp
from invincibility import Invincibility
from despawner import DeSpawner
from pause import pause_screen

# initializing pygame
pygame.init()

# Settings of the powerups
POWERUP_ICON_DURATION = 5000  # 5 seconds in milliseconds
POWERUP_ICON_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(POWERUP_ICON_EVENT, POWERUP_ICON_DURATION)  # Set up a timer event for every 10 seconds (10000 milliseconds)
invincibility_probability = 1 #FOR TESTING PURPOSES
#POWERUP_DEACTIVATION_EVENT = pygame.USEREVENT + 2
# Initialize power-ups
invincibility_powerup = Invincibility()

def game_loop():
    # creating the player for the game:
    player = Player()

    # by default i start the game in the map area
    current_state = "main"

    # "endless" game loop:
    while True:
        if current_state == "main":
            current_state = execute_game(player)


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

    # creating a powerup group
    powerups = pygame.sprite.Group()

    # before starting our main loop, setup the enemy cooldown
    enemy_cooldown = 0

    # Load the pause button image
    pause_button_image = pygame.image.load('images/pause_button.png')
    pause_button_image = pygame.transform.scale(pause_button_image, (70, 70))
    pause_button_position = (resolution[0] - pause_button_image.get_width() - 10, 10)

    # MAIN GAME LOOP
    running = True

    while running:

        # controlling the frame rate
        clock.tick(fps)

        # setting up the background
        screen.blit(background, (0, 0))

        # handling events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (pause_button_position[0] <= mouse_pos[0] <= pause_button_position[0] + pause_button_image.get_width() and
                        pause_button_position[1] <= mouse_pos[1] <= pause_button_position[1] + pause_button_image.get_height()):
                    pause_screen(screen, resolution)
            # Check for power-up appearance
            elif event.type == POWERUP_ICON_EVENT:
                prob = random.random()
                if prob < invincibility_probability:
                    powerup_type = invincibility_powerup
                    powerup_type.draw(screen)
                    

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
        #if player.rect.right >= width:
        #    return "shed"

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

        # checking for collisions between player and enemies
        for enemy in enemies:
            collided_player = pygame.sprite.spritecollide(player, enemies, False)
            for enemy in collided_player:
                player.health -= 0.3

                # OR
                # player.health -= 20
                # enemy.kill()

                if player.health <= 0:
                    player.kill()
                    pygame.quit()

        # Draw the player's health bar
        player.draw_health_bar(screen)
        # Draw enemy health bar
        for enemy in enemies:
            enemy.draw_health_bar(screen)

        # Update player
        player.update()

        # Draw player
        screen.blit(player.image, player.rect.topleft)

        # Draw the pause button
        screen.blit(pause_button_image, pause_button_position)

        pygame.display.flip()

    # the main while game loop has terminated and the game ends
    pygame.quit()

