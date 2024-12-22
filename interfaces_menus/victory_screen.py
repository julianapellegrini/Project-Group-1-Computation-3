from utils import *
from config import *
from interfaces_menus.button import Button, select_sound


def victory_screen(screen, resolution, coins_earned, minutes, seconds, enemies_defeated):
    # Load the victory background image
    background1 = pygame.image.load("images/ice-background2.png")
    background1 = pygame.transform.scale(background1, (width, height))

    background = pygame.image.load('images/textbg.png')
    background = pygame.transform.scale(background, (600, 600))
    background_rect = background.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # Load the buttons images
    play_button = Button(resolution[0] // 2 - 70, resolution[1] // 1.5, 140, 140, "", None, None, 0, False, None,
                         'images/play_button.png')

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
                if play_button.is_clicked(mouse_pos, ev):
                    select_sound()
                    victory = False

        # Render the victory screen
        screen.blit(background1, (0, 0))
        screen.blit(background, background_rect)
        screen.blit(win_text, win_text_rect)
        screen.blit(coins_text, coins_text_rect)
        screen.blit(time_text, time_text_rect)
        screen.blit(enemies_text, enemies_text_rect)
        play_button.draw(screen, pygame.mouse.get_pos())

        # Putting visual effects on buttons
        if play_button.is_hovered(pygame.mouse.get_pos()):
            play_button.scale_up()
        else:
            play_button.scale_down()

        pygame.display.update()
