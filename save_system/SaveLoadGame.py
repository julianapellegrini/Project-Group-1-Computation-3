# function to save and load game data
class SaveManager:

    """
    A class to manage saving and loading game data.

    Attributes:
    -----------
    save_file : str
        The path to the save file.
    player_data : list
        A list to store player data.
    """

    def __init__(self):

        """
        Initializes the SaveManager with default attributes.
        """

        self.save_file = "save_system/gamesave.txt"  # save file path
        self.player_data = []  # list to store player data

    def save_game(self, player):

        """
        Saves the game data to the save file.

        Parameters:
        -----------
        player : object
            The player object containing the data to be saved.
        """

        # clear previous player data and add current player data
        self.player_data = [player.inventory.items, player.balance, player.weapon, player.level, player.ptype,
                            player.health_cap, player.speed_cap, player.snowball.damage, player.slingshot.damage,
                            player.fish_bazooka.damage, player.ice_ninja_stars.damage, player.sardine_shooter.damage,
                            player.weapon_upgrades]
        # save player data to save file
        with open(self.save_file, "w") as file:
            for data in self.player_data:
                file.write(str(data) + "\n")

    # gets each line from the save file and returns it as a list
    # will be used in the player class to load the game
    def load_game(self):

        """
        Loads the game data from the save file.

        Returns:
        --------
        list
            A list of player data loaded from the save file.
        """
        
        # get inventory data from save file
        with open(self.save_file, "r") as file:
            self.player_data = [line.strip() for line in file]
        return self.player_data
    
    
    
        
        

   
