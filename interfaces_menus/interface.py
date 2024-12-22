from config import *  # importing colors and the like
from interfaces_menus.map import map_layout
from interfaces_menus.button import Button, select_sound
from save_system.SaveLoadGame import SaveManager
from interfaces_menus.confirm_screen import confirm
from interfaces_menus.choose_interface import choose_interface
from save_system.check_save import check_save_file
from interfaces_menus.moving_bg import bg_images, draw_bg, load_backgrounds
from music import Music
from interfaces_menus.slider import Slider

# define scroll variables
scroll = 0

# sound settings variables
music_volume = 0.3
sound_volume = 0.2

# default slider values to match the default volume
music_slider_value = music_volume * 100
sound_slider_value = sound_volume * 100


# start screen so we can redirect the player to the correct interface based on the save file
def start_screen(player):

    """
    Displays the start screen and redirects the player to the correct interface based on the save file.

    Parameters:
    -----------
    player : object
        The player object.
    """

    global scroll

    # initialize pygame and load music
    pygame.init()

    background_music = Music("audio/start-screen.mp3")
    background_music.play()
    background_music.volchange(music_volume)

    # check if the music is playing
    is_playing = background_music.isplaying()

    # set screen and other UI elements
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Penguin Rodeo")
    pygame_icon = pygame.image.load('images/game_icon.jpg')
    pygame.display.set_icon(pygame_icon)
    load_backgrounds()

    # load font and text
    press_text = pygame.image.load('images/press2p.png')
    press_text = pygame.transform.scale(press_text, (600, 50))
    press_rect = press_text.get_rect(center=(resolution[0] // 2, resolution[1] * 0.75))

    icon = pygame.image.load('images/game-logo.png')
    icon = pygame.transform.scale(icon, (456, 440))
    icon_rect = icon.get_rect(center=(resolution[0] // 2, 300))

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)  # cap FPS

        # draw background and update scroll
        draw_bg(screen, scroll)
        scroll += 0.5

        # display text
        screen.blit(press_text, press_rect)
        screen.blit(icon, icon_rect)

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                choose_interface(player, interface_w_save=interface_w_save, interface_no_save=interface_no_save)
                # transition to next screen

        pygame.display.update()


# interface if player has no save file
def interface_no_save(player):

    """
    Displays the interface when there is no save file.

    This function sets up a Pygame window with the game logo and buttons for playing, viewing rules, options, credits, and quitting.

    Parameters:
    -----------
    player : object
        The player object.
    """

    global scroll

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # loading the same image for the buttons
    button_sprite = "images/Wood-button1.png"
    #  wood_banner = "images/wood-banner.png"

    # game logo
    icon = pygame.image.load('images/game-logo.png')
    icon = pygame.transform.scale(icon, (256, 230))
    icon_rect = icon.get_rect(center=(resolution[0] // 2, 140))

    # calculate the center x-coordinate
    center_x = resolution[0] // 2

    # initialize buttons with the correct parameters
    play_button = Button(center_x - 130, 230, 250, 100, "Play", brown, "fonts/Grand9KPixel.ttf", 40, True, light_brown,
                         image=button_sprite)
    rules_button = Button(center_x - 75, 350, 140, 60, "Rules", brown, "fonts/Grand9KPixel.ttf", 25, True, light_brown,
                          image=button_sprite)
    options_button = Button(center_x - 75, 430, 140, 60, "Options", brown, "fonts/Grand9KPixel.ttf", 24, True,
                            light_brown,
                            image=button_sprite)
    credits_button = Button(center_x - 75, 510, 140, 60, "Credits", brown, "fonts/Grand9KPixel.ttf", 26, True,
                            light_brown,
                            image=button_sprite)
    quit_button = Button(center_x - 75, 590, 140, 60, "Quit", brown, "fonts/Grand9KPixel.ttf", 28, True, light_brown,
                         image=button_sprite)

    while True:

        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

        # get mouse position
        mouse = pygame.mouse.get_pos()

        screen.blit(icon, icon_rect)

        # event handling
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
                settings(player)
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

        # update the display
        pygame.display.update()


# interface if player has a save file
def interface_w_save(player):

    """
    Displays the interface when there is a save file.

    This function sets up a Pygame window with the game logo and buttons for loading the game, starting a new game, viewing rules, options, credits, and quitting.

    Parameters:
    -----------
    player : object
        The player object.
    """

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    global scroll

    # loading the same image for the buttons
    button_sprite = "images/Wood-button1.png"

    # calculate the center x-coordinate
    center_x = resolution[0] // 2

    # game logo
    icon = pygame.image.load('images/game-logo.png')
    icon = pygame.transform.scale(icon, (256, 230))
    icon_rect = icon.get_rect(center=(resolution[0] // 2, 160))

    # initialize buttons
    load_game_button = Button(center_x - 155, 270, 150, 70, "Load Game", brown, "fonts/Grand9KPixel.ttf", 19, True,
                              light_brown,
                              image=button_sprite)
    new_game_button = Button(center_x + 5, 270, 150, 70, "New Game", brown, "fonts/Grand9KPixel.ttf", 21, True,
                             light_brown,
                             image=button_sprite)
    rules_button = Button(center_x - 75, 350, 140, 60, "Rules", brown, "fonts/Grand9KPixel.ttf", 25, True, light_brown,
                          image=button_sprite)
    options_button = Button(center_x - 75, 430, 140, 60, "Options", brown, "fonts/Grand9KPixel.ttf", 24, True,
                            light_brown,
                            image=button_sprite)
    credits_button = Button(center_x - 75, 510, 140, 60, "Credits", brown, "fonts/Grand9KPixel.ttf", 26, True,
                            light_brown,
                            image=button_sprite)
    quit_button = Button(center_x - 75, 590, 140, 60, "Quit", brown, "fonts/Grand9KPixel.ttf", 28, True, light_brown,
                         image=button_sprite)

    # set save manager
    save_manager = SaveManager()

    while True:

        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

        screen.blit(icon, icon_rect)  # game logo

        # get mouse position
        mouse = pygame.mouse.get_pos()

        # event handling
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            # button is clicked
            if load_game_button.is_clicked(mouse, ev):
                select_sound()
                # check if save file exists so game doesn't crash at load
                if check_save_file():
                    saved_data = save_manager.load_game()
                    if saved_data:
                        player.load_data(saved_data)
                        print(player.inventory.items)
                    map_layout(player, interface_w_save=interface_w_save, interface_no_save=interface_no_save)
                else:
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
                settings(player)
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

        # update the display
        pygame.display.update()


# credits screen
def credits_():

    """
    Displays the credits screen.

    This function sets up a Pygame window with the credits information and a back button to return to the previous screen.
    """

    # loading the credits screen
    screen = pygame.display.set_mode(resolution)

    global scroll

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")

    # credits image
    textbg = pygame.image.load('images/textbg.png')
    textbg = pygame.transform.scale(textbg, (520, 620))
    textbg_rect = textbg.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    credit = pygame.image.load('images/credit.png')
    credit = pygame.transform.scale(credit, (500, 600))
    credit_rect = credit.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 50)
    text = pixel_font.render("CREDITS", True, brown)
    text_rect = text.get_rect(center=(600, 100))

    while True:

        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

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

            # update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            # drawing the back button
            back_button.draw(screen, mouse)

            screen.blit(textbg, textbg_rect)
            screen.blit(credit, credit_rect)
            screen.blit(text, text_rect)

        # drawing the back button
        back_button.draw(screen, mouse)

        screen.blit(textbg, textbg_rect)
        screen.blit(credit, credit_rect)
        screen.blit(text, text_rect)

        # updating the display
        pygame.display.update()


# rules screen
def rules_(player):

    """
    Displays the rules screen.

    This function sets up a Pygame window with the game rules and a back button to return to the previous screen.

    Parameters:
    -----------
    player : object
        The player object.
    """

    global scroll

    # loading the rules screen
    screen = pygame.display.set_mode(resolution)
    textbg = pygame.image.load('images/textbg.png')
    textbg = pygame.transform.scale(textbg, (520, 620))
    textbg_rect = textbg.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 50)
    text = pixel_font.render("RULES", True, brown)
    text_rect = text.get_rect(center=(600, 100))

    rules = pygame.image.load('images/rules.jpeg')
    rules = pygame.transform.scale(rules, (500, 600))
    rules_rect = rules.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")
    power_button = Button(1000, 550, 150, 60, "Powerups", pink, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                          image="images/Wood-button1.png")
    weapons_button = Button(1000, 450, 150, 60, "Weapons", light_blue, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                            image="images/Wood-button1.png")
    chest_button = Button(1000, 350, 150, 60, "Chests", yellow, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                          image="images/Wood-button1.png")

    while True:

        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

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
                power_desc(player)

            if weapons_button.is_clicked(mouse, ev):
                select_sound()
                weapon_desc(player)

            if chest_button.is_clicked(mouse, ev):
                select_sound()
                chest_desc(player)

            # draw bg, rules and title text
            screen.blit(textbg, textbg_rect)
            screen.blit(rules, rules_rect)
            screen.blit(text, text_rect)

            # update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            if power_button.is_hovered(mouse):
                power_button.scale_up()
            else:
                power_button.scale_down()

            if weapons_button.is_hovered(mouse):
                weapons_button.scale_up()
            else:
                weapons_button.scale_down()

            if chest_button.is_hovered(mouse):
                chest_button.scale_up()
            else:
                chest_button.scale_down()

            back_button.draw(screen, mouse)
            power_button.draw(screen, mouse)
            weapons_button.draw(screen, mouse)
            chest_button.draw(screen, mouse)

        screen.blit(textbg, textbg_rect)
        screen.blit(rules, rules_rect)
        screen.blit(text, text_rect)

        # drawing the back button
        back_button.draw(screen, mouse)
        power_button.draw(screen, mouse)
        weapons_button.draw(screen, mouse)
        chest_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()


# powerup description screen
def power_desc(player):

    """
    Displays the powerup description screen.

    This function sets up a Pygame window with the powerup descriptions and a back button to return to the previous screen.

    Parameters:
    -----------
    player : object
        The player object.
    """

    global scroll

    # loading the powerup screen
    screen = pygame.display.set_mode(resolution)
    textbg = pygame.image.load('images/textbg.png')
    textbg = pygame.transform.scale(textbg, (520, 620))
    textbg_rect = textbg.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 50)
    text = pixel_font.render("POWERUPS", True, brown)
    text_rect = text.get_rect(center=(600, 100))

    power = pygame.image.load('images/powers.png')
    power = pygame.transform.scale(power, (500, 600))
    power_rect = power.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")

    while True:

        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

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

            screen.blit(textbg, textbg_rect)
            screen.blit(power, power_rect)
            screen.blit(text, text_rect)

            # update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            back_button.draw(screen, mouse)

        screen.blit(textbg, textbg_rect)
        screen.blit(power, power_rect)
        screen.blit(text, text_rect)

        # drawing the back button
        back_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()


# weapon description screen
def weapon_desc(player):

    """
    Displays the weapon description screen.

    This function sets up a Pygame window with the powerup descriptions and a back button to return to the previous screen.

    Parameters:
    -----------
    player : object
        The player object.
    """

    global scroll

    # loading the powerup screen
    screen = pygame.display.set_mode(resolution)
    textbg = pygame.image.load('images/textbg.png')
    textbg = pygame.transform.scale(textbg, (520, 620))
    textbg_rect = textbg.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 50)
    text = pixel_font.render("WEAPONS", True, brown)
    text_rect = text.get_rect(center=(600, 100))

    weapomscr = pygame.image.load('images/weaponscr.jpeg')
    weaponscr = pygame.transform.scale(weapomscr, (500, 600))
    weaponscr_rect = weaponscr.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")

    while True:

        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

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

            screen.blit(textbg, textbg_rect)
            screen.blit(weapomscr, weaponscr_rect)
            screen.blit(text, text_rect)

            # update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            back_button.draw(screen, mouse)

        screen.blit(textbg, textbg_rect)
        screen.blit(weapomscr, weaponscr_rect)
        screen.blit(text, text_rect)

        # drawing the back button
        back_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()


# chest description screen
def chest_desc(player):

    """
    Displays the treasure chest description screen.

    This function sets up a Pygame window with the powerup descriptions and a back button to return to the previous screen.

    Parameters:
    -----------
    player : object
        The player object.
    """

    global scroll

    # loading the powerup screen
    screen = pygame.display.set_mode(resolution)
    textbg = pygame.image.load('images/textbg.png')
    textbg = pygame.transform.scale(textbg, (520, 620))
    textbg_rect = textbg.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # set font
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 50)
    text = pixel_font.render("CHESTS", True, brown)
    text_rect = text.get_rect(center=(600, 100))

    chestscr = pygame.image.load('images/chestscr.jpeg')
    chestscr = pygame.transform.scale(chestscr, (500, 600))
    chestscr_rect = chestscr.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")

    while True:

        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

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

            screen.blit(textbg, textbg_rect)
            screen.blit(chestscr, chestscr_rect)
            screen.blit(text, text_rect)

            # update and draw the button
            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            back_button.draw(screen, mouse)

        screen.blit(textbg, textbg_rect)
        screen.blit(chestscr, chestscr_rect)
        screen.blit(text, text_rect)

        # drawing the back button
        back_button.draw(screen, mouse)

        # updating the display
        pygame.display.update()


# settings screen
def settings(player):

    """
    Displays the settings screen.

    This function sets up a Pygame window with sound settings and a back button to return to the previous screen.

    Parameters:
    -----------
    player : object
        The player object.
    """

    global scroll
    global music_volume
    global sound_volume
    global music_slider_value
    global sound_slider_value

    # loading the powerup screen
    screen = pygame.display.set_mode(resolution)

    textbg = pygame.image.load('images/textbg.png')
    textbg = pygame.transform.scale(textbg, (520, 620))
    textbg_rect = textbg.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

    # title
    pixel_font = pygame.font.Font("fonts/Grand9KPixel.ttf", 40)
    text = pixel_font.render("SOUND SETTINGS", True, brown)
    text_rect = text.get_rect(center=(600, 100))

    # music text
    pixel_font2 = pygame.font.Font("fonts/Grand9KPixel.ttf", 20)
    music_text = pixel_font2.render("MUSIC", True, brown)
    music_text_rect = text.get_rect(center=(750, 250))

    # sound text
    sound_text = pixel_font2.render("SOUND EFFECTS", True, brown)
    sound_text_rect = text.get_rect(center=(700, 450))

    # setting up the back button
    back_button = Button(1000, 650, 150, 60, "Back", brown, "fonts/Grand9KPixel.ttf", 20, True, light_brown,
                         image="images/Wood-button1.png")

    # initialize sliders for volume control
    music_slider = Slider(500, 300, 200, 20, 0, 100, music_slider_value)
    sound_slider = Slider(500, 500, 200, 20, 0, 100, sound_slider_value)

    # create an instance of the Music class
    background_music = Music("audio/start-screen.mp3")

    while True:
        # display background
        draw_bg(screen, scroll)
        scroll += 0.5

        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        # event handling for Pygame
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return
            if back_button.is_clicked(pygame.mouse.get_pos(), ev):
                select_sound()
                return

            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            # handle slider events
            music_slider.handle_event(ev)
            sound_slider.handle_event(ev)

        # update volume based on slider values
        music_volume = music_slider.value / 100
        sound_volume = sound_slider.value / 100
        background_music.volchange(music_volume)
        Button.sound_volume = sound_volume

        # saving the position of the slider
        music_slider_value = music_slider.value
        sound_slider_value = sound_slider.value

        # draw bg, title, subtitles
        screen.blit(textbg, textbg_rect)
        screen.blit(text, text_rect)
        screen.blit(music_text, music_text_rect)
        screen.blit(sound_text, sound_text_rect)

        # Draw sliders and button
        music_slider.draw(screen)
        sound_slider.draw(screen)
        back_button.draw(screen, pygame.mouse.get_pos())

        pygame.display.update()


# set the volume for the music
def set_sound_volume(volume):

    """
    Sets the volume for sound effects.

    Parameters:
    -----------
    volume : float
        The volume level to set for sound effects, ranging from 0.0 to 1.0.
    """
    
    # this function sets the volume for sound effects
    for sound in pygame.mixer.get_sounds():
        sound.set_volume(volume)
