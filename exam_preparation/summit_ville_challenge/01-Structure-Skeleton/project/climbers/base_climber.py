from abc import ABC, abstractmethod
from typing import List

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.conquered_peaks: List = []
        self.is_prepared = True

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        return (f"{self.__class__.__name__}: /// "
                f"Climber name: {self.name} * "
                f"Left strength: {self.strength} * "
                f"Conquered peaks: {', '.join(peak for peak in sorted(self.conquered_peaks))} ///")

