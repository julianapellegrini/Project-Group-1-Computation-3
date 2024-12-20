from utils import *
from interfaces_menus.button import Button, select_sound
from player_related.weapons import Snowball, Slingshot, Fish_bazooka, Ice_Ninja_Stars

def improve_combat_screen(player):

    # Load background
    background = pygame.image.load("images/weapon_selector_background.png")
    background = pygame.transform.scale(background, resolution)

    # Set screen
    screen = pygame.display.set_mode(resolution)

    # Set clock
    clock = pygame.time.Clock()

    # Back button
    back_button = Button(1000, 650, 150, 60, "Back", None, "fonts/Grand9KPixel.ttf", 35, True, bice_blue,
                         image="images/ice-banner.png")

    # Weapons list
    weapons = [Snowball(), Slingshot(), Fish_bazooka(), Ice_Ninja_Stars()]

    # Coin image
    coin_image = pygame.image.load("images/snowflake_coin.png")
    coin_image = pygame.transform.scale(coin_image, (40, 40))  # Adjust the coin size

    # Font for text
    font = pygame.font.Font("fonts/Grand9KPixel.ttf", 25)

    # Running flag
    running = True

    # Weapon upgrade progress tracking
    weapon_upgrades = {weapon.name: 0 for weapon in weapons}  # 0 to 6 progress

    while running:
        # Set FPS
        clock.tick(fps)

        # Draw background
        screen.blit(background, (0, 0))

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Vertical rectangle dimensions
        rect_width, rect_height = 800, 500
        rect_x, rect_y = (resolution[0] - rect_width) // 2, 100
        section_height = rect_height // len(weapons)

        # Draw vertical rectangle
        pygame.draw.rect(screen, (50, 50, 50), (rect_x, rect_y, rect_width, rect_height))

        # Loop through weapons and draw sections
        for i, weapon in enumerate(weapons):
            section_y = rect_y + i * section_height

            # Draw section divider
            pygame.draw.line(screen, (200, 200, 200), (rect_x, section_y), (rect_x + rect_width, section_y))

            # Weapon Image
            weapon.image = pygame.transform.scale(weapon.image, (100, 100))  # Resize weapon image
            screen.blit(weapon.image, (rect_x + 20, section_y + (section_height - 100) // 2))

            # Weapon Name
            weapon_name_text = font.render(weapon.name, True, (255, 255, 255))
            screen.blit(weapon_name_text, (rect_x + 140, section_y + 20))

            # Weapon Damage
            weapon_damage_text = font.render(f"DMG: {weapon.damage}", True, (255, 255, 255))
            screen.blit(weapon_damage_text, (rect_x + 140, section_y + 60))

            # Upgrade Progress Bar
            bar_x, bar_y = rect_x + 300, section_y + (section_height - 30) // 2
            bar_width, bar_height = 300, 30
            pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))  # Background bar

            # Filled sections based on upgrade progress
            progress = weapon_upgrades[weapon.name]
            for j in range(progress):
                segment_width = bar_width // 6
                pygame.draw.rect(screen, (0, 200, 0), (bar_x + j * segment_width, bar_y, segment_width - 2, bar_height))

            # Upgrade Button
            upgrade_button = Button(rect_x + 650, section_y + (section_height - 60) // 2, 150, 60, "+0.5 DMG", None,
                                     "fonts/Grand9KPixel.ttf", 25, True, bice_blue, image="images/ice-banner.png")
            upgrade_button.draw(screen, mouse)

            # Coin image beside the button
            screen.blit(coin_image, (rect_x + 610, section_y + (section_height - 40) // 2))

            # Handle weapon upgrade click
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

                if upgrade_button.is_clicked(mouse, ev):
                    if player.balance >= 50 and weapon_upgrades[weapon.name] < 6:
                        select_sound()
                        player.balance -= 50
                        weapon.damage += 0.5
                        weapon_upgrades[weapon.name] += 1
                        print(f"Upgraded {weapon.name} to {weapon.damage} damage. Coins left: {player.balance}")
                    elif weapon_upgrades[weapon.name] >= 6:
                        print(f"{weapon.name} is fully upgraded!")
                    else:
                        print("Not enough coins!")

        # Draw player's coin count at the top
        coin_count_text = font.render(f"Coins: {player.balance}", True, (255, 255, 255))
        screen.blit(coin_count_text, (20, 20))

        # Draw back button
        back_button.draw(screen, mouse)

        # Handle back button click
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

        # Update display
        pygame.display.update()
