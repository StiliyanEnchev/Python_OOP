from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, refuel):
        pass


class Car(Vehicle):
    CON_ON = 0.9

    def drive(self, distance):
        consumption = (self.CON_ON + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CON_ON = 1.6
    TANK_PERCENT_FILL = 0.95

    def drive(self, distance):
        consumption = (self.CON_ON + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.TANK_PERCENT_FILL


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

