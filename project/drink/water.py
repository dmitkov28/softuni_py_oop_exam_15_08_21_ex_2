from project.drink.drink import Drink

class Water(Drink):
    def __init__(self, name, portion, brand):
        self.name = name
        self.portion = portion
        self.brand = brand
        self.price = 1.50

