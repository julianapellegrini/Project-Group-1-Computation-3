from utils import *
from config import *
from button import Button, select_sound


def weapon_selector():

    # set background
    background = pygame.image.load("images/weapon_selector_background.png")
    # scale background
    background = pygame.transform.scale(background, resolution)

    # set screen
    screen = pygame.display.set_mode(resolution)

    # set clock
    clock = pygame.time.Clock()

    # set buttons
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")
    select_button = Button(1000, (resolution[0] - 150) // 2, 150, 60, "Select", None, "chiller", 35, True, bice_blue,
                           image="images/ice-banner.png")

    arrow_left = Button(100, 300, 50, 50, "<", None, "chiller", 35, True, bice_blue,
                        image="images/arrow_left.png")
    arrow_right = Button(1200, 300, 50, 50, ">", None, "chiller", 35, True, bice_blue,
                         image="images/arrow_right.png")

    # set running
    running = True
    while running:

        # set fps
        clock.tick(fps)

        # display background
        screen.blit(background, (0, 0))

        # get mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            if select_button.is_clicked(mouse, ev):
                select_sound()
                under_construction()

            if arrow_left.is_clicked(mouse, ev):
                select_sound()
                under_construction()

            if arrow_right.is_clicked(mouse, ev):
                select_sound()
                under_construction()

            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            if select_button.is_hovered(mouse):
                select_button.scale_up()
            else:
                select_button.scale_down()

            if arrow_left.is_hovered(mouse):
                arrow_left.scale_up()
            else:
                arrow_left.scale_down()

            if arrow_right.is_hovered(mouse):
                arrow_right.scale_up()
            else:
                arrow_right.scale_down()

        # draw buttons
        back_button.draw(screen, mouse)
        select_button.draw(screen, mouse)
        arrow_left.draw(screen, mouse)
        arrow_right.draw(screen, mouse)

        pygame.display.update()
