from config import *
import pygame
from player import Player
from enemy import Seal, Seal2, Seal_with_a_hat, Polar_bear, Orca  # Import new enemy types
import random
from powerups.despawner import DeSpawner
from pause import pause_screen
from powerups.speed_boost import Speed_Boost
from powerups.extra_fish import Extra_Fish

# initializing pygame
pygame.init()




def game_loop(level):
    """
    Main game loop that handles gameplay for different levels.
    :param level: The current level the player is playing.
    """
    # Setup:
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
    player_group.add(player)

    # creating an empty bullet group that will be given as input to the player.shoot() method
    bullets = pygame.sprite.Group()

    # creating an enemy group
    enemies = pygame.sprite.Group()

    # setting up enemy cooldown and spawn rates
    enemy_cooldown = 0
    spawn_chances = {
        Seal: 0.4,  # 0.4 chance to spawn the base enemy
        Seal2: 0.3 if level >= 2 else 0.0,     # 0.3 chance to spawn level 2 enemy
        Seal_with_a_hat: 0.2 if level >= 3 else 0.0,  # 20% chance starting from level 2
        Polar_bear: 0.1 if level >= 4 else 0.0,  # 10% chance starting from level 3
    }

    # Initialize mini-boss cooldown
    mini_boss_cooldown = fps * 30  # Mini-boss spawns every 30 seconds

    # Load the pause button image
    pause_button_image = pygame.image.load('images/pause_button.png')
    pause_button_image = pygame.transform.scale(pause_button_image, (70, 70))
    pause_button_position = (resolution[0] - pause_button_image.get_width() - 10, 10)


    # Settings for powerups
    POWERUP_SPAWN_INTERVAL = 5000  # 5 seconds in milliseconds
    last_powerup_spawn_time = pygame.time.get_ticks()
    powerup_group = pygame.sprite.Group() 
    despawner_probability = 0.6 #40% to get
    speed_boost_probability = 0.3 #30% to get
    invincibility_probability = 0.12 #18% to get
    extra_fish_probability = 0 # 12% to get

    
    
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
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (pause_button_position[0] <= mouse_pos[0] <= pause_button_position[0] + pause_button_image.get_width() and
                        pause_button_position[1] <= mouse_pos[1] <= pause_button_position[1] + pause_button_image.get_height()):
                    pause_screen(screen, resolution)
            
        # Check if it's time to spawn a powerup
        current_time = pygame.time.get_ticks()
        if current_time - last_powerup_spawn_time >= POWERUP_SPAWN_INTERVAL:
            prob = random.random()
            if prob >= despawner_probability:
                new_powerup = DeSpawner()
                powerup_group.add(new_powerup)
            elif prob() >= invincibility_probability and prob < despawner_probability:
                new_powerup = DeSpawner(0.5)
                powerup_group.add(new_powerup)
            elif prob >= speed_boost_probability and prob < invincibility_probability:
                new_powerup = SpeedBoost()
                powerup_group.add(new_powerup)
            elif prob >= extra_fish_probability and prob < speed_boost_probability:
                new_powerup = Extra_Fish()
                powerup_group.add(new_powerup)
            last_powerup_spawn_time = current_time  # Reset the timer
    

        for powerup in powerup_group:
            powerup.draw(screen)
            if pygame.sprite.collide_rect(player, powerup):
                powerup.affect_player(player)
                powerup.affect_game()
                
                
            
        # automatically shoot bullets from the player
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
        player_group.update()
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

        # checking for collisions between player and enemies
        for enemy in enemies:
            if pygame.sprite.collide_rect(player, enemy):
                # If the player is not invincible, reduce health
                if not player.invincible:
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
