from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int):

        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):

        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):

        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'

        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_to_pay = sum([w.salary for w in self.workers])

        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_to_feed_animals = sum([a.money_for_care for a in self.animals])

        if money_to_feed_animals <= self.__budget:
            self.__budget -= money_to_feed_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        amount_of_lions = len(lions)
        result += f"----- {amount_of_lions} Lions:\n"

        for lion in lions:
            result += f'{lion}\n'

        tigers = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        amount_of_tigers = len(tigers)
        result += f"----- {amount_of_tigers} Tigers:\n"

        for tiger in tigers:
            result += f'{tiger}\n'

        cheetahs = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']
        amount_of_cheetahs = len(cheetahs)
        result += f"----- {amount_of_cheetahs} Cheetahs:\n"

        for cheetah in cheetahs:
            result += f'{cheetah}\n'

        return result[:-1]

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        caretakers = [k for k in self.workers if k.__class__.__name__ == 'Caretaker']
        vets = [v for v in self.workers if v.__class__.__name__ == 'Vet']

        result += f"----- {len(keepers)} Keepers:\n"

        for k in keepers:
            result += f'{k}\n'

        result += f"----- {len(caretakers)} Caretakers:\n"

        for c in caretakers:
            result += f'{c}\n'

        result += f"----- {len(vets)} Vets:\n"

        for v in vets:
            result += f'{v}\n'

        return result[:-1]

