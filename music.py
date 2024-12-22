import pygame


# class to handle music
class Music:
    def __init__(self, file):
        self.sound = file
        pygame.init()
        pygame.mixer.init()

    def play(self):
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()

    def volchange(self, volume):
        # changes the volume of the music (value between 0 and 1)
        pygame.mixer.music.set_volume(volume)

    def isplaying(self):
        # checks if theres music playing and returns a boolean
        return pygame.mixer.music.get_busy()