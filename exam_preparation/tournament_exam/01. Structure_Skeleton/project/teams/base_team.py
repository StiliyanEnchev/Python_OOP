import math
from abc import ABC, abstractmethod
from typing import List


class BaseTeam(ABC):
    def __init__(self, name, country, advantage, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget: float = budget
        self.wins = 0
        self.equipment: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Team name cannot be empty!")

        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")

        self.__country = value

    @property
    def advantage(self):
        return self.__advantage
    
    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")

        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_price_of_team_equipment = sum([item.price for item in self.equipment])
        avg_team_protection = math.floor(sum([item.protection for item in self.equipment]))

        return (f"\nName: {self.name}"
                f"\nCountry: {self.country}"
                f"\nAdvantage: {self.advantage} points"
                f"\nBudget: {self.budget:.2f}EUR"
                f"\nWins: {self.wins}"
                f"\nTotal Equipment Price: {total_price_of_team_equipment:.2f}"
                f"\nAverage Protection: {avg_team_protection}")

