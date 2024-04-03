from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN = 120
    def __init__(self, name):
        super().__init__(name, FreeDiver.INITIAL_OXYGEN)

    def miss(self, time_to_catch):
        result = round(self.oxygen_level - (0.60 * time_to_catch))

        if result <= 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = result

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.INITIAL_OXYGEN