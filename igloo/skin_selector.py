from utils import *
from config import *
from interfaces_menus.button import Button, select_sound


def skin_selector(player):

    # set background
    background = pygame.image.load("images/chest_background.png")
    # scale background
    background = pygame.transform.scale(background, resolution)

    # set screen
    screen = pygame.display.set_mode(resolution)

    # set clock
    clock = pygame.time.Clock()

    # set buttons
    back_button = Button(1000, 650, 150, 60, "Back", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                         image="images/ice-banner.png")
    select_button = Button((resolution[0] - 150) // 2, 600, 150, 60, "Select", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                           image="images/ice-banner.png")

    arrow_left = Button(100, 300, 200, 200, None, None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                        image="images/arrow_left.png")
    arrow_right = Button(1000, 300, 200, 200, None, None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                         image="images/arrow_right.png")

    # list of penguin types
    ptypes = ['gray', 'brown', 'eyebrow']

    # penguin images
    penguin_images = [pygame.image.load(f'images_penguins/{ptype}up.png') for ptype in ptypes]

    # tracker for current weapon
    selector_current = 0

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
                pygame.quit()

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            if select_button.is_clicked(mouse, ev):
                select_sound()
                player.ptype = ptypes[selector_current]
                player.load_images()
                print(player.ptype)

            if arrow_left.is_clicked(mouse, ev):
                select_sound()
                if selector_current > 0:
                    selector_current -= 1
                else:
                    selector_current = len(ptypes) - 1

            if arrow_right.is_clicked(mouse, ev):
                select_sound()
                if selector_current < len(ptypes) - 1:
                    selector_current += 1
                else:
                    selector_current = 0

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

        # draw penguin image according to the selector_current
        screen.blit(penguin_images[selector_current], (resolution[0] // 2 - 100, 100))

        pygame.display.update()