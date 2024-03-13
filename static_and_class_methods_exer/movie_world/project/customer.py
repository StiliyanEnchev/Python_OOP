from typing import List

from project.dvd import DVD


class Customer:
    def __init__(self, name, age, personal_id):
        self.name = name
        self.age = age
        self.id = personal_id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has "
                f"{len(self.rented_dvds)} rented DVD's "
                f"({', '.join(dvd.name for dvd in self.rented_dvds)})")

