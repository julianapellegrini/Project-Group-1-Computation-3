from interface import *
from button import Button


def map_layout():
    # initializing pygame
    pygame.init()

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # path for the images of the buttons
    button_sprite = "images/ice-banner.png"
    igloo_sprite = "images/igloo_button.png"

    # setting up the back button
    back_button = Button(950, 600, 200, 100, "Back", None, "chiller", 45, True, bice_blue,
                         image=button_sprite)

    # setting up the igloo button
    igloo_button = Button(940, 30, 200, 200, None, None, None, 35, False, None,
                         image=igloo_sprite)

    while True:

        # Displaying the screen
        background = pygame.image.load('images/map_layout.png')
        background = pygame.transform.scale(background, (resolution[0], resolution[1]))
        screen.blit(background, (0, 0))

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            if igloo_button.is_clicked(mouse, ev):
                select_sound()
                return "shed"

            # Clear the button's previous position
            previous_rect = pygame.Rect(back_button.x, back_button.y, back_button.width, back_button.height)
            screen.blit(background, previous_rect, previous_rect)  # Clear the previous area

            # Update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            # Update and draw the button
            if igloo_button.is_hovered(mouse):
                igloo_button.scale_up()
            else:
                igloo_button.scale_down()

            back_button.draw(screen, mouse)  # Draw the button after updating
            igloo_button.draw(screen, mouse)  # Draw the button after updating

        # drawing the back button
        back_button.draw(screen, mouse)
        igloo_button.draw(screen, mouse)

        # Update the display
        pygame.display.update()



