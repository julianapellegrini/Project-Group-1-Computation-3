from powerups.powerup import PowerUp


class DeSpawner(PowerUp):

    def __init__(self):
        super().__init__('powerup_images/Despawner_icon.png', 'powerup_images/Despawner_image.png', 0.6)
        self.reduction_factor = 0.5

    def affect_player(self, surface, player):
        pass

    def affect_game(self):
        pass

    def deactivate(self):
        pass
