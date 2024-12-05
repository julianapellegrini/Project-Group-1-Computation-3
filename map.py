from interface import *
from button import Button, select_sound
from shed import shed



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

    play_button = Button(500, 230, 260, 100, "Play", bice_blue, "chiller", 55, True, royal_blue,
                         image=button_sprite)

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

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            if play_button.is_clicked(mouse, ev):
                select_sound()
                game_loop()

            if igloo_button.is_clicked(mouse, ev):
                select_sound()
                shed()

            # Clear the button's previous position
            previous_rect = pygame.Rect(back_button.x, back_button.y, back_button.width, back_button.height)
            screen.blit(background, previous_rect, previous_rect)  # Clear the previous area

            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            if igloo_button.is_hovered(mouse):
                igloo_button.scale_up()
            else:
                igloo_button.scale_down()

            if play_button.is_hovered(mouse):
                play_button.scale_up()
            else:
                play_button.scale_down()

            back_button.draw(screen, mouse)  # Draw the button after updating
            igloo_button.draw(screen, mouse)  # Draw the button after updating
            play_button.draw(screen, mouse)  # Draw the button after updating

        # drawing the back button
        back_button.draw(screen, mouse)
        igloo_button.draw(screen, mouse)
        play_button.draw(screen, mouse)

        # Update the display
        pygame.display.update()



