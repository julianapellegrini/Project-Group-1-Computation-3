from utils import *
from config import *
from interfaces_menus.button import Button, select_sound



def victory_screen(screen, resolution, coins_earned, minutes, seconds, enemies_defeated, level, player, interface_w_save, interface_no_save):

    # Load the victory background image
    background1 = pygame.image.load(f"images/level{level}bg.png")
    background1 = pygame.transform.scale(background1, (width, height))

    background = pygame.image.load('images/textbg.png')
    background = pygame.transform.scale(background, (600, 600))
    background_rect = background.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # Play the sound effect
    powerup_sound = pygame.mixer.Sound('audio/level-completed.mp3')
    powerup_sound.set_volume(Button.sound_volume)
    powerup_sound.play()

    # Load the buttons images
    back_button = Button(resolution[0] // 2 - 70, 550, 140, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 27, True, light_brown, image='images/Wood-button1.png')
    next_level_button = Button(resolution[0] // 2 - 70, 450, 140, 60, "Next Level", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown, image='images/Wood-button1.png')

    # Set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 45)
    pixel_font_small = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)

    # Create victory content
    win_text = pixel_font.render("You Win!", True, (255, 255, 255))
    win_text_rect = win_text.get_rect(center=(resolution[0] // 2, resolution[1] // 3))

    coins_text = pixel_font_small.render(f"{coins_earned}", True, (255, 255, 255))
    coins_text_rect = coins_text.get_rect(center=(resolution[0] // 2, resolution[1] // 2.5))

    time_text = pixel_font_small.render(f"{int(minutes)}:{int(seconds)}", True, (255, 255, 255))
    time_text_rect = time_text.get_rect(center=(resolution[0] // 2, resolution[1] // 2.2))

    enemies_text = pixel_font_small.render(f"{enemies_defeated}", True, (255, 255, 255))
    enemies_text_rect = enemies_text.get_rect(center=(resolution[0] // 2, resolution[1] // 1.9))

    # Main loop to maintain the victory screen
    victory = True
    while victory:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if back_button.is_clicked(mouse_pos, ev):
                    select_sound()
                    from interfaces_menus.map import map_layout
                    victory = False
                    map_layout(player, interface_w_save, interface_no_save)
                    return
                elif next_level_button.is_clicked(mouse_pos, ev):
                    select_sound()
                    from interfaces_menus.map import map_layout
                    from game import game_loop
                    victory = False
                    game_loop(level + 1, player, map_layout, interface_w_save, interface_no_save)
                    return

        # Render the victory screen
        screen.blit(background1, (0, 0))
        screen.blit(background, background_rect)
        screen.blit(win_text, win_text_rect)
        screen.blit(coins_text, coins_text_rect)
        screen.blit(time_text, time_text_rect)
        screen.blit(enemies_text, enemies_text_rect)
        back_button.draw(screen, pygame.mouse.get_pos())
        next_level_button.draw(screen, pygame.mouse.get_pos())

        if back_button.is_hovered(pygame.mouse.get_pos()):
            back_button.scale_up()
        else:
            back_button.scale_down()

        if next_level_button.is_hovered(pygame.mouse.get_pos()):
            next_level_button.scale_up()
        else:
            next_level_button.scale_down()

        pygame.display.update()