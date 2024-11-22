import pygame
from config import *


class Button:
    def __init__(self, x, y, width, height, text, color, font, font_size, image=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color if color else (255, 255, 255)  # Default to white if no color is passed
        self.font = font
        self.font_size = font_size
        self.image = image
        self.scaled_font = pygame.font.SysFont(self.font, self.font_size)  # Use the font passed as an argument

    def draw(self, screen, mouse):
        # Optionally use the image
        if self.image:
            button_image = pygame.image.load(self.image)
            button_image = pygame.transform.scale(button_image, (self.width, self.height))
            screen.blit(button_image, (self.x, self.y))

        # Draw the text with the scaled font
        text_surface = self.scaled_font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

    def is_clicked(self, mouse_pos, event):
        return self.is_hovered(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN

