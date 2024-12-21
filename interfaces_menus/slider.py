from config import *

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, start_val):
        self.bar = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.button = pygame.Rect((x + (start_val - min_val) / (max_val - min_val) * width - height // 2) - 3, y - 3, height + 7, height + 7)
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, light_brown, self.bar)
        pygame.draw.rect(screen, brown, self.button)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.button.x = max(self.bar.x, min(event.pos[0] - self.button.width // 2, self.bar.x + self.bar.width - self.button.width))
                self.value = self.min_val + (self.button.x - self.bar.x) / self.bar.width * (self.max_val - self.min_val)