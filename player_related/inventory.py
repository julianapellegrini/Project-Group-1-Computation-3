class Inventory:
    def __init__(self):
        self.items = {'Fishes': {'Salmon': 0, 'Cod': 0, 'ClownFish': 0},
                      'Weapons': {}}

    def add_item(self, item):
        if item.name in self.items['Fishes']:
            self.items['Fishes'][item.name] += 1
        elif item.name in self.items['Weapons']:
            self.items['Weapons'][item.name] = item

    def add_weapon(self, weapon):
        self.items['Weapons'][weapon.name] = weapon
