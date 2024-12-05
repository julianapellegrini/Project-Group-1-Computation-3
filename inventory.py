class Inventory:
    def __init__(self):
        self.items = {'Fishes': {'Salmon': 0, 'Cod': 0, 'ClownFish': 0}}

    def add_item(self, item):
        if item.name in self.items['Fishes']:
            self.items['Fishes'][item.name] += 1
