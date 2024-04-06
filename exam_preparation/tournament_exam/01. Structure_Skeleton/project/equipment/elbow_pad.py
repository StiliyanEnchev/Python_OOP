from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    ELBOW_PAD_PROTECTION = 90
    ELBOW_PAD_PRICE = 25.0

    def __init__(self):
        super().__init__(ElbowPad.ELBOW_PAD_PROTECTION, ElbowPad.ELBOW_PAD_PRICE)

    def increase_price(self):
        self.price += 0.10 * self.price

