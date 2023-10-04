from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0
        self.free_rooms = []
        self.taken_rooms = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def find_room_by_number(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room

        return None

    def take_room(self, room_number, people):
        room = self.find_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.find_room_by_number(room_number)
        room_guests = room.guests
        result = room.free_room()
        if result:
            return result

        self.guests -= room_guests

    def status(self):

        for room in self.rooms:
            if room.is_taken:
                self.taken_rooms.append(room.number)
            else:
                self.free_rooms.append(room.number)
        return f"Hotel {self.name} has {self.guests} total guests" + '\n' + \
            f"Free rooms: {', '.join(map(str, self.free_rooms))}" + '\n' + \
            f"Taken rooms: {', '.join(map(str, self.taken_rooms))}"





