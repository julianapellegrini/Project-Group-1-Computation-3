from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
from utils import under_construction
from game import game_loop
from button import Button


def interface():

    # initiating pygame
    pygame.init()   # calling pygame

    # initiating mixer aka what plays the music
    pygame.mixer.init()

    # loading music file
    pygame.mixer.music.load("audio/nocturne-of-ice.mp3")

    # playing the music infinitely
    pygame.mixer.music.play(loops=-1)

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)    # show the user something

    # Loading the same image for the buttons
    button_sprite = "images/ice-banner.png"
    wood_banner = "images/wood-banner.png"

    # Initialize buttons with the correct parameters
    # wilderness_button = Button(90, 40, 550, 100, "Wilderness Explorer", royal_blue, "Cooper Black", 40, True, bice_blue, image=wood_banner)
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

            if play_button.is_clicked(mouse, ev):
                wilderness_explorer()
            if rules_button.is_clicked(mouse, ev):
                under_construction()
            if options_button.is_clicked(mouse, ev):
                under_construction()
            if quit_button.is_clicked(mouse, ev):
                pygame.quit()
            if credits_button.is_clicked(mouse, ev):
                credits_()

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

    # basic settings #

    screen = pygame.display.set_mode(resolution)

    # creating the fonts:
    corbelfont = pygame.font.SysFont("Corbel", 50)
    comicsansfont = pygame.font.SysFont("Comic Sans MS", 25)

    # creating the rendered texts for the credits
    madi_text = comicsansfont.render("Madalena Duarte", True, royal_blue)
    juliana_text = comicsansfont.render("Juliana Reis", True, royal_blue)
    julia_text = comicsansfont.render("Júlia Vidal", True, royal_blue)
    andre_text = comicsansfont.render("André Calheiros", True, royal_blue)

    # main loop to detect user input and displaying the credits page

    while True:
        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():

            # allow the user to quit on (x)
            if ev.type == pygame.QUIT:
                pygame.quit()

            # checking if the user clicked the back button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    interface()

        # displaying my screen
        background = pygame.image.load('images/ice-background.jpg')
        background = pygame.transform.scale(background, (resolution[0], resolution[1]))
        screen.blit(background, (0, 0))

        # displaying our texts
        screen.blit(madi_text, (0, 0))
        screen.blit(juliana_text, (0, 25))
        screen.blit(julia_text, (0, 50))
        screen.blit(andre_text, (0, 75))

        # drawing and displaying the back button
        pygame.draw.rect(screen, dark_red, [450, 600, 140, 60])
        back_text = corbelfont.render("back", True, white)
        back_rect = back_text.get_rect(center=(450 + 140 // 2, 600 + 60 // 2))
        screen.blit(back_text, back_rect)

        # updating the display
        pygame.display.update()


def rules_():
    print("Displaying rules...")


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
