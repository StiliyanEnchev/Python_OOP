from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    MIN_STR_NEEDED = 75
    INITIAL_STR = 150

    def __init__(self, name):
        super().__init__(name, SummitClimber.INITIAL_STR)

    def can_climb(self):
        return self.strength >= SummitClimber.MIN_STR_NEEDED

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == 'Advanced':
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5

        self.conquered_peaks.append(peak.name)
