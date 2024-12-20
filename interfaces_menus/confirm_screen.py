from interfaces_menus.button import Button, select_sound
from config import *
from utils import *
from interfaces_menus.interface import *
from interfaces_menus.moving_bg import *

scroll = 0
# function to confirm player choice
def confirm():

    global scroll
    # set screen
    screen = pygame.display.set_mode(resolution)
    load_backgrounds()

    # create confirmation buttons
    yes_button = Button(400, 300, 150, 60, "Yes", brown, "fonts/Grand9KPixel.ttf", 35, True, light_brown, image="images/Wood-button1.png")
    no_button = Button(600, 300, 150, 60, "No", brown, "fonts/Grand9KPixel.ttf", 35, True, light_brown, image="images/Wood-button1.png")

    # set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 30)

    # create confirmation text
    text = pixel_font.render("Are you sure?", True, brown)

    # main loop
    while True:

        # get mouse position
        mouse = pygame.mouse.get_pos()

        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

        # draw text
        text_rect = text.get_rect(center=(575, 260))
        screen.blit(text, text_rect)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            # return True if yes is clicked, False if no or esc is clicked
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return False

            if yes_button.is_clicked(mouse, ev):
                select_sound()
                return True

            if no_button.is_clicked(mouse, ev):
                select_sound()
                return False

            # visuals for buttons
            if yes_button.is_hovered(mouse):
                yes_button.scale_up()
            else:
                yes_button.scale_down()

            if no_button.is_hovered(mouse):
                no_button.scale_up()
            else:
                no_button.scale_down()

        # draw buttons
        yes_button.draw(screen, mouse)
        no_button.draw(screen, mouse)

        pygame.display.update()
