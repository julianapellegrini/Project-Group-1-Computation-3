from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
from utils import under_construction
from interfaces_menus.map import map_layout
from interfaces_menus.button import Button, select_sound
from save_system.SaveLoadGame import SaveManager, check_save_file


def start_screen(player):
    # initialize pygame
    pygame.init()  # calling pygame

    # set screen
    screen = pygame.display.set_mode(resolution)

    # set the window title
    pygame.display.set_caption("Penguin Rodeo")

    # set game icon
    pygame_icon = pygame.image.load('images/game_icon.jpg')
    pygame.display.set_icon(pygame_icon)

    # set and scale background
    background = pygame.image.load('images/menu.png')
    background = pygame.transform.scale(background, resolution)

    # load font
    chiller_font = pygame.font.SysFont("chiller", 30)

    # create text
    text = chiller_font.render("Press Space Bar to Start Game!", True, bice_blue)

    # set text position
    text_rect = text.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # set game loop
    running = True
    while running:

        # display background
        screen.blit(background, (0, 0))

        # display text
        screen.blit(text, text_rect)

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if check_save_file():
                    interface_w_save(player)
                else:
                    interface_no_save(player)

        # update display
        pygame.display.update()


# function to confirm new game
def confirm_new_game():

    # set screen
    screen = pygame.display.set_mode(resolution)

    # scale and set background
    background = pygame.image.load('images/menu.png')
    background = pygame.transform.scale(background, resolution)
    screen.blit(background, (0, 0))

    # create confirmation buttons
    yes_button = Button(400, 300, 150, 60, "Yes", None, "chiller", 35, True, bice_blue, image="images/ice-banner.png")
    no_button = Button(600, 300, 150, 60, "No", None, "chiller", 35, True, bice_blue, image="images/ice-banner.png")

    while True:

        # get mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return False

            if yes_button.is_clicked(mouse, ev):
                select_sound()
                return True

            if no_button.is_clicked(mouse, ev):
                select_sound()
                return False

            # visuals for buttons
            if yes_button.is_hovered(mouse):
                yes_button.scale_up()
            else:
                yes_button.scale_down()

            if no_button.is_hovered(mouse):
                no_button.scale_up()
            else:
                no_button.scale_down()

        # draw buttons
        yes_button.draw(screen, mouse)
        no_button.draw(screen, mouse)

        pygame.display.update()


def interface_no_save(player):

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # set and scale background
    background = pygame.image.load('images/menu.png')
    background = pygame.transform.scale(background, (resolution[0], resolution[1]))

    # Loading the same image for the buttons
    button_sprite = "images/ice-banner.png"
    #  wood_banner = "images/wood-banner.png"

    # Calculate the center x-coordinate
    center_x = resolution[0] // 2

    # Initialize buttons with the correct parameters
    play_button = Button(center_x - 130, 230, 260, 100, "Play", bice_blue, "chiller", 55, True, royal_blue,
                         image=button_sprite)
    rules_button = Button(center_x - 75, 350, 150, 60, "Rules", None, "chiller", 35, True, bice_blue,
                          image=button_sprite)
    options_button = Button(center_x - 75, 430, 150, 60, "Options", None, "chiller", 35, True, bice_blue,
                            image=button_sprite)
    credits_button = Button(center_x - 75, 510, 150, 60, "Credits", None, "chiller", 40, True, bice_blue,
                            image=button_sprite)
    quit_button = Button(center_x - 75, 590, 150, 60, "Quit", None, "chiller", 45, True, bice_blue, image=button_sprite)

    while True:
        # Displaying the screen
        screen.blit(background, (0, 0))

        # LOGO:
        # title = pygame.image.load(wood_banner)
        # title = pygame.transform.scale(title, (450, 120))
        # screen.blit(title, (center_x - 225, 40))

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Event handling
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            # button is clicked
            if play_button.is_clicked(mouse, ev):
                select_sound()
                map_layout(player)
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

        # draw buttons
        play_button.draw(screen, mouse)
        rules_button.draw(screen, mouse)
        options_button.draw(screen, mouse)
        quit_button.draw(screen, mouse)
        credits_button.draw(screen, mouse)

        # Update the display
        pygame.display.update()


def interface_w_save(player):

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # set and scale background
    background = pygame.image.load('images/menu.png')
    background = pygame.transform.scale(background, (resolution[0], resolution[1]))

    # Loading the same image for the buttons
    button_sprite = "images/ice-banner.png"
    #  wood_banner = "images/wood-banner.png"

    # Calculate the center x-coordinate
    center_x = resolution[0] // 2

    # initialize buttons
    load_game_button = Button(center_x - 75, 230, 150, 60, "Load Game", None, "chiller", 35, True, bice_blue,
                              image=button_sprite)
    new_game_button = Button(center_x - 75, 311, 150, 60, "New Game", None, "chiller", 35, True, bice_blue,
                             image=button_sprite)
    rules_button = Button(center_x - 75, 393, 150, 60, "Rules", None, "chiller", 35, True, bice_blue,
                          image=button_sprite)
    options_button = Button(center_x - 75, 475, 150, 60, "Options", None, "chiller", 35, True, bice_blue,
                            image=button_sprite)
    credits_button = Button(center_x - 75, 556, 150, 60, "Credits", None, "chiller", 40, True, bice_blue,
                            image=button_sprite)
    quit_button = Button(center_x - 75, 638, 150, 60, "Quit", None, "chiller", 45, True, bice_blue, image=button_sprite)

    # set save manager
    save_manager = SaveManager()

    while True:
        # Displaying the screen
        screen.blit(background, (0, 0))

        # LOGO:
        # title = pygame.image.load(wood_banner)
        # title = pygame.transform.scale(title, (450, 120))
        # screen.blit(title, (center_x - 225, 40))

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Event handling
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            # button is clicked
            if load_game_button.is_clicked(mouse, ev):
                select_sound()
                # check if save file exists so game doesn't crash at load
                if check_save_file():  # load game if save file exists
                    saved_data = save_manager.load_game()
                    if saved_data:
                        player.load_inventory(saved_data)
                    map_layout(player)
                else:  # print message if no save file found
                    print("No save file found")
            if new_game_button.is_clicked(mouse, ev):
                select_sound()
                # get confirmation for new game
                if confirm_new_game():
                    # clear save file and start new game
                    open('save_system/gamesave.txt', 'w').close()
                    map_layout(player)
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
            if load_game_button.is_hovered(mouse):
                load_game_button.scale_up()
            else:
                load_game_button.scale_down()

            if new_game_button.is_hovered(mouse):
                new_game_button.scale_up()
            else:
                new_game_button.scale_down()

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

        # draw buttons
        load_game_button.draw(screen, mouse)
        new_game_button.draw(screen, mouse)
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
    background = pygame.image.load('images/credits2.png')
    screen.blit(background, (0, 0))

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")

    while True:

        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

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
    background = pygame.image.load('images/rules2.png')
    screen.blit(background, (0, 0))

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")
    power_button = Button(1000, 550, 150, 60, "Powerups", pink, "chiller", 35, True, bice_blue,
                          image="images/ice-banner.png")

    while True:

        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            if power_button.is_clicked(mouse, ev):
                select_sound()
                power_desc()

            # Clear the button's previous position
            previous_rect = pygame.Rect(back_button.x, back_button.y, back_button.width, back_button.height)
            screen.blit(background, previous_rect, previous_rect)  # Clear the previous area

            previous_rect = pygame.Rect(power_button.x, power_button.y, power_button.width, power_button.height)
            screen.blit(background, previous_rect, previous_rect)

            # Update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            if power_button.is_hovered(mouse):
                power_button.scale_up()
            else:
                power_button.scale_down()

            back_button.draw(screen, mouse)  # Draw the button after updating
            power_button.draw(screen, mouse)

        # drawing the back button
        back_button.draw(screen, mouse)
        power_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()


def power_desc():
    # loading the rules screen
    screen = pygame.display.set_mode(resolution)
    background = pygame.image.load('images/powerups_desc.png')
    screen.blit(background, (0, 0))

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")

    while True:

        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            if back_button.is_clicked(mouse, ev):
                select_sound()
                rules_()

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
