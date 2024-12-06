import os


# check if save file is not empty so load game doesn't crash
def check_save_file():
    if os.path.getsize("save_system/gamesave.txt") > 0:
        return True
    else:
        return False


class SaveManager:
    def __init__(self):
        self.save_file = "save_system/gamesave.txt"
        self.player_data = []

    def save_game(self, player):
        # clear previous player_related data and add current player_related data
        self.player_data = [player.inventory.items]
        # save player_related inventory
        with open(self.save_file, "w") as file:
            for data in self.player_data:
                file.write(str(data) + "\n")

    def load_game(self):
        # get inventory data from save file
        with open(self.save_file, "r") as file:
            self.player_data = [eval(line) for line in file]
        return self.player_data[-1] if self.player_data else None
