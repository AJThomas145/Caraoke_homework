class Guest:

    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = []

    def pay_for_entry(self, room):
        self.wallet -= room.entry_fee

    def add_favourite_song(self, song):
        self.favourite_song.append(song.name)

    def does_guest_have_favourite_song(self):
        return len(self.favourite_song)

    def pay_for_drink(self, drink):
        self.wallet -= drink.price

