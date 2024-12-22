import pygame
from config import resolution

bg_images = []


# load the background images
def load_backgrounds():
    global bg_images
    for i in range(1, 6):
        bg_image = pygame.image.load(f"bg/Plan{i}.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, resolution)
        bg_images.append(bg_image)


# draw the moving background
def draw_bg(screen, scroll):
    global bg_images

    bg_width = bg_images[0].get_width()
    for x in range(50):
        speed = 1
        for bg_image in bg_images:
            screen.blit(bg_image, ((x * bg_width) - scroll * speed, 0))
            speed += 0.3
