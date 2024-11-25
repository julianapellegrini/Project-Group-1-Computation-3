class Invincibility(PowerUp):
    def __init__(self, duration, image_path):
        super().__init__(image_path)
        self.duration = duration

    def affect_player(self, player):
        player.invincible = True
        self.active = True
        pygame.time.set_timer(pygame.USEREVENT + 1, self.duration)

    def affect_game(self, spawn_rate):
        return spawn_rate  # No change to spawn rate

    def deactivate(self, player, spawn_rate):
        player.invincible = False
        self.active = False
        return spawn_rate
    
    def draw(self, surface):
        if self.player:
            # Position the power-up image around the player
            self.rect.center = self.player.rect.center
            surface.blit(self.image, self.rect.topleft)