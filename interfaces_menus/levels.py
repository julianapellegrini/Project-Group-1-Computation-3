import pygame
from config import *
from interfaces_menus.button import Button

class Level:
    # initializing the Level
    def __init__(self, number, x, y, width, height, color, image):
        self.number = number
        self.button = Button(x, y, width, height, str(number), None, "fonts/Grand9KPixel.ttf", 45, True, color, image=image)

    # drawing the button in the screen
    def draw(self, screen, mouse):
        self.button.draw(screen, mouse)

    # checking if the button is clicked
    def is_clicked(self, mouse, event):
        return self.button.is_clicked(mouse, event)

    # checking if the button is hovered
    def is_hovered(self, mouse):
        return self.button.is_hovered(mouse)

    # Scale up and down buttons
    def scale_up(self):
        self.button.scale_up()

    def scale_down(self):
        self.button.scale_down()