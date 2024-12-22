import pygame

# class to handle music
class Music:
    """
    A class to handle music playback.

    Attributes:
    -----------
    sound : str
        The file path to the music file.
    """

    def __init__(self, file):
        """
        Initializes the Music class with the given file.

        Parameters:
        -----------
        file : str
            The file path to the music file.
        """
        self.sound = file
        pygame.init()
        pygame.mixer.init()

    def play(self):
        """
        Plays the music file.
        """
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()

    def volchange(self, volume):
        """
        Changes the volume of the music.

        Parameters:
        -----------
        volume : float
            The volume level to set, between 0 and 1.
        """
        pygame.mixer.music.set_volume(volume)

    def isplaying(self):
        """
        Checks if there is music playing.

        Returns:
        --------
        bool
            True if music is playing, False otherwise.
        """
        return pygame.mixer.music.get_busy()