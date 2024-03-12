from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.guests = 0
        self.rooms: List[Room] = []

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        people = room.guests
        result = room.free_room()

        if not result:
            self.guests -= people

    def status(self):
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"
                f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}")