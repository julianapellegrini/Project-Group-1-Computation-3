from config import *
import pygame
from enemy import Seal, Seal2, Seal_with_a_hat, Polar_bear, Orca  # Import new enemy types
import random
from powerups.despawner import DeSpawner
from powerups.speed_boost import Speed_Boost
from powerups.extra_fish import Extra_Fish
from powerups.invincibility import Invincibility
from interfaces_menus.pause import pause_screen
from chest import Chest
from interfaces_menus.victory_screen import victory_screen
from interfaces_menus.game_over import game_over

# initializing pygame
pygame.init()


# main game loop
def game_loop(level, player, map_layout, interface_w_save, interface_no_save):
    
    """
    Main game loop that handles gameplay for different levels.

    Parameters:
    -----------
    level : int
        The current level the player is playing.
    player : object
        The player object.
    map_layout : function
        The function to call to display the map layout.
    interface_w_save : function
        The function to call if a save file is present.
    interface_no_save : function
        The function to call if no save file is present.
    """
    

    # importing the global variables for music and sound volume
    from interfaces_menus.interface import music_volume, sound_volume
    global music_volume
    global sound_volume

    # setting up the background:
    background = pygame.image.load(f"images/level{level}bg.png")
    background = pygame.transform.scale(background, (width, height))

    # loading the music and setting the volume
    pygame.mixer.music.load("audio/battle-music.mp3")
    pygame.mixer.music.set_volume(music_volume)
    pygame.mixer.music.play(loops=-1)

    # using the clock to control the time frame
    clock = pygame.time.Clock()

    # screen setup:
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Endless Wilderness Explorer")

    # setting up the player_related group
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # creating an empty bullet group that will be given as input to the player's shoot method
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

    # initialize mini-boss cooldown
    mini_boss_cooldown = fps * 30  # mini-boss spawns every 30 seconds

    # load the pause button image
    pause_button_image = pygame.image.load('images/pause_button.png')
    pause_button_image = pygame.transform.scale(pause_button_image, (70, 70))
    pause_button_position = (resolution[0] - pause_button_image.get_width() - 10, 10)

    # load the image of coin
    coin_image = pygame.image.load("images/snowflake_coin.png")
    coin_image = pygame.transform.scale(coin_image, (25, 25))

    # GAME VARIABLES

    # timer variables
    minutes = 0
    seconds = 0

    # enemies defeated
    enemies_defeated = 0

    # coins earned
    coins_earned = 0

    # current enemies on screen to establish a limit
    current_enemies = 0

    # fonts
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 50)
    pixel_font_small = pygame.font.Font("fonts/Grand9KPixel.ttf", 20)

    # settings for powerups
    powerup_spawn_interval = 10000  # every 10 seconds
    last_powerup_spawn_time = pygame.time.get_ticks()
    powerup_group = pygame.sprite.Group()

    # powerups
    powerup_types = [DeSpawner, Speed_Boost, Extra_Fish, Invincibility]

    # powerup select function
    def select_powerup():

        """
        Selects a powerup based on their probabilities.

        Returns:
        --------
        object
            The selected powerup object.
        """
        
        # choice function with weights to select a powerup
        selected_powerup = random.choices(powerup_types, [i().probability for i in powerup_types])[0]
        return selected_powerup()

    # settings for chests
    chest_spawn_interval = 10000  # 10% to chance every 20 seconds
    last_chest_spawn_time = pygame.time.get_ticks()
    chest_group = pygame.sprite.Group()
    chest_spawn_probability = 0.1  # 10% chance to spawn a chest every x seconds

    # MAIN GAME LOOP
    running = True
    while running:

        # controlling the frame rate
        clock.tick(fps)

        # setting up the background
        screen.blit(background, (0, 0))

        # draw coins text
        coins_text = pixel_font_small.render(f"Coins: {coins_earned}", True, oxford_blue)
        screen.blit(coins_text, (10, 10))

        # draw timer text
        timer_text = pixel_font_small.render(f"Time: {int(minutes)}:{int(seconds)}", True, oxford_blue)
        screen.blit(timer_text, (10, 60))

        # draw enemies defeated text
        enemy_defeated_text = pixel_font_small.render(f"Enemies defeated: {enemies_defeated}", True, oxford_blue)
        screen.blit(enemy_defeated_text, (10, 110))

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

        # check if it's time to spawn a new chest
        current_time_chest = pygame.time.get_ticks()
        if current_time_chest - last_chest_spawn_time > chest_spawn_interval:
            if random.random() < chest_spawn_probability:  # check if chest should spawn based on probability
                chest_group.empty()  # clear the chest group so only one chest is on screen at a time
                chest = Chest()  # create a new Chest object
                chest.spawn(screen)  # set its position and draw it
                chest_group.add(chest)  # add it to the chest group
            last_chest_spawn_time = current_time_chest  # update the last time a chest was spawned

        # draw all chests
        for chest in chest_group:
            chest.spawn(screen)
            if chest.rect.colliderect(player.rect):
                chest.open(screen, enemies, spawn_chances, player)
                chest_group.remove(chest)

        # check if it's time to spawn a powerup
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
        
        for powerup in powerup_group:
            # draw the powerup on the screen
            powerup.spawn(screen)
            if powerup.rect.colliderect(player.rect):
                if player.powerup is None:
                    # start timer
                    player.powerup_start = pygame.time.get_ticks()
                    if not isinstance(powerup, DeSpawner):
                        powerup.affect_player(screen, player)
                        player.powerup = powerup
                    else:
                        enemies_despawned = powerup.affect_game(screen, enemies, spawn_chances, player)
                        current_enemies -= enemies_despawned
                        player.powerup = powerup

                    # play the sound effect
                    powerup_sound = pygame.mixer.Sound('audio/power-up.mp3')
                    powerup_sound.set_volume(sound_volume)
                    powerup_sound.play()
                        
                    # remove the powerup from the group
                    powerup_group.remove(powerup)
                else:
                    print("Player already has a powerup")

        # check if the powerup has been active for the specified duration
        if player.powerup is not None:
            current_time_powerup = pygame.time.get_ticks()  # Initialize current_time_powerup
            if (current_time_powerup - player.powerup_start >= player.powerup.duration * 1000):  # Convert duration to milliseconds
                if isinstance(player.powerup, DeSpawner):
                    player.powerup.deactivate(spawn_chances, player)
                else:
                    player.powerup.deactivate(player)
                player.powerup = None
        
        # draw the invincibility image if the player is invincible
        if isinstance(player.powerup, Invincibility) and player.powerup.active:
            player.powerup.update_position(player)
            screen.blit(player.powerup.image, player.powerup.image_rect.topleft)
        # draw the speed boost image if the player has speed boost
        elif isinstance(player.powerup, Speed_Boost) and player.powerup.active:
            player.powerup.update_position(player)
            screen.blit(player.powerup.image, player.powerup.image_rect.topleft)
        elif isinstance(player.powerup, DeSpawner) and player.powerup.active:
            player.powerup.update_position(player)
            screen.blit(player.powerup.image, player.powerup.image_rect.topleft)

        # automatically shoot bullets from the player
        player.shoot(bullets)

        # spawn enemies
        if enemy_cooldown <= 0 and current_enemies < 5:
            enemy_type = random.choices(list(spawn_chances.keys()), list(spawn_chances.values()))[0]
            enemy = enemy_type()
            enemies.add(enemy)
            current_enemies += 1
            enemy_cooldown = fps * 2  # spawn every 2 seconds

        # spawn a mini-boss
        if mini_boss_cooldown <= 0 and level >= 4:
            mini_boss = Orca()
            enemies.add(mini_boss)
            mini_boss_cooldown = fps * 30  # Reset cooldown

        # update cooldowns
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
            bullet.draw(screen,player)

        # checking for collisions between bullets and enemies
        for bullet in bullets:
            collided_enemies = pygame.sprite.spritecollide(bullet, enemies, False)
            for enemy in collided_enemies:
                enemy.health -= player.weapon.damage
                bullet.kill()
                if enemy.health <= 0:

                    # play the sound effect for killing an enemy
                    powerup_sound = pygame.mixer.Sound('audio/kill-noise.mp3')
                    powerup_sound.set_volume(sound_volume)
                    powerup_sound.play()

                    # remove the enemy then add to game and player variables
                    enemy.kill()
                    coins_earned += 5
                    enemies_defeated += 1
                    current_enemies -= 1

        # checking for collisions between player and enemies
        for enemy in enemies:
            if pygame.sprite.collide_rect(player, enemy):
                # if the player is not invincible, reduce health
                if not isinstance(player.powerup, Invincibility):
                    player.health -= 0.3
                if player.health <= 0:
                    # when player loses restore health and call game over screen
                    player.health = player.health_cap
                    game_over(screen, resolution, coins_earned, minutes, seconds, enemies_defeated, level, player, interface_w_save, interface_no_save)
                    return

        # draw health bars
        player.draw_health_bar(screen)
        for enemy in enemies:
            enemy.draw_health_bar(screen)

        # draw the pause button
        screen.blit(pause_button_image, pause_button_position)

        # update timer
        if seconds == 59:
            minutes += 1
            seconds = 0
        else:
            seconds += 1 / fps

        # END GAME CONDITIONS
        if enemies_defeated >= level * 5 or minutes >= level * 2:
            player.balance += coins_earned
            if level == player.level:
                player.level += 1
            player.health = player.health_cap
            player.speed = player.speed_cap

            # call the victory screen
            victory_screen(screen, resolution, coins_earned, minutes, seconds, enemies_defeated, level, player, interface_w_save, interface_no_save)

            return

        # update display
        pygame.display.flip()

    pygame.quit()
