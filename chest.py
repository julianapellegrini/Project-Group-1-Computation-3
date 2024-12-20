import pygame
import random
from powerups.despawner import DeSpawner
from powerups.invincibility import Invincibility
from powerups.extra_fish import Extra_Fish
from powerups.speed_boost import Speed_Boost
from player_related.weapons import Snowball, Slingshot, Fish_bazooka, Ice_Ninja_Stars

class Chest(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/chest_image.png")  # load the image
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
        if not self.spawned:
            # define map boundaries
            map_width, map_height = surface.get_size()

            # generate random position within boundaries
            random_x = random.randint(0, map_width - self.rect.width)
            random_y = random.randint(0, map_height - self.rect.height)

            # set the rect position to the random coordinates
            self.rect.topleft = (random_x, random_y)

            # set spawned to True
            self.spawned = True

            print(f"Chest spawned at {self.rect.topleft}")

        # draw the chest
        surface.blit(self.image, self.rect.topleft)

    def select_options(self):
        # Separate the items and probabilities to then choose the items based on their probabilities
        items = list(self.possible_items.keys())
        probabilities = list(self.possible_items.values())
        # Select 3 random items based on their probabilities
        self.options = random.choices(items, probabilities, k=3)
        print(f"Selected options: {self.options}")

    def display_options(self, surface, enemies, spawn_chances, player):
        # Pause the game
        paused = True

        # Create a semi-transparent overlay
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Black with 50% opacity

        # Display the overlay
        surface.blit(overlay, (0, 0))

        # Define dimensions for images and their positions
        option_width = 150
        option_height = 150
        padding = 20
        total_width = len(self.options) * (option_width + padding) - padding
        start_x = (surface.get_width() - total_width) // 2
        y_position = (surface.get_height() - option_height) // 2 - 50  # Offset upward for names

        # Load and display the options as images
        option_images = []
        for option in self.options:
            image_path = f"chest_option_images/{option.lower().replace(' ', '_')}.png"  # Example image naming convention
            option_image = pygame.image.load(image_path).convert_alpha()
            option_image = pygame.transform.scale(option_image, (option_width, option_height))
            option_images.append(option_image)

        option_rects = []
        font = pygame.font.Font(None, 36)
        for i, (option_image, option) in enumerate(zip(option_images, self.options)):
            # Calculate x position for this option
            x_position = start_x + i * (option_width + padding)

            # Draw the option image
            surface.blit(option_image, (x_position, y_position))

            # Draw the option name below the image
            text = font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(center=(x_position + option_width // 2, y_position + option_height + 20))
            surface.blit(text, text_rect)

            # Save the clickable area (the image)
            option_rects.append(pygame.Rect(x_position, y_position, option_width, option_height))

        # Update the display
        pygame.display.flip()

        # Wait for the player to select an item
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Press Enter to continue without selecting
                        paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = event.pos
                        for rect, option in zip(option_rects, self.options):
                            if rect.collidepoint(mouse_pos):
                                # If user selects a weapon, change the player's weapon
                                if option in self.weapons:
                                    if option == "Slingshot":
                                        player.weapon = Slingshot()
                                    elif option == "Snowball":
                                        player.weapon = Snowball()
                                    elif option == "Fish Bazooka":
                                        player.weapon = Fish_bazooka()
                                    elif option == "Ice Ninja Stars":
                                        player.weapon = Ice_Ninja_Stars()
                                    print(f"Player weapon changed to {option}")
                                # If user selects a powerup, apply the powerup
                                elif option in self.powerups:
                                    if option == "Despawner":
                                        powerup = DeSpawner()
                                        powerup.affect_game(surface, enemies, spawn_chances, player)
                                        player.powerup = powerup
                                    elif option == "Invincibility":
                                        powerup = Invincibility()
                                        powerup.affect_player(surface, player)
                                        player.powerup = powerup
                                    elif option == "Extra Fish":
                                        powerup = Extra_Fish()
                                        powerup.affect_player(surface, player)
                                        player.powerup = powerup
                                    elif option == "Speed Boost":
                                        powerup = Speed_Boost()
                                        powerup.affect_player(surface, player)
                                        player.powerup = powerup
                                    # Set the start time for the powerup
                                    player.powerup_start = pygame.time.get_ticks()
                                    print(f"Applied powerup: {option}")
                                paused = False  # Exit the loop after selecting an item
                                break
                        if not paused:
                            break  # Exit the outer loop as well



    # Method to use when actually colliding with the chest
    def open(self, surface, enemies, spawn_chances, player):
        self.select_options()
        self.display_options(surface, enemies, spawn_chances, player)