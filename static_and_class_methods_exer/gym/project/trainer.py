from project.next_id_mixin import NextIdMixin


class Trainer(NextIdMixin):
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()
        self.next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

