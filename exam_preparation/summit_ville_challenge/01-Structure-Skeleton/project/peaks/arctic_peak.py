from abc import ABC

from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak, ABC):

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return "Extreme"
        elif 2000 <= self.elevation <= 3000:
            return 'Advanced'




