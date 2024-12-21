from utils import *
from config import *
from interfaces_menus.button import Button, select_sound


class WeaponSale:
    def __init__(self, name, price, image_path):
        self.name = name
        self.price = price
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (150, 150))


def weapon_shop(player):
    pygame.init()
    screen = pygame.display.set_mode(resolution)

    # setting up the background
    background = pygame.image.load('images/textbg.png')
    background = pygame.transform.scale(background, resolution)

    # loading the coin image
    coin_image = pygame.image.load('images/snowflake_coin.png')
    coin_image = pygame.transform.scale(coin_image, (35, 35))

    # setting up buttons
    back_button = Button(950, 600, 200, 100, "Back", brown, "fonts/Grand9KPixel.ttf", 30, True, light_brown,
                         image="images/Wood-button1.png")

    # list of weapons
    weapons = [
        WeaponSale("Snowball", 10, "images_weapons/snowball.png"),
        WeaponSale("Slingshot", 25, "images_weapons/ice_slingshot.png"),
        WeaponSale("Fish Bazooka", 100, "images_weapons/fish_bazooka.png"),
        WeaponSale("Ice Ninja Stars", 35, "images_weapons/ice_ninja_star.png"),
        WeaponSale("Sardine Shooter", 50, "images_weapons/sardine_shooter.png")
    ]

    # setting up the  weapon buttons
    weapon_buttons = []
    for i, weapon in enumerate(weapons):
        weapon_buttons.append(Button(650, 70 + i * 140, 120, 50, "BUY", royal_blue,
                                     "fonts/Grand9KPixel.ttf", 20, True, light_blue, image="images/Wood-button1.png"))

    while True:
        # displaying the background
        screen.blit(background, (0, 0))

        # get player's mouse position
        mouse = pygame.mouse.get_pos()
        print(mouse)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return
            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            for i, weapon_button in enumerate(weapon_buttons):
                if weapon_button.is_clicked(mouse, ev):
                    select_sound()
                    if player.balance >= weapons[i].price:
                        player.balance -= weapons[i].price
                        player.inventory.add_weapon(weapons[i])
                        print(f"Bought {weapons[i].name}")

            # putting visual effects on buttons
            if back_button.is_hovered(pygame.mouse.get_pos()):
                back_button.scale_up()
            else:
                back_button.scale_down()

            for weapon_button in weapon_buttons:
                if weapon_button.is_hovered(pygame.mouse.get_pos()):
                    weapon_button.scale_up()
                else:
                    weapon_button.scale_down()

        # draw the button after updating
        back_button.draw(screen, mouse)

        for i, weapon in enumerate(weapons):
            screen.blit(weapon.image, (80, 30 + i * 135))
            weapon_buttons[i].draw(screen, mouse)

            # draw weapon name and price
            weapon_text = f"{weapon.name}  -  {weapon.price}"
            weapon_text_surface = pygame.font.Font("fonts/Grand9KPixel.ttf", 20).render(weapon_text, True, brown)
            screen.blit(weapon_text_surface, (300, 80 + i * 140))

            # draw coin image next to the price
            screen.blit(coin_image, (300 + weapon_text_surface.get_width() + 10, 78 + i * 140))

        # update the display
        pygame.display.update()
