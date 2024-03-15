class NextIdMixin:
    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def next_id(cls):
        cls.id += 1