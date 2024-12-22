from config import *

# rectangle for fishing minigame
def draw_centered_rectangle(screen, height, color, outline_thickness):
    
    """
    Draws a centered rectangle on the screen.

    Parameters:
    -----------
    screen : pygame.Surface
        The Pygame display surface.
    height : int
        The height of the rectangle.
    color : tuple
        The color of the rectangle.
    outline_thickness : int
        The thickness of the rectangle's outline.
    """
    
    # calculate the dimensions and position of the rectangle
    rect_width = resolution[0] * 2 // 3
    rect_height = height
    rect_x = (resolution[0] - rect_width) // 2
    rect_y = (resolution[1] - rect_height) // 2

    # rectangle properties
    # outline color
    rect_color = color
    # thickness of the outline
    rect_thickness = outline_thickness

    # draw the rectangle
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height), rect_thickness)


# function to draw fishing bar for the fishing minigame
def draw_chasing_rectangle(screen, mouse_pos, height_centered, width_chasing, centered_color,
                           chasing_color):
    
    """
    Draws a chasing rectangle within a centered rectangle on the screen.

    Parameters:
    -----------
    screen : pygame.Surface
        The Pygame display surface.
    mouse_pos : tuple
        The current position of the mouse.
    height_centered : int
        The height of the centered rectangle.
    width_chasing : int
        The width of the chasing rectangle.
    centered_color : tuple
        The color of the centered rectangle.
    chasing_color : tuple
        The color of the chasing rectangle.

    Returns:
    --------
    pygame.Rect
        The chasing rectangle as a Pygame Rect object.
    """

    # calculate the dimensions and position of the centered rectangle
    rect_width = resolution[0] * 2 // 3
    rect_height = height_centered
    rect_x = (resolution[0] - rect_width) // 2
    rect_y = (resolution[1] - rect_height) // 2

    # create the centered rectangle
    centered_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    # calculate the dimensions and position of the chasing rectangle
    # adjust it so it does not overlap with the centered rectangle
    # outline thickness is set to 2
    inset_x = rect_x + 2
    inset_y = rect_y + 2
    inset_width = rect_width - 2 * 2

    # properties of the chasing rectangle
    chase_rect_width = width_chasing
    chase_rect_height = height_centered - 4
    chase_rect_x = mouse_pos[0] - chase_rect_width // 2
    chase_rect_y = inset_y

    # keep chasing rectangle within the centered rectangle
    if chase_rect_x < inset_x:
        chase_rect_x = inset_x
    elif chase_rect_x + chase_rect_width > inset_x + inset_width:
        chase_rect_x = inset_x + inset_width - chase_rect_width

    # create the chasing rectangle
    chasing_rect = pygame.Rect(chase_rect_x, chase_rect_y, chase_rect_width, chase_rect_height)

    # draw the centered rectangle (outline)
    pygame.draw.rect(screen, centered_color, centered_rect, 2)

    # draw the chasing rectangle (filled)
    pygame.draw.rect(screen, chasing_color, chasing_rect)

    # return as a pygame rect object
    return chasing_rect




