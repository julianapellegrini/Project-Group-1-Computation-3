from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
from utils import under_construction
from interfaces_menus.map import map_layout
from interfaces_menus.button import Button, select_sound
from save_system.SaveLoadGame import SaveManager
from interfaces_menus.confirm_screen import confirm
from interfaces_menus.choose_interface import choose_interface
from save_system.check_save import check_save_file

# define scroll variables
scroll = 0
bg_images = []

def load_backgrounds():
    global bg_images
    for i in range(1, 6):
        bg_image = pygame.image.load(f"bg/Plan{i}.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, resolution)
        bg_images.append(bg_image)


def draw_bg(screen):
    global bg_images
    bg_width = bg_images[0].get_width()
    for x in range(50):
        speed = 1
        for bg_image in bg_images:
            screen.blit(bg_image, ((x * bg_width) - scroll * speed, 0))
            speed += 0.3

def start_screen(player):
    global scroll

    # Initialize pygame and load music
    pygame.init()
    pygame.mixer.music.load("audio/nocturne-of-ice.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    # Set screen and other UI elements
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Penguin Rodeo")
    pygame_icon = pygame.image.load('images/game_icon.jpg')
    pygame.display.set_icon(pygame_icon)
    load_backgrounds()

    # Load font and text
    chiller_font = pygame.font.SysFont("chiller", 30)
    text = chiller_font.render("Press Space Bar to Start Game!", True, bice_blue)
    text_rect = text.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)  # Cap FPS

        # Draw background and update scroll
        draw_bg(screen)
        scroll += 0.5

        # Display text
        screen.blit(text, text_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                interface_no_save(player)  # Transition to next screen

        pygame.display.update()



def interface_no_save(player):

    global scroll

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

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

        # display background
        draw_bg(screen)
        scroll += 1

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
                map_layout(player, interface_w_save=interface_w_save, interface_no_save=interface_no_save)
            if rules_button.is_clicked(mouse, ev):
                select_sound()
                rules_(player)
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
                    map_layout(player, interface_w_save=interface_w_save, interface_no_save=interface_no_save)
                else:  # print message if no save file found
                    print("No save file found")
            if new_game_button.is_clicked(mouse, ev):
                select_sound()
                # get confirmation for new game
                if confirm():
                    # clear save file and start new game
                    open('save_system/gamesave.txt', 'w').close()
                    map_layout(player, interface_w_save=interface_w_save, interface_no_save=interface_no_save)
            if rules_button.is_clicked(mouse, ev):
                select_sound()
                rules_(player)
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


def rules_(player):
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
                choose_interface(player, interface_w_save=interface_w_save, interface_no_save=interface_no_save)

            if power_button.is_clicked(mouse, ev):
                select_sound()
                power_desc(player)

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


def power_desc(player):
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
                rules_(player)

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
