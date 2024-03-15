from project.next_id_mixin import NextIdMixin


class Customer(NextIdMixin):
    id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self.next_id()



    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
