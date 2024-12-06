import pygame
from config import *


def select_sound():
    # playing sound
    hover_sound = pygame.mixer.Sound("../audio/button-select.mp3")
    hover_sound.set_volume(0.2)
    hover_sound.play()


class Button:
    def __init__(self, x, y, width, height, text, color, font, font_size, outline, outline_color, image=None):
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
        self.outline = outline
        self.outline_color = outline_color
        self.is_scaled = False
        self.original_size = (self.x, self.y, self.width, self.height)

    def draw(self, screen, mouse):

        if self.image:
            button_image = pygame.image.load(self.image)
            button_image = pygame.transform.scale(button_image, (self.width, self.height))
            screen.blit(button_image, (self.x, self.y))

        if self.outline:
            list1 = self.outline_()
            for i in list1:
                screen.blit(i[0], i[1])

        # Draw the text with the scaled font
        text_surface = self.scaled_font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

    def is_clicked(self, mouse_pos, event):
        return self.is_hovered(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN

    def outline_(self):

        text_surface1 = self.scaled_font.render(self.text, True, self.outline_color)
        text_rect1 = text_surface1.get_rect(center=((self.x + self.width // 2) - 1, self.y + self.height // 2))

        text_surface2 = self.scaled_font.render(self.text, True, self.outline_color)
        text_rect2 = text_surface2.get_rect(center=((self.x + self.width // 2) + 1, self.y + self.height // 2))

        text_surface3 = self.scaled_font.render(self.text, True, self.outline_color)
        text_rect3 = text_surface3.get_rect(center=(self.x + self.width // 2, (self.y + self.height // 2)+1))

        text_surface4 = self.scaled_font.render(self.text, True, self.outline_color)
        text_rect4 = text_surface4.get_rect(center=(self.x + self.width // 2, (self.y + self.height // 2) - 1))

        list1 = [(text_surface1, text_rect1), (text_surface2, text_rect2), (text_surface3, text_rect3), (text_surface4, text_rect4)]
        return list1

    def scale_up(self):
        if not self.is_scaled:  # Only scale up if not already scaled
            # increase in size
            new_width = self.width * 1.1
            new_height = self.height * 1.1

            # adjust x and y to keep the button centered
            self.x -= (new_width - self.width) / 2
            self.y -= (new_height - self.height) / 2

            # scaling up the button
            self.width = new_width
            self.height = new_height

            # playing sound
            hover_sound = pygame.mixer.Sound("../audio/hover.mp3")
            hover_sound.set_volume(0.3)
            hover_sound.play()

            self.is_scaled = True

    def scale_down(self):
        if self.is_scaled:
            # reset to original size and position
            self.x, self.y, self.width, self.height = self.original_size
            self.is_scaled = False

