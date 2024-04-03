from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540
    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN)

    def miss(self, time_to_catch):
        result = round(self.oxygen_level - (0.30 * time_to_catch))

        if result <= 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = result

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN