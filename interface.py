from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
from utils import under_construction
from game import game_loop
from button import Button, select_sound


def interface():

    # initiating pygame
    pygame.init()   # calling pygame

    # loading music file
    pygame.mixer.music.load("audio/nocturne-of-ice.mp3")
    pygame.mixer.music.set_volume(0.3)

    # playing the music infinitely
    pygame.mixer.music.play(loops=-1)

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # Loading the same image for the buttons
    button_sprite = "images/ice-banner.png"
    wood_banner = "images/wood-banner.png"

    # Initialize buttons with the correct parameters
    play_button = Button(230, 230, 260, 100, "Play", bice_blue, "chiller", 55, True, royal_blue, image=button_sprite)
    rules_button = Button(285, 350, 150, 60, "Rules", None, "chiller", 35, True, bice_blue, image=button_sprite)
    options_button = Button(285, 430, 150, 60, "Options", None, "chiller", 35, True, bice_blue, image=button_sprite)
    credits_button = Button(285, 510, 150, 60, "Credits", None, "chiller", 40, True, bice_blue, image=button_sprite)
    quit_button = Button(285, 590, 150, 60, "Quit", None, "chiller", 45, True, bice_blue, image=button_sprite)

    while True:
        # Displaying the screen
        background = pygame.image.load('images/ice-background.jpg')
        background = pygame.transform.scale(background, (resolution[0], resolution[1]))
        screen.blit(background, (0, 0))

        # LOGO:
        title = pygame.image.load(wood_banner)
        title = pygame.transform.scale(title, (450, 120))
        screen.blit(title, (135, 40))

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Event handling
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            # button is clicked
            if play_button.is_clicked(mouse, ev):
                select_sound()
                wilderness_explorer()
            if rules_button.is_clicked(mouse, ev):
                select_sound()
                rules_()
            if options_button.is_clicked(mouse, ev):
                select_sound()
                under_construction()
            if quit_button.is_clicked(mouse, ev):
                select_sound()
                pygame.quit()
            if credits_button.is_clicked(mouse, ev):
                select_sound()
                credits_()

            # hover over button
            if play_button.is_hovered(mouse):
                play_button.scale_up()
            else:
                play_button.scale_down()

            if rules_button.is_hovered(mouse):
                rules_button.scale_up()
            else:
                rules_button.scale_down()

            if options_button.is_hovered(mouse):
                options_button.scale_up()
            else:
                options_button.scale_down()

            if credits_button.is_hovered(mouse):
                credits_button.scale_up()
            else:
                credits_button.scale_down()

            if quit_button.is_hovered(mouse):
                quit_button.scale_up()
            else:
                quit_button.scale_down()

        # Draw buttons
        # wilderness_button.draw(screen, mouse)
        play_button.draw(screen, mouse)
        rules_button.draw(screen, mouse)
        options_button.draw(screen, mouse)
        quit_button.draw(screen, mouse)
        credits_button.draw(screen, mouse)

        # Update the display
        pygame.display.update()


# Under construction screen
def credits_():
    # loading the rules screen
    screen = pygame.display.set_mode(resolution)
    background = pygame.image.load('images/credits.png')
    screen.blit(background, (0, 0))

    # setting up the back button
    back_button = Button(550, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue, image="images/ice-banner.png")

    while True:

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


def rules_():
    # loading the rules screen
    screen = pygame.display.set_mode(resolution)
    background = pygame.image.load('images/rules.png')
    screen.blit(background, (0, 0))

    # setting up the back button
    back_button = Button(550, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue, image="images/ice-banner.png")

    while True:

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



def ice_button(x, y, d1, d2):
    screen = pygame.display.set_mode(resolution)

    # Load the image
    ice = pygame.image.load("images/ice-banner.png")

    # Resize the image to fit the dimensions received as input
    resized_image = pygame.transform.scale(ice, (d1, d2))

    # Draw the image on the screen at position received as input
    screen.blit(resized_image, (x, y))


def wilderness_explorer():
    game_loop()
