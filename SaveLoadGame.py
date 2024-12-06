import os


# check if save file is not empty so load game doesn't crash
def check_save_file():
    if os.path.getsize("gamesave.txt") > 0:
        return True
    else:
        return False


class SaveManager:
    def __init__(self):
        self.save_file = "gamesave.txt"
        self.player_data = []

    def save_game(self, player):
        self.player_data.append(player.inventory.items)
        with open(self.save_file, "w") as file:
            for data in self.player_data:
                file.write(str(data) + "\n")

    def load_game(self):
        with open(self.save_file, "r") as file:
            for line in file:
                self.player_data.append(eval(line))
        return self.player_data
