from utils import *
from config import *
from interfaces_menus.button import Button, select_sound


class WeaponSale(pygame.sprite.Sprite):
    """
    A class to represent a weapon for sale in the weapon shop.

    Attributes
    ----------
    name : str
        The name of the weapon.
    price : int
        The price of the weapon.
    image : pygame image
        The image of the weapon.
    rect : pygame rect
        The rectangle of the weapon, used for positioning and collision detection.

    Methods
    -------
    __init__(name, price, image_path)
        Initializes the weapon object with the given attributes.
    """
    def __init__(self, name, price, image_path):
        super().__init__()
        self.name = name
        self.price = price
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()


def weapon_shop(player):
    """
    Display the weapon shop screen where the player can buy weapons.

    Parameters
    ----------
    player : object
        The player object that interacts with the weapon shop screen. It contains the player's balance and inventory.

    Returns
    -------
    None
        The function does not return anything. It exits on ESC key press or back button click. It updates the player's
        balance and inventory based on the player's actions on the screen.
    """
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
        WeaponSale("Slingshot", 25, "images_weapons/slingshot.png"),
        WeaponSale("Fish Bazooka", 100, "images_weapons/fish_bazooka.png"),
        WeaponSale("Ice Ninja Stars", 50, "images_weapons/ice_ninja_stars.png"),
        WeaponSale("Sardine Shooter", 85, "images_weapons/sardine_shooter.png")
    ]

    # setting up the  weapon buttons
    weapon_buttons = []
    for i, weapon in enumerate(weapons):
        weapon_buttons.append(Button(650, 91 + i * 133, 120, 50, "BUY", royal_blue,
                                     "fonts/Grand9KPixel.ttf", 20, True, light_blue, image="images/Wood-button1.png"))

    # font for text
    font = pygame.font.Font("fonts/Grand9KPixel.ttf", 25)

    while True:
        # displaying the background
        screen.blit(background, (0, 0))

        # drawing the brown background rectangle
        rect_x, rect_y, rect_width, rect_height = 50, 45, 850, 650
        pygame.draw.rect(screen, brown, (rect_x, rect_y, rect_width, rect_height))

        # draw player's balance at the top-right
        balance_text = font.render(f"Balance: {player.balance}", True, oxford_blue)
        screen.blit(balance_text, (resolution[0] - 230, 30))

        # get player's mouse position
        mouse = pygame.mouse.get_pos()

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
                    if player.balance >= weapons[i].price and player.inventory.items['Weapons'][weapons[i].name] == 0:
                        player.balance -= weapons[i].price
                        player.inventory.add_item(weapons[i])
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
            screen.blit(weapon.image, (rect_x + 20, rect_y + i * 130))
            weapon_buttons[i].draw(screen, mouse)

            # draw weapon name and price
            weapon_text = f"{weapon.name}  -  {weapon.price}"
            weapon_text_surface = pygame.font.Font("fonts/Grand9KPixel.ttf", 20).render(weapon_text, True, white)
            screen.blit(weapon_text_surface, (rect_x + 200, rect_y + 50 + i * 133))

            # draw coin image next to the price
            screen.blit(coin_image, (rect_x + 200 + weapon_text_surface.get_width() + 10, rect_y + 50 + i * 133))

        # update the display
        pygame.display.update()
