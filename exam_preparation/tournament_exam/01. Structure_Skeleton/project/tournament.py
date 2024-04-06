from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"ElbowPad": ElbowPad,
                       'KneePad': KneePad}

    VALID_TEAMS = {'IndoorTeam': IndoorTeam,
                   'OutdoorTeam': OutdoorTeam}

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type):

        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")

        equipment_class = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(equipment_class)
        return f"{equipment_type} was successfully added."
    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.VALID_TEAMS[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."
    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(filter(lambda t: t.name == team_name, self.teams))
        equipment = next(filter(lambda e: e.__class__.__name__ == equipment_type, reversed(self.equipment)))

        if team.budget < equipment.price:
            raise Exception("Invalid equipment type!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."
    def increase_equipment_price(self, equipment_type: str):

        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        number_of_raised_equipments = 0

        for eq in equipment:
            eq.increase_price()
            number_of_raised_equipments += 1

        return f"Successfully changed {number_of_raised_equipments}pcs of equipment."
    def play(self, team_name1: str, team_name2: str):
        team1 = next(filter(lambda t: t.name == team_name1, self.teams))
        team2 = next(filter(lambda t: t.name == team_name2, self.teams))

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_total_points = sum([eq.protection for eq in team1.equipment]) + team1.advantage
        team2_total_points = sum([eq.protection for eq in team2.equipment]) + team2.advantage

        if team1_total_points > team2_total_points:
            team1.win()
            return f"The winner is {team1.name}."

        elif team1_total_points < team2_total_points:
            team2.win()
            return f"The winner is {team2.name}."

        else:
            return "No winner in this game."
    def get_statistics(self):
        result = (f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:")

        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        for team in reversed(sorted_teams):
            result += f'{team.get_statistics()}'

        return result