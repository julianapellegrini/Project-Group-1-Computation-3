class Inventory:
    def __init__(self):
        self.items = {'Fishes': {'Salmon': 0, 'Cod': 0, 'ClownFish': 0}, 'Weapons': {}, 'Powerups': {}}

    def add_item(self, item):
        if item.name in self.items['Fishes']:
            self.items['Fishes'][item.name] += 1
        elif item.name in self.items['Weapons']:
            self.items['Weapons'][item.name] = item
        elif item.name in self.items['Powerups']:
            self.items['Powerups'][item.name] = item

    def add_weapon(self, weapon):
        if 'Weapons' not in self.items:
            self.items['Weapons'] = {}
        self.items['Weapons'][weapon.name] = weapon