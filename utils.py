import pygame

from config import resolution, white, dark_red


# Function to draw a stick figure with a construction hat
def draw_stick_figure_with_hat(screen, x, y):
    # head
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 20, 2)  # White head outline

    # body
    pygame.draw.line(screen, (255, 255, 255), (x, y + 20), (x, y + 60), 2)  # Body

    # arms
    pygame.draw.line(screen, (255, 255, 255), (x, y + 40), (x - 30, y + 40), 2)  # Left arm
    pygame.draw.line(screen, (255, 255, 255), (x, y + 40), (x + 30, y + 40), 2)  # Right arm

    # legs
    pygame.draw.line(screen, (255, 255, 255), (x, y + 60), (x - 20, y + 100), 2)  # Left leg
    pygame.draw.line(screen, (255, 255, 255), (x, y + 60), (x + 20, y + 100), 2)  # Right leg

    # hat
    hat_color = (255, 215, 0)

    # drawing the construction hat
    pygame.draw.rect(screen, hat_color, [x - 25, y - 30, 50, 10])  # Hat's brim
    pygame.draw.rect(screen, hat_color, [x - 20, y - 40, 40, 20])  # Hat's dome


# Function to draw a normal stick figure (without a hat)
def draw_normal_stick_figure(screen, x, y):
    # head
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 20, 2)  # White head outline

    # body
    pygame.draw.line(screen, (255, 255, 255), (x, y + 20), (x, y + 60), 2)  # Body

    # arms
    pygame.draw.line(screen, (255, 255, 255), (x, y + 40), (x - 30, y + 40), 2)  # Left arm
    pygame.draw.line(screen, (255, 255, 255), (x, y + 40), (x + 30, y + 40), 2)  # Right arm

    # legs
    pygame.draw.line(screen, (255, 255, 255), (x, y + 60), (x - 20, y + 100), 2)  # Left leg
    pygame.draw.line(screen, (255, 255, 255), (x, y + 60), (x + 20, y + 100), 2)  # Right leg


# rectangle for fishing minigame
def draw_centered_rectangle(screen, height, color, outline_thickness):
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


def under_construction():
    # creating the screen at 720x720 pixels
    screen = pygame.display.set_mode(resolution)

    # setting up the fonts
    corbelfont = pygame.font.SysFont("Corbel", 50)
    conversation_font = pygame.font.SysFont("Arial", 30)

    # setting my texts:
    back_text = corbelfont.render("back", True, white)
    construction_text = corbelfont.render("UNDER CONSTRUCTION", True, white)
    first_speech = conversation_font.render("Can we fix it?", True, white)
    bob_speech = conversation_font.render("Probably not...", True, white)

    # setting up the "images" positions
    bob_x_position = 460
    bob_y_position = 450

    normal_x_position = 260
    normal_y_position = 450

    # same old, same old while True loop

    while True:
        # getting the mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return

            if ev.type == pygame.MOUSEBUTTONDOWN:
                # checking if the back button was clicked
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    return

        # displaying the screen:
        background = pygame.image.load('images/winter2.png')
        background = pygame.transform.scale(background, (resolution[0], resolution[1]))
        screen.blit(background, (0, 0))

        # displaying the main UNDER CONSTRUCTION text
        construction_rect = construction_text.get_rect(center=(720 // 2, 300))
        screen.blit(construction_text, construction_rect)

        # drawing the back button
        pygame.draw.rect(screen, dark_red, [450, 600, 140, 60])
        back_rect = back_text.get_rect(center=(450 + 140 // 2, 600 + 60 // 2))
        screen.blit(back_text, back_rect)

        # stick figures text and "images"
        draw_normal_stick_figure(screen, normal_x_position, normal_y_position)
        draw_stick_figure_with_hat(screen, bob_x_position, bob_y_position)

        screen.blit(first_speech, (normal_x_position - 60, normal_y_position - 80))
        screen.blit(bob_speech, (bob_x_position - 60, bob_y_position - 80))

        # finally, as always, updating our screen
        pygame.display.update()
