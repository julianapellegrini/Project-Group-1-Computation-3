class Fish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs {self.price}"


class Salmon(Fish):
    def __init__(self):
        super().__init__("Salmon", 10)
