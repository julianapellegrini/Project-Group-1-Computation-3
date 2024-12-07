from interfaces_menus.button import Button, select_sound
from config import *
from utils import *


# function to confirm player choice
def confirm():

    # set screen
    screen = pygame.display.set_mode(resolution)

    # scale and set background
    background = pygame.image.load('images/menu.png')
    background = pygame.transform.scale(background, resolution)

    # create confirmation buttons
    yes_button = Button(400, 300, 150, 60, "Yes", None, "chiller", 35, True, bice_blue, image="images/ice-banner.png")
    no_button = Button(600, 300, 150, 60, "No", None, "chiller", 35, True, bice_blue, image="images/ice-banner.png")

    # set font
    chiller_font = pygame.font.SysFont("chiller", 30)

    # create confirmation text
    text = chiller_font.render("Are you sure?", True, bice_blue)

    # main loop
    while True:

        # get mouse position
        mouse = pygame.mouse.get_pos()

        # draw background
        screen.blit(background, (0, 0))

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
