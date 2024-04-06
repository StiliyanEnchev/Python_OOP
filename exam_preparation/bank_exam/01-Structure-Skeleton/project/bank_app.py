from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    VALID_LOANS = {'StudentLoan': StudentLoan,
                   'MortgageLoan': MortgageLoan}

    VALID_CLIENTS = {'Student': Student,
                     'Adult': Adult}

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if self.capacity < 1:
            return "Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        self.capacity -= 1
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda lo: lo.__class__.__name__ == loan_type, self.loans))

        client_type_name = client.__class__.__name__
        loan_type_name = loan.__class__.__name__

        if client_type_name == 'Adult' and loan_type_name == 'StudentLoan' or client_type_name == 'Student' and loan_type_name == 'MortgageLoan':
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
    def remove_client(self, client_id: str):

        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        increased_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                increased_loans += 1

        return f"Successfully changed {increased_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        increased_rates = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                increased_rates += 1


        return f"Number of clients affected: {increased_rates}."

    def get_statistics(self):
        active_clients = [c for c in self.clients if len(c.loans) > 0]
        granted_loans = [loan.amount for client in active_clients for loan in client.loans]
        available_loan_sum = sum([loan.amount for loan in self.loans])
        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        result = (f"Active Clients: {len(active_clients)}\n"
                  f"Total Income: {sum([c.income for c in active_clients]):.2f}\n"
                  f"Granted Loans: {len(granted_loans)}, Total Sum: {sum(granted_loans):.2f}\n"
                  f"Available Loans: {len(self.loans)}, Total Sum: {available_loan_sum:.2f}\n"
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

        return result