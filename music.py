import pygame

class Music:
    def __init__(self, file):
        self.sound = file

    def play(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()

    @staticmethod
    def volchange(volume):
        pygame.mixer.music.set_volume(volume)

    @staticmethod
    def isplaying():
        return pygame.mixer.music.get_busy()