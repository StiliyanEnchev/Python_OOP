from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return self.__radius ** 2 * pi

    def calculate_perimeter(self):
        return 2 * pi * self.__radius



class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__weight = width

    def calculate_perimeter(self):
        return 2 * (self.__weight + self.__height)

    def calculate_area(self):
        return self.__weight * self.__height


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


