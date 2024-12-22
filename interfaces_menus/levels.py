from interfaces_menus.button import Button


class Level:

    """
    A class to represent a level in the game.

    Attributes:
    -----------
    number : int
        The level number.
    button : Button
        The button associated with the level.
    """

    # initializing the Level
    def __init__(self, number, x, y, width, height, color, image):

        """
        Initializes the Level with a button.

        Parameters:
        -----------
        number : int
            The level number.
        x : int
            The x-coordinate of the button.
        y : int
            The y-coordinate of the button.
        width : int
            The width of the button.
        height : int
            The height of the button.
        color : tuple
            The color of the button.
        image : str
            The image file for the button.
        """

        self.number = number
        self.button = Button(x, y, width, height, str(number), None, "fonts/Grand9KPixel.ttf", 45, True, color,
                             image=image)

    # drawing the button in the screen
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

        self.button.draw(screen, mouse)

    # checking if the button is clicked
    def is_clicked(self, mouse, event):

        """
        Checks if the button is clicked.

        Parameters:
        -----------
        mouse : tuple
            The current position of the mouse cursor.
        event : pygame.event.Event
            The current event.

        Returns:
        --------
        bool
            True if the button is clicked, False otherwise.
        """

        return self.button.is_clicked(mouse, event)

    # checking if the button is hovered
    def is_hovered(self, mouse):

        """
        Checks if the button is hovered.

        Parameters:
        -----------
        mouse : tuple
            The current position of the mouse cursor.

        Returns:
        --------
        bool
            True if the button is hovered, False otherwise.
        """

        return self.button.is_hovered(mouse)

    # scale up and down buttons
    def scale_up(self):
        
        """
        Increases the size of the button when hovered.
        """

        self.button.scale_up()

    def scale_down(self):

        """
        Resets the button to its original size and position.
        """
        
        self.button.scale_down()
