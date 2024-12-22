# class for player's inventory
class Inventory:

    """
    A class to represent the player's inventory.

    Attributes:
    -----------
    items : dict
        A dictionary containing the items in the inventory, categorized by type.
    """

    def __init__(self):

        """
        Initializes the Inventory with default items and their quantities.
        """

        self.items = {'Fishes': {'Salmon': 0, 'Cod': 0, 'ClownFish': 0},
                      'Weapons': {'Watergun': 0, 'Snowball': 0, 'Slingshot': 0, 'Fish Bazooka': 0, 'Ice Ninja Stars': 0}}

    # adding to the item amount on the inventory depending on the item's type
    def add_item(self, item):

        """
        Adds an item to the inventory.

        Parameters:
        -----------
        item : object
            The item object to be added to the inventory.
        """
        
        if item.name in self.items['Fishes']:
            self.items['Fishes'][item.name] += 1
        elif item.name in self.items['Weapons']:
            self.items['Weapons'][item.name] += 1
