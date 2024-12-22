class SaveManager:
    def __init__(self):
        self.save_file = "save_system/gamesave.txt"
        self.player_data = []

    def save_game(self, player):
        # clear previous player_related data and add current player_related data
        self.player_data = [player.inventory.items, player.balance, player.weapon, player.level, player.ptype,
                            player.health_cap, player.speed_cap, player.weapon_upgrades]
        # save player_related inventory
        with open(self.save_file, "w") as file:
            for data in self.player_data:
                file.write(str(data) + "\n")

    def load_game(self):
        # get inventory data from save file
        with open(self.save_file, "r") as file:
            self.player_data = [line.strip() for line in file]
        return self.player_data
    
    
    
        
        

   
