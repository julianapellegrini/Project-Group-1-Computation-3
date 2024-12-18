from config import *
import pygame
from enemy import Seal, Seal2, Seal_with_a_hat, Polar_bear, Orca  # Import new enemy types
import random
from powerups.despawner import DeSpawner
from powerups.speed_boost import Speed_Boost
from powerups.extra_fish import Extra_Fish
from powerups.invincibility import Invincibility
from interfaces_menus.pause import pause_screen
import time
from chest import Chest

# initializing pygame
pygame.init()


def game_loop(level, player, map_layout, interface_w_save, interface_no_save):
    """
    Main game loop that handles gameplay for different levels.
    :param player: keep same player_related instance throughout the game in order to be able to save the
    player's progress.
    :param level: The current level the player_related is playing.
    """
    # Setup:
    # setting up the background:
    background = pygame.image.load("images/ice-background2.png")
    background = pygame.transform.scale(background, (width, height))

    pygame.mixer.music.load("audio/nocturne-of-ice.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    # using the clock to control the time frame
    clock = pygame.time.Clock()

    # screen setup:
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Endless Wilderness Explorer")

    # setting up the player_related group
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # creating an empty bullet group that will be given as input to the player_related.shoot() method
    bullets = pygame.sprite.Group()

    # creating an enemy group
    enemies = pygame.sprite.Group()

    # setting up enemy cooldown and spawn rates
    enemy_cooldown = 0
    spawn_chances = {
        Seal: 0.4,  # 0.4 chance to spawn the base enemy
        Seal2: 0.3 if level >= 2 else 0.0,  # 0.3 chance to spawn level 2 enemy
        Seal_with_a_hat: 0.2 if level >= 3 else 0.0,  # 20% chance starting from level 2
        Polar_bear: 0.1 if level >= 4 else 0.0,  # 10% chance starting from level 3
    }

    # Initialize mini-boss cooldown
    mini_boss_cooldown = fps * 30  # Mini-boss spawns every 30 seconds

    # Load the pause button image
    pause_button_image = pygame.image.load('images/pause_button.png')
    pause_button_image = pygame.transform.scale(pause_button_image, (70, 70))
    pause_button_position = (resolution[0] - pause_button_image.get_width() - 10, 10)

    # Balance text
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 50)
    balance_text = pixel_font.render(f"Balance: {player.balance}", True, (255, 255, 255))

    # Settings for powerups
    powerup_spawn_interval = 10000  # every 10 seconds
    last_powerup_spawn_time = pygame.time.get_ticks()
    powerup_group = pygame.sprite.Group()

    # powerups
    # powerup_types = [DeSpawner, Speed_Boost, Extra_Fish, Invincibility]
    powerup_types = [Invincibility, Extra_Fish, DeSpawner]  # temporary while others aren't done

    # powerup spawn function
    def select_powerup():
        # choice function with weights to select a powerup
        selected_powerup = random.choices(powerup_types, [i().probability for i in powerup_types])[0]
        return selected_powerup()

    # Settings for chests
    chest_spawn_interval = 3000  # 20% to chance every 20 seconds
    last_chest_spawn_time = pygame.time.get_ticks()
    chest_group = pygame.sprite.Group()
    chest_spawn_probability = 0.2  # 5% chance to spawn a chest every x seconds

    # MAIN GAME LOOP
    running = True
    while running:

        # controlling the frame rate
        clock.tick(fps)

        # setting up the background
        screen.blit(background, (0, 0))

        # draw balance text
        balance_text = pixel_font.render(f"Balance: {player.balance}", True, (255, 255, 255))
        screen.blit(balance_text, (10, 10))

        # handling events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (pause_button_position[0] <= mouse_pos[0] <= pause_button_position[
                    0] + pause_button_image.get_width() and
                        pause_button_position[1] <= mouse_pos[1] <= pause_button_position[
                            1] + pause_button_image.get_height()):
                    pause_screen(screen, resolution, player, map_layout, interface_w_save, interface_no_save)

        # Check if it's time to spawn a new chest
        current_time_chest = pygame.time.get_ticks()
        if current_time_chest - last_chest_spawn_time > chest_spawn_interval:
            if random.random() < chest_spawn_probability:  # Check if chest should spawn based on probability
                chest = Chest()  # Create a new Chest object
                chest.spawn(screen)  # Set its position and draw it
                chest_group.add(chest)  # Add it to the chest group
            last_chest_spawn_time = current_time_chest  # Update the last chest spawn time

        # Draw all chests
        for chest in chest_group:
            chest.spawn(screen)
            if chest.rect.colliderect(player.rect):
                chest.open(screen, enemies, spawn_chances, player)
                chest_group.remove(chest)

        # Check if it's time to spawn a powerup
        current_time_powerup_icon = pygame.time.get_ticks()
        if current_time_powerup_icon - last_powerup_spawn_time >= powerup_spawn_interval:
            # use select_powerup() to get a powerup
            new_powerup = select_powerup()
            # clear the powerup group and add the new powerup
            powerup_group.empty()
            powerup_group.add(new_powerup)
            # draw the powerup on the screen
            for powerup in powerup_group:
                powerup.spawn(screen)
            # set the last powerup spawn time to the current time
            last_powerup_spawn_time = current_time_powerup_icon

        current_time_powerup = pygame.time.get_ticks()
        for powerup in powerup_group:
            # draw the powerup on the screen
            powerup.spawn(screen)
            if powerup.rect.colliderect(player.rect):
                if player.powerup is None:
                    # start timer

                    player.powerup_start = pygame.time.get_ticks()
                    # set player powerup to the powerup and affect the player and game
                    player.powerup = powerup
                    if powerup != DeSpawner():
                        powerup.affect_player(screen, player)
                    else:
                        powerup.affect_game(screen, enemies, spawn_chances, player)
                    # remove the powerup from the group
                    powerup_group.remove(powerup)
                else:
                    print("Player already has a powerup")

        if player.powerup and current_time_powerup - player.powerup_start >= player.powerup.duration:
            if player.powerup == DeSpawner():
                player.powerup.deactivate(player,spawn_chances)
            else:
                player.powerup.deactivate(player)
            player.powerup = None


        # automatically shoot bullets from the player_related
        player.shoot(bullets)

        # spawn enemies
        if enemy_cooldown <= 0:
            enemy_type = random.choices(list(spawn_chances.keys()), list(spawn_chances.values()))[0]
            enemy = enemy_type()
            enemies.add(enemy)
            enemy_cooldown = fps * 2  # Spawn every 2 seconds

        # Spawn a mini-boss
        if mini_boss_cooldown <= 0 and level >= 4:
            mini_boss = Orca()
            enemies.add(mini_boss)
            mini_boss_cooldown = fps * 30  # Reset cooldown

        # Update cooldowns
        enemy_cooldown -= 1
        mini_boss_cooldown -= 1

        # updating groups
        player_group.update(screen)
        bullets.update()
        enemies.update(player)

        # drawing entities
        player_group.draw(screen)
        enemies.draw(screen)

        # drawing the bullet sprites:
        for bullet in bullets:
            bullet.draw(screen)

        # checking for collisions between bullets and enemies
        for bullet in bullets:
            collided_enemies = pygame.sprite.spritecollide(bullet, enemies, False)
            for enemy in collided_enemies:
                enemy.health -= 5
                bullet.kill()
                if enemy.health <= 0:
                    enemy.kill()
                    player.balance += 5

        # checking for collisions between player_related and enemies
        for enemy in enemies:
            if pygame.sprite.collide_rect(player, enemy):
                # If the player_related is not invincible, reduce health
                if player.powerup != Invincibility():
                    player.health -= 0.3
                if player.health <= 0:
                    pygame.quit()
                    return

        # draw health bars
        player.draw_health_bar(screen)
        for enemy in enemies:
            enemy.draw_health_bar(screen)

        # draw the pause button
        screen.blit(pause_button_image, pause_button_position)

        # update display
        pygame.display.flip()

    pygame.quit()
