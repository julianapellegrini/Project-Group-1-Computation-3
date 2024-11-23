from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
from utils import under_construction
from game import game_loop
from button import Button


def interface():

    # initiating pygame
    pygame.init() # calling pygame
    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)    # show the user something

    # Loading the same image for the buttons
    button_sprite = "images/ice-banner.png"
    wood_banner = "images/wood-banner.png"

    # Initialize buttons with the correct parameters
    wilderness_button = Button(90, 100, 540, 300, "Wilderness Explorer", royal_blue, "Cooper Black", 40, image=wood_banner)
    rules_button = Button(260, 300, 200, 100, "Rules", None, "chiller", 30, image=button_sprite)
    options_button = Button(260, 370, 200, 100, "Options", None, "chiller", 35, image=button_sprite)
    credits_button = Button(260, 450, 200, 100, "Credits", None, "chiller", 40, image=button_sprite)
    quit_button = Button(260, 520, 200, 100, "Quit", None, "chiller", 45, image=button_sprite)

    while True:
        # Displaying the screen
        background = pygame.image.load('images/ice-background.jpg')
        background = pygame.transform.scale(background, (resolution[0], resolution[1]))
        screen.blit(background, (0, 0))

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Event handling
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if wilderness_button.is_clicked(mouse, ev):
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
        wilderness_button.draw(screen, mouse)
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
    augusto_text = comicsansfont.render("Augusto Santos, ajrsantos@novaims.unl.pt", True, white)
    diogo_text = comicsansfont.render("Diogo Rastreio, drasteiro@novaims.unl.pt", True, white)
    liah_text = comicsansfont.render("Liah Rosenfeld, lrosenfeld@novaims.unl.pt", True, white)

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
        screen.blit(augusto_text, (0, 0))
        screen.blit(diogo_text, (0, 25))
        screen.blit(liah_text, (0, 50))

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
