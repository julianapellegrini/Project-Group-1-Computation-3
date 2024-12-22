
from utils import *
from interfaces_menus.button import Button, select_sound
from player_related.weapons import Snowball, Slingshot, Fish_bazooka, Ice_Ninja_Stars

def improve_combat_screen(player):
    """
    Display the combat improvement screen where the player can upgrade their weapons for better damage using coins

    Parameters
    ----------
    player : object
        The player object that contains the player's balance and weapons

    Returns
    -------
    None
        The function does not return anything. It updates the player's weapons and balance based on the
        on-screen actions
    """

    # setting up the background
    background = pygame.image.load('images/textbg.png')
    background = pygame.transform.scale(background, resolution)

    # set screen
    screen = pygame.display.set_mode(resolution)

    # set clock
    clock = pygame.time.Clock()

    # setting up buttons
    back_button = Button(950, 600, 200, 100, "Back", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown,
                         image="images/Wood-button1.png")

    # weapons list from the player object
    weapons = [player.snowball, player.slingshot, player.fish_bazooka, player.ice_ninja_stars, player.sardine_shooter]
    # get weapon upgrades from the player object to keep track of the progress
    weapon_upgrades = player.weapon_upgrades

    # ensure all weapons are initialized in upgrades
    for weapon in weapons:
        if weapon.name not in weapon_upgrades:
            weapon_upgrades[weapon.name] = 0                   

    # coin image
    coin_image = pygame.image.load("images/snowflake_coin.png")
    coin_image = pygame.transform.scale(coin_image, (35, 35))  # Adjust the coin size

    # font for text
    font = pygame.font.Font("fonts/Grand9KPixel.ttf", 25)

    # create upgrade buttons for each weapon
    upgrade_buttons = []
    button_x, button_y = 760, 70
    button_spacing = 128
    for i, weapon in enumerate(weapons):
        upgrade_button = Button(button_x, button_y + i * button_spacing, 150, 60, "+0.5 DMG", royal_blue,
                                "fonts/Grand9KPixel.ttf", 25, True, light_blue, image="images/Wood-button1.png")
        upgrade_buttons.append(upgrade_button)

    running = True
    while running:
        # set FPS
        clock.tick(fps)

        # draw background
        screen.blit(background, (0, 0))

        # get mouse position
        mouse = pygame.mouse.get_pos()

        # vertical rectangle dimensions
        rect_width, rect_height = 900, 650  # increased height for each section to fit all content
        rect_x, rect_y = 40, 40  # lowered the starting Y position
        section_height = rect_height // len(weapons)

        # draw vertical rectangle
        pygame.draw.rect(screen, (50, 50, 50), (rect_x, rect_y, rect_width, rect_height))

        # draw player's balance at the top-right
        balance_text = font.render(f"Balance: {player.balance}", True, oxford_blue)
        screen.blit(balance_text, (resolution[0] - 230, 30))

        # loop through weapons and draw sections
        for i, weapon in enumerate(weapons):
            section_y = rect_y + i * section_height

            # draw section background
            pygame.draw.rect(screen, brown, (rect_x, section_y, rect_width, section_height))

            # weapon Image
            weapon.image = pygame.transform.scale(weapon.image, (100, 100))  # Resize weapon image
            screen.blit(weapon.image, (rect_x + 20, section_y + (section_height - 100) // 2))

            # weapon Name
            weapon_name_text = font.render(weapon.name, True, (255, 255, 255))
            screen.blit(weapon_name_text, (rect_x + 140, section_y + 10))  # Adjusted position

            # weapon Damage
            weapon_damage_text = font.render(f"DMG: {weapon.damage}", True, (255, 255, 255))
            screen.blit(weapon_damage_text, (rect_x + 140, section_y + 50))  # Adjusted position

            # upgrade Progress Bar
            bar_x, bar_y = rect_x + 300, section_y + 50  # Placed right in front of the damage text
            bar_width, bar_height = 400, 30  # Wider progress bar
            pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))  # Background bar

            # filled sections based on upgrade progress
            progress = player.weapon_upgrades[weapon.name]
            for j in range(progress):
                segment_width = bar_width // 6
                pygame.draw.rect(screen, (0, 200, 0), (bar_x + j * segment_width, bar_y, segment_width - 2, bar_height))

            # draw upgrade button
            upgrade_buttons[i].draw(screen, mouse)

            # coin cost below the button
            cost_text = font.render("20", True, (255, 255, 255))
            coin_cost_x, coin_cost_y = upgrade_buttons[i].x + 50, upgrade_buttons[i].y + 65
            screen.blit(coin_image, (coin_cost_x + 35, coin_cost_y))
            screen.blit(cost_text, (coin_cost_x, coin_cost_y))

        # handle weapon upgrade click
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return
            if back_button.is_clicked(mouse, ev):
                select_sound()
                return
            for i, upgrade_button in enumerate(upgrade_buttons):
                if upgrade_button.is_clicked(mouse, ev):
                    if player.balance >= 20 and weapon_upgrades[weapons[i].name] < 6:
                        select_sound()
                        player.balance -= 20
                        weapons[i].damage += 0.5
                        player.weapon_upgrades[weapons[i].name] += 1  # save progress to the player object
                        print(
                            f"Upgraded {weapons[i].name} to {weapons[i].damage} damage. Balance left: {player.balance}")
                    elif weapon_upgrades[weapons[i].name] >= 6:
                        print(f"{weapons[i].name} is fully upgraded!")
                    else:
                        print("Not enough balance!")
        
        

        # putting visual effects on buttons
        for button in [back_button] + upgrade_buttons:
            if button.is_hovered(pygame.mouse.get_pos()):
                button.scale_up()
            else:
                button.scale_down()

        # Draw back button
        back_button.draw(screen, mouse)

        # Update 
        pygame.display.update()