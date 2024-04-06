from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    KNEE_PAD_PROTECTION = 120
    KNEE_PAD_PRICE = 15.0
    def __init__(self):
        super().__init__(self.KNEE_PAD_PROTECTION, self.KNEE_PAD_PRICE)

    def increase_price(self):
        self.price += 0.20 * self.price
