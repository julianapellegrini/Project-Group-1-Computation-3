from interface import *
from button import Button, select_sound
from shed import shed
from game import game_loop  # Import the game_loop function to pass the level number

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

    # creating level buttons
    level_buttons = [
        Button(150, 200, 200, 100, "1", None, "chiller", 45, True, royal_blue, image="images/level-button.png"),
        Button(400, 300, 200, 100, "2", None, "chiller", 45, True, royal_blue, image="images/level-button.png"),
        Button(650, 400, 200, 100, "3", None, "chiller", 45, True, royal_blue, image="images/level-button.png"),
        Button(200, 500, 200, 100, "4", None, "chiller", 45, True, royal_blue, image="images/level-button.png"),
        Button(500, 600, 200, 100, "5", None, "chiller", 45, True, royal_blue, image="images/level-button.png")
    ]

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

            if igloo_button.is_clicked(mouse, ev):
                select_sound()
                shed()

            # Check if any level button is clicked by iterating through them rather than creating 1908393 if cases
            for i, level_button in enumerate(level_buttons):
                if level_button.is_clicked(mouse, ev):
                    select_sound()
                    game_loop(level=i + 1)  # Pass the level number to game_loop

        # Update button visuals
        for level_button in level_buttons:
            if level_button.is_hovered(mouse):
                level_button.scale_up()
            else:
                level_button.scale_down()

        if back_button.is_hovered(mouse):
            back_button.scale_up()
        else:
            back_button.scale_down()

        if igloo_button.is_hovered(mouse):
            igloo_button.scale_up()
        else:
            igloo_button.scale_down()

        # Draw all buttons
        for level_button in level_buttons:
            level_button.draw(screen, mouse)

        back_button.draw(screen, mouse)
        igloo_button.draw(screen, mouse)

        # Update the display
        pygame.display.update()
