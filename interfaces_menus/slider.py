from config import *

class Slider:
    def __init__(self, x, y, w, h, min_val, max_val, start_val):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.handle_rect = pygame.Rect(x + (start_val - min_val) / (max_val - min_val) * w - h // 2, y - h // 2, h, h)
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, light_brown, self.rect)
        pygame.draw.rect(screen, brown, self.handle_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.handle_rect.x = max(self.rect.x, min(event.pos[0] - self.handle_rect.width // 2, self.rect.x + self.rect.width - self.handle_rect.width))
                self.value = self.min_val + (self.handle_rect.x - self.rect.x) / self.rect.width * (self.max_val - self.min_val)