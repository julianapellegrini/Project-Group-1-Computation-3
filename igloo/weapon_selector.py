from utils import *
from config import *
from interfaces_menus.button import Button, select_sound
from player_related.weapons import Snowball, Slingshot
from player_related.player import Player


def weapon_selector():

    # set background
    background = pygame.image.load("images/weapon_selector_background.png")
    # scale background
    background = pygame.transform.scale(background, resolution)

    # set screen
    screen = pygame.display.set_mode(resolution)

    # set clock
    clock = pygame.time.Clock()

    # set buttons
    back_button = Button(1000, 650, 150, 60, "Back", None, "chiller", 35, True, bice_blue,
                         image="images/ice-banner.png")
    select_button = Button((resolution[0] - 150) // 2, 600, 150, 60, "Select", None, "chiller", 35, True, bice_blue,
                           image="images/ice-banner.png")

    arrow_left = Button(100, 300, 200, 200, None, None, "chiller", 35, True, bice_blue,
                        image="images/arrow_left.png")
    arrow_right = Button(900, 300, 200, 200, None, None, "chiller", 35, True, bice_blue,
                         image="images/arrow_right.png")

    # list weapons
    weapons = [Snowball(), Slingshot()]

    # tracker for current weapon
    selector_current = 0

    # player_related instance to add weapon
    player = Player()

    # set running
    running = True
    while running:

        # set fps
        clock.tick(fps)

        # display background
        screen.blit(background, (0, 0))

        # get mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if back_button.is_clicked(mouse, ev):
                select_sound()
                return

            if select_button.is_clicked(mouse, ev):
                select_sound()
                player.change_weapon(weapons[selector_current])
                print(player.weapon)

            if arrow_left.is_clicked(mouse, ev):
                select_sound()
                if selector_current > 0:
                    selector_current -= 1
                else:
                    selector_current = len(weapons) - 1

            if arrow_right.is_clicked(mouse, ev):
                select_sound()
                if selector_current < len(weapons) - 1:
                    selector_current += 1
                else:
                    selector_current = 0

            if back_button.is_hovered(mouse):
                back_button.scale_up()
            else:
                back_button.scale_down()

            if select_button.is_hovered(mouse):
                select_button.scale_up()
            else:
                select_button.scale_down()

            if arrow_left.is_hovered(mouse):
                arrow_left.scale_up()
            else:
                arrow_left.scale_down()

            if arrow_right.is_hovered(mouse):
                arrow_right.scale_up()
            else:
                arrow_right.scale_down()

        # draw buttons
        back_button.draw(screen, mouse)
        select_button.draw(screen, mouse)
        arrow_left.draw(screen, mouse)
        arrow_right.draw(screen, mouse)

        # rescale current weapon
        current_weapon = weapons[selector_current]
        current_weapon.image = pygame.transform.scale(current_weapon.image, (150, 150))  # Adjust the scale as needed
        current_weapon.rect = current_weapon.image.get_rect(center=(resolution[0] // 2, resolution[1] // 2))

        # add current weapon to group
        weapons_group = pygame.sprite.Group(weapons[selector_current])

        # draw weapon
        weapons_group.draw(screen)

        pygame.display.update()
