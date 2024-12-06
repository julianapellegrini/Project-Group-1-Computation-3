import pickle


class SaveManager:
    def __init__(self):
        self.save_dict = {}

    def save_game(self, player):
        self.save_dict['inventory'] = player.inventory

        save_file = 'savegame.pickle'
        pickle.dump(self.save_dict, open(save_file, 'wb'))

    def load_game(self):
        save_file = 'savegame.pickle'
        self.save_dict = pickle.load(open(save_file, 'rb'))
        return self.save_dict
