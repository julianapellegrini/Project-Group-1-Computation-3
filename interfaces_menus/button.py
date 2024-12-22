from config import *


def select_sound():

    """
    Plays a sound when a button is selected.

    This function loads a sound file, sets its volume, and plays it.
    """

    # playing sound
    hover_sound = pygame.mixer.Sound("audio/button-select.mp3")
    hover_sound.set_volume(Button.sound_volume)
    hover_sound.play()


class Button:

    """
    A class to represent a button in a Pygame interface.

    Attributes:
    -----------
    sound_volume : float
        Class attribute to set the volume of the button sound.
    x : int
        The x-coordinate of the button.
    y : int
        The y-coordinate of the button.
    width : int
        The width of the button.
    height : int
        The height of the button.
    text : str
        The text displayed on the button.
    color : tuple
        The color of the button.
    font : str
        The font of the button text.
    font_size : int
        The size of the button text font.
    outline : bool
        Whether the button has an outline.
    outline_color : tuple
        The color of the button outline.
    image : str, optional
        The image file for the button (default is None).
    scaled_font : pygame.font.Font
        The scaled font object for the button text.
    is_scaled : bool
        Whether the button is scaled.
    original_size : tuple
        The original size and position of the button.
    """

    sound_volume = 0.2

    def __init__(self, x, y, width, height, text, color, font, font_size, outline, outline_color, image=None):
        """
        Constructs all the necessary attributes for the button object.

        Parameters:
        -----------
        x : int
            The x-coordinate of the button.
        y : int
            The y-coordinate of the button.
        width : int
            The width of the button.
        height : int
            The height of the button.
        text : str
            The text displayed on the button.
        color : tuple
            The color of the button.
        font : str
            The font of the button text.
        font_size : int
            The size of the button text font.
        outline : bool
            Whether the button has an outline.
        outline_color : tuple
            The color of the button outline.
        image : str, optional
            The image file for the button (default is None).
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color if color else (255, 255, 255)  # default to white if no color is passed
        self.font = font
        self.font_size = font_size
        self.image = image
        self.scaled_font = pygame.font.Font(self.font, self.font_size)  # use the font passed as an argument
        self.outline = outline
        self.outline_color = outline_color
        self.is_scaled = False
        self.original_size = (self.x, self.y, self.width, self.height)

    def draw(self, screen, mouse):

        """
        Draws the button on the screen.

        Parameters:
        -----------
        screen : pygame.Surface
            The surface on which the button is drawn.
        mouse : tuple
            The current position of the mouse cursor.
        """

        if self.image:
            button_image = pygame.image.load(self.image)
            button_image = pygame.transform.scale(button_image, (self.width, self.height))
            screen.blit(button_image, (self.x, self.y))

        if self.outline:
            list1 = self.outline_()
            for i in list1:
                screen.blit(i[0], i[1])

        # draw the text with the scaled font
        text_surface = self.scaled_font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    # check if the button is hovered
    def is_hovered(self, mouse_pos):

        """
        Checks if the button is hovered.

        Parameters:
        -----------
        mouse_pos : tuple
            The current position of the mouse cursor.

        Returns:
        --------
        bool
            True if the button is hovered, False otherwise.
        """
        
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

    # check if the button is clicked
    def is_clicked(self, mouse_pos, event):

        """
        Checks if the button is clicked.

        Parameters:
        -----------
        mouse_pos : tuple
            The current position of the mouse cursor.
        event : pygame.event.Event
            The current event.

        Returns:
        --------
        bool
            True if the button is clicked, False otherwise.
        """
        
        return self.is_hovered(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN

    # add an outline to the text
    def outline_(self):

        """
        Adds an outline to the text.

        Returns:
        --------
        list
            A list of tuples containing the text surfaces and their corresponding rectangles.
        """
        text_surface1 = self.scaled_font.render(self.text, True, self.outline_color)
        text_rect1 = text_surface1.get_rect(center=((self.x + self.width // 2) - 1, self.y + self.height // 2))

        text_surface2 = self.scaled_font.render(self.text, True, self.outline_color)
        text_rect2 = text_surface2.get_rect(center=((self.x + self.width // 2) + 1, self.y + self.height // 2))

        text_surface3 = self.scaled_font.render(self.text, True, self.outline_color)
        text_rect3 = text_surface3.get_rect(center=(self.x + self.width // 2, (self.y + self.height // 2) + 1))

        text_surface4 = self.scaled_font.render(self.text, True, self.outline_color)
        text_rect4 = text_surface4.get_rect(center=(self.x + self.width // 2, (self.y + self.height // 2) - 1))

        list1 = [(text_surface1, text_rect1), (text_surface2, text_rect2), (text_surface3, text_rect3),
                 (text_surface4, text_rect4)]
        return list1

    # increase the size of the button when hovered
    def scale_up(self):

        """
        Increases the size of the button when hovered.
        """
        
        if not self.is_scaled:
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
            hover_sound = pygame.mixer.Sound("audio/hover.mp3")
            hover_sound.set_volume(Button.sound_volume)
            hover_sound.play()

            self.is_scaled = True

    def scale_down(self):

        """
        Resets the button to its original size and position.

        This method is called when the button is no longer hovered.
        """
        
        if self.is_scaled:
            # reset to original size and position
            self.x, self.y, self.width, self.height = self.original_size
            self.is_scaled = False

