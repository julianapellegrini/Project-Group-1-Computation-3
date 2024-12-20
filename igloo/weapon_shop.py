from utils import *
from interfaces_menus.button import Button, select_sound


def weapon_shop(player):

    pygame.init()
    screen = pygame.display.set_mode(resolution)

    # setting up the background
    background = pygame.image.load('images/textbg.png')
    background = pygame.transform.scale(background, resolution)

    # setting up buttons
    back_button = Button(950, 600, 200, 100, "Back", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown,
                         image="images/Wood-button1.png")

    while True:
        # displaying the background
        screen.blit(background, (0, 0))

        # get player's mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return
            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            # putting visual effects on buttons
            if back_button.is_hovered(pygame.mouse.get_pos()):
                back_button.scale_up()
            else:
                back_button.scale_down()

        # draw the button after updating
        back_button.draw(screen, mouse)

        # update the display
        pygame.display.update()
