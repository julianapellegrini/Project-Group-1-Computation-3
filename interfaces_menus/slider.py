from config import *


# class to create a slider
class Slider:
    """
    A class to create a slider.

    Attributes:
    -----------
    bar : pygame.Rect
        The rectangle representing the slider bar.
    min_val : int
        The minimum value of the slider.
    max_val : int
        The maximum value of the slider.
    value : int
        The current value of the slider.
    button : pygame.Rect
        The rectangle representing the slider button.
    dragging : bool
        Whether the slider button is being dragged.
    offset_x : int
        The offset of the mouse position from the button's position.
    """

    def __init__(self, x, y, width, height, min_val, max_val, start_val):
        
        """
        Initializes the Slider with the given parameters.

        Parameters:
        -----------
        x : int
            The x-coordinate of the slider.
        y : int
            The y-coordinate of the slider.
        width : int
            The width of the slider.
        height : int
            The height of the slider.
        min_val : int
            The minimum value of the slider.
        max_val : int
            The maximum value of the slider.
        start_val : int
            The starting value of the slider.
        """

        self.bar = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.button = pygame.Rect((x + (start_val - min_val) / (max_val - min_val) * width - height // 2) - 3, y - 3, height + 7, height + 7)
        self.dragging = False
        self.offset_x = 0

    # draw the slider
    def draw(self, screen):

        """
        Draws the slider on the screen.

        Parameters:
        -----------
        screen : pygame.Surface
            The Pygame display surface.
        """

        # recalculate the button's position based on the current value
        self.button.x = self.bar.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.bar.width - self.button.width // 2
        pygame.draw.rect(screen, light_brown, self.bar)
        pygame.draw.rect(screen, brown, self.button)

    # handle the slider events like dragging
    def handle_event(self, event):

        """
        Handles the slider events like dragging.

        Parameters:
        -----------
        event : pygame.event.Event
            The current event.
        """
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.collidepoint(event.pos):
                self.dragging = True
                self.offset_x = event.pos[0] - self.button.x
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                new_x = event.pos[0] - self.offset_x
                self.button.x = max(self.bar.x, min(new_x, self.bar.x + self.bar.width - self.button.width))
                self.value = self.min_val + (self.button.x - self.bar.x) / self.bar.width * (self.max_val - self.min_val)
