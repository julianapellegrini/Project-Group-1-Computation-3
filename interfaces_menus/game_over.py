from config import *
from interfaces_menus.button import Button, select_sound


def game_over(screen, resolution, coins_earned, minutes, seconds, enemies_defeated, level, player,
                   interface_w_save, interface_no_save):
    
    """
    Displays the game over screen.

    This function sets up a Pygame window with the game over message, statistics, and buttons for retrying or returning to the map.

    Parameters:
    -----------
    screen : pygame.Surface
        The Pygame display surface.
    resolution : tuple
        The resolution of the game window.
    coins_earned : int
        The number of coins earned by the player.
    minutes : int
        The number of minutes played.
    seconds : int
        The number of seconds played.
    enemies_defeated : int
        The number of enemies defeated by the player.
    level : int
        The level the player was on.
    player : object
        The player object.
    interface_w_save : function
        The function to call if a save file is present.
    interface_no_save : function
        The function to call if no save file is present.
    """
    
    # load the victory background image
    background1 = pygame.image.load(f"images/level{level}bg.png")
    background1 = pygame.transform.scale(background1, (width, height))

    background = pygame.image.load('images/textbg.png')
    background = pygame.transform.scale(background, (600, 600))
    background_rect = background.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # play the sound effect
    powerup_sound = pygame.mixer.Sound('audio/game-over.mp3')
    powerup_sound.set_volume(Button.sound_volume)
    powerup_sound.play()

    # load the buttons images
    retry = Button(resolution[0] // 2 - 70, 550, 140, 60, "Retry", brown, "fonts/Grand9KPixel.ttf", 27, True,
                        light_brown, image='images/Wood-button1.png')
    map = Button(resolution[0] // 2 - 70, 450, 140, 60, "Map", brown, "fonts/Grand9KPixel.ttf", 20,
                               True, light_brown, image='images/Wood-button1.png')

    # set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 45)
    pixel_font_small = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)

    # load icons
    snowflake_coin = pygame.image.load('images/snowflake_coin.png')
    snowflake_coin = pygame.transform.scale(snowflake_coin, (40, 40))

    icon_hourglass = pygame.image.load('images/icon_hourglass.png')
    icon_hourglass = pygame.transform.scale(icon_hourglass, (40, 40))

    icon_enemy = pygame.image.load('images/icon_enemy.png')
    icon_enemy = pygame.transform.scale(icon_enemy, (43, 43))

    # create victory content
    win_text = pixel_font.render("Game Over", True, oxford_blue)
    win_text_rect = win_text.get_rect(center=(resolution[0] // 2, resolution[1] // 4))

    coins_text = pixel_font_small.render(f"{coins_earned}", True, (255, 255, 255))
    coins_text_rect = coins_text.get_rect(center=(resolution[0] // 2.7, resolution[1] // 2.1))

    time_text = pixel_font_small.render(f"{int(minutes)}:{int(seconds)}", True, (255, 255, 255))
    time_text_rect = time_text.get_rect(center=(resolution[0] // 1.9, resolution[1] // 2.1))

    enemies_text = pixel_font_small.render(f"{enemies_defeated}", True, (255, 255, 255))
    enemies_text_rect = enemies_text.get_rect(center=(resolution[0] // 1.5, resolution[1] // 2.1))

    # main loop to maintain the victory screen
    victory = True
    while victory:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)

                if retry.is_clicked(mouse_pos, ev):
                    select_sound()
                    from interfaces_menus.map import map_layout
                    from game import game_loop
                    victory = False
                    game_loop(level, player, map_layout, interface_w_save, interface_no_save)
                    return
                elif map.is_clicked(mouse_pos, ev):
                    select_sound()
                    from interfaces_menus.map import map_layout
                    victory = False
                    map_layout(player, interface_w_save, interface_no_save)
                    return

        # render the victory screen
        screen.blit(background1, (0, 0))
        screen.blit(background, background_rect)
        screen.blit(win_text, win_text_rect)

        # draw icons and texts
        screen.blit(snowflake_coin, (coins_text_rect.left - 40, coins_text_rect.top + 5))
        screen.blit(coins_text, coins_text_rect)

        screen.blit(icon_hourglass, (time_text_rect.left - 40, time_text_rect.top))
        screen.blit(time_text, time_text_rect)

        screen.blit(icon_enemy, (enemies_text_rect.left - 43, enemies_text_rect.top - 3))
        screen.blit(enemies_text, enemies_text_rect)

        retry.draw(screen, pygame.mouse.get_pos())
        map.draw(screen, pygame.mouse.get_pos())

        if retry.is_hovered(pygame.mouse.get_pos()):
            retry.scale_up()
        else:
            retry.scale_down()

        if map.is_hovered(pygame.mouse.get_pos()):
            map.scale_up()
        else:
            map.scale_down()

        pygame.display.update()
