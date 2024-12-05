class Inventory:
    def __init__(self):
        self.items = [{'Fishes': {'Salmon': 0, 'Cod': 0, 'ClownFish': 0}}]

    def add_item(self, item):
        if item in self.items[0]['Fishes']:
            self.items[0]['Fishes'][item] += 1
