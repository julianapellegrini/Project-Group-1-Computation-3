import pickle
import os


def check_save():
    return os.path.isfile('savegame.pickle')


class SaveManager:
    def __init__(self):
        self.save_dict = None

    def save_game(self, player):
        self.save_dict = player.inventory.items

        save_file = 'savegame.pickle'
        with open(save_file, 'wb') as f:
            pickle.dump(self.save_dict, f)

    def load_game(self):
        save_file = 'savegame.pickle'
        with open(save_file, 'rb') as f:
            self.save_dict = pickle.load(f)
        return self.save_dict

