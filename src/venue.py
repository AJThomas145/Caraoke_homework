class Venue:

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.number_of_rooms = []
        self.total_number_of_guests = 0
        self.capacity = 0
        self.total_revenue = 0

    def add_room(self, room):
        self.number_of_rooms.append(room)

    def total_number_of_rooms(self):
        return len(self.number_of_rooms)

    def total_capacity(self, room1, room2, room3):
        self.capacity += room1.capacity
        self.capacity += room2.capacity
        self.capacity += room3.capacity
        return self.capacity

    def total_number_of_guests_in_venue(self, room1, room2, room3):
        self.total_number_of_guests += len(room1.guests_in_room)
        self.total_number_of_guests += len(room2.guests_in_room)
        self.total_number_of_guests += len(room3.guests_in_room)
        return self.total_number_of_guests

    
        