from abc import ABC


class Food(ABC):
    def __init__(self, quantity):
        self.quantity = quantity


class Fruit(Food):
    pass


class Meat(Food):
    pass


class Seed(Food):
    pass


class Vegetable(Food):
    pass