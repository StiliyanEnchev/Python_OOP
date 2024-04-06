from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, protection, price: float):
        self.protection = protection
        self.price: float = price

    @abstractmethod
    def increase_price(self):
        pass

