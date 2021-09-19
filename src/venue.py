class Venue:

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.number_of_rooms = []
        self.number_of_bars = []
        self.total_number_of_guests = 0
        self.capacity = 0
        self.total_revenue = 0

    def add_room(self, room):
        self.number_of_rooms.append(room)

    def add_room_entry_fee_to_venue_till(self, room):
        self.till += room.entry_fee

    def sell_guest_entry_to_room(self, guest, room):
        guest.pay_for_entry(room)
        self.add_room_entry_fee_to_venue_till(room)
        room.add_guest_to_room(guest)
        
    def total_number_of_rooms(self):
        return len(self.number_of_rooms)

    def add_bar(self, bar):
        self.number_of_bars.append(bar)

    def total_number_of_bars(self):
        return len(self.number_of_bars)

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

    def can_guest_enter_venue(self,  number_of_guests,room1, room2, room3):
        if (self.total_capacity(room1, room2, room3) - self.total_number_of_guests_in_venue(room1, room2, room3)) >= number_of_guests:
            return True
        return False

    def how_many_rooms_are_full_capacity(self, room1, room2, room3):
        full_rooms = 0
        if room1.can_I_add_guest_to_room() == False:
            full_rooms += 1
        if room2.can_I_add_guest_to_room() == False:
            full_rooms += 1
        if room3.can_I_add_guest_to_room() == False:
            full_rooms += 1
        return full_rooms   

    def what_is_venue_total_revenue(self, bar1):
        venue_starting_cash_float = 200.00
        bar_starting_cash_float = 100.00
        self.total_revenue += (self.till + bar1.till - venue_starting_cash_float - bar_starting_cash_float)
        

        
        

