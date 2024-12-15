import pygame
import random
from player_related.player import player
from powerups.powerup import Powerup
from powerups.despawner import Despawner
from powerups.invincibility import Invincibility
from powerups.extra_fish import ExtraFish
from powerups.speed_boost import SpeedBoost
from player_related.weapons import Snowball
from player_related.weapons import Slingshot

class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/treasure_chest.png") # load the image
        self.image = pygame.transform.scale(self.image, (150, 150))  # scale the image
        self.rect = self.image.get_rect()
        self.spawned = False
        self.possible_items = {
            "Despawner": 0.25,
            "Invincibility": 0.2,
            "Extra Fish": 0.10,
            "Speed Boost": 0.15,
            "Snowball": 0.2,
            "Slingshot": 0.1
        }
        self.options = []
        self.weapons = ["Snowball", "Slingshot"]
        self.powerups = ["Despawner", "Invincibility", "Extra Fish", "Speed Boost"]

    def spawn(self, surface):
        # check if chest is not already spawned and spawn it
        # if its already spawned it will be drawn again at the position it was spawned
        if not self.spawned:
            # define map boundaries
            map_width, map_height = surface.get_size()

            # generate random position within boundaries
            random_x = random.randint(0, map_width - self.rect.width)
            random_y = random.randint(0, map_height - self.rect.height)

            # set the rect position to the random coordinates, using the top left corner of the icon
            self.rect.topleft = (random_x, random_y)

            # set spawned to True
            self.spawned = True

            print(f"Chest spawned at {self.rect.topleft}")

        # draw the chest
        surface.blit(self.image, self.rect.topleft)

    def select_options(self):
        # seperating the items and porbabilities to then choose the items based on their probabilities
        items = list(self.possible_items.keys())
        probabilities = list(self.possible_items.values())
        # Select 3 random items based on their probabilities
        self.options = random.choices(items, probabilities, k=3)
        print(f"Selected options: {self.options}")

    def open_chest(self, surface, player):
        self.select_options()
        self.display_options(surface, player)

    def display_options(self, surface, player):
        # Pause the game
        paused = True

        # Create a semi-transparent overlay
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Black with 50% opacity

        # Display the overlay
        surface.blit(overlay, (0, 0))

        # Display the options
        font = pygame.font.Font(None, 36)
        text_y = 100
        option_rects = []
        for option in self.options:
            text = font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(topleft=(100, text_y))
            option_rects.append((text_rect, option))
            surface.blit(text, text_rect.topleft)
            text_y += 50

        # Update the display
        pygame.display.flip()
    
        # Wait for the player to collect the items
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Press Enter to continue
                        paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = event.pos
                        for rect, option in option_rects:
                            if rect.collidepoint(mouse_pos):
                                #If user selects a weapon, change the player's weapon
                                if option in self.weapons:
                                    player.weapon = option
                                    print(f"Player weapon changed to {option}")
                                #If user selects a powerup, apply the powerup
                                elif option in self.powerups:
                                    if option == "Despawner":
                                        powerup = Despawner()
                                        powerup.affect_game()
                                    elif option == "Invincibility":
                                        powerup = Invincibility()
                                        powerup.affect_player()
                                    elif option == "Extra Fish":
                                        powerup = ExtraFish()
                                        powerup.affect_player()
                                    elif option == "Speed Boost":
                                        powerup = SpeedBoost()
                                        powerup.affect_player()
                                    print(f"Applied powerup: {option}")
                                paused = False  # Exit the loop after selecting one item
                                break
                    if not paused:
                        break  # Exit the outer loop as well

        