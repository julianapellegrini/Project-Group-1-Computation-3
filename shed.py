import pygame

from config import *
from utils import *
from button import Button, select_sound


def shed():
    # setting up the background and the screen
    background = pygame.image.load("images/temporary-igloo.jpg")

    # scaling the background image into our selected resolution
    background = pygame.transform.scale(background, resolution)

    # setting up the screen
    screen = pygame.display.set_mode(resolution)

    # setting up the clock for fps
    clock = pygame.time.Clock()

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")

    running = True

    while running:
        clock.tick(fps)
        # displaying the background on the entirety of the screen
        screen.blit(background, (0, 0))

        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            # Clear the button's previous position
            previous_rect = pygame.Rect(back_button.x, back_button.y, back_button.width, back_button.height)
            screen.blit(background, previous_rect, previous_rect)  # Clear the previous area

            # Update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            back_button.draw(screen, mouse)  # Draw the button after updating

        # drawing the back button
        back_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()