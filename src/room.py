class Room:

    def __init__(self, input_name,input_entry_fee):
        self.name = input_name
        self.entry_fee = input_entry_fee
        self.guests_in_room = []
        self.capacity = 5
        self.songs_to_sing = []
        self.revenue = 0


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
        self.capacity -= self.number_of_guests_in_room()
        if self.capacity >= 1:
            return True
        return False

    def is_favourite_song_available(self, guest):
        for song in self.songs_to_sing:
            if song.name == guest.favourite_song[0]: 
                return "Whoo"
            if song.name != guest.favourite_song[0]:
                return "Sorry, favourite song is unavailable"

    def total_room_revenue(self):
        self.revenue += self.number_of_guests_in_room() * self.entry_fee
         

        
        



