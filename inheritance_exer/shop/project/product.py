class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, given_quantity):
        if self.quantity >= given_quantity:
            self.quantity -= given_quantity

    def increase(self, given_quantity):
        self.quantity += given_quantity

    def __repr__(self):
        return self.name
