class Room:

    def __init__(self, input_name):
        self.name = input_name
        self.guests_in_room = []
        self.capacity = 5
        self.songs_to_sing = []

    def add_guest_to_room(self, guest):
        self.guests_in_room.append(guest)

    def remove_guest_from_room(self, guest):
        self.guests_in_room.remove(guest)

    def number_of_guests_in_room(self):
        return len(self.guests_in_room)

    def add_song_to_room(self, song):
        self.songs_to_sing.append(song)

    def remove_song_from_room(self,song):
        self.songs_to_sing.remove(song)

    def number_of_songs_in_room(self):
        return len(self.songs_to_sing)

    def capacity_of_room(self):
        return self.capacity

    def can_I_add_guest_to_room(self):
        guests_that_can_enter_room = 0
        guests_that_can_enter_room += self.capacity
        guests_that_can_enter_room -= self.number_of_guests_in_room()
        if guests_that_can_enter_room >= 1:
            return True
        return False



