import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.venue import Venue
from src.bar import Bar
from src.drink import Drink

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.venue = Venue("CodeClanCaraoke", 200.00)
        self.bar1 = Bar(100.00)
        self.bar2 = Bar(200.00)
        self.room1 = Room("One", 5.00)
        self.room2 = Room("Two", 6.00)
        self.room3 = Room("Three", 7.00)
        self.guest1 = Guest("Jon", 30.00)
        self.guest2 = Guest("Craig", 40.00)
        self.guest3 = Guest("Andy", 50.00)
        self.guest4 = Guest("John", 70.00)
        self.drink1 = Drink("Beer", 5.00)
        self.drink2 = Drink("Wine", 6.00)
        self.drink3 = Drink("Whiskey", 6.50)
        self.song1 = Song("One Vision")
        self.song2 = Song("Bohemian Rhapsody")
        self.song3 = Song("we Will Rock You")
        self.song4 = Song("Show Must Go on")


    def test_venue_has_name(self):
        self.assertEqual("CodeClanCaraoke", self.venue.name)

    def test_venue_has_a_till(self):
        self.assertEqual(200.00, self.venue.till)

    def test_add_bar_to_venue(self):
        self.venue.add_bar(self.bar1)
        self.assertEqual(1, self.venue.total_number_of_bars())

    def test_add_room_venue(self):
        self.venue.add_room(self.room1)
        self.venue.add_room(self.room2)
        self.venue.add_room(self.room3)
        self.assertEqual(3, self.venue.total_number_of_rooms())

    def test_add_room_entry_fee_to_venue_till(self):
        self.venue.add_room_entry_fee_to_venue_till(self.room1)
        self.assertEqual(205.00, self.venue.till)

    def test_sell_guest_entry_to_room(self):
        self.venue.sell_guest_entry_to_room(self.guest1, self.room1)
        self.assertEqual(205.00, self.venue.till)
        self.assertEqual(1, self.room1.number_of_guests_in_room())
        self.assertEqual(25.00, self.guest1.wallet)
    
    def test_total_capacity(self):
        self.assertEqual(15, self.venue.total_capacity(self.room1, self.room2, self.room3))

    def test_number_of_guest_in_venue(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.room2.add_guest_to_room(self.guest1)
        self.room2.add_guest_to_room(self.guest2)
        self.room3.add_guest_to_room(self.guest1)
        self.room3.add_guest_to_room(self.guest2)
        self.room3.add_guest_to_room(self.guest3)
        self.assertEqual(8, self.venue.total_number_of_guests_in_venue(self.room1, self.room2, self.room3))

    def test_can_guest_enter_venue(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.room1.add_guest_to_room(self.guest3)
        self.room1.add_guest_to_room(self.guest3)
        self.room2.add_guest_to_room(self.guest1)
        self.room2.add_guest_to_room(self.guest2)
        self.room2.add_guest_to_room(self.guest2)
        self.room2.add_guest_to_room(self.guest2)
        self.room2.add_guest_to_room(self.guest2)
        self.room3.add_guest_to_room(self.guest1)
        self.room3.add_guest_to_room(self.guest2)
        self.room3.add_guest_to_room(self.guest3)
        self.assertEqual(True, self.venue.can_guest_enter_venue(1, self.room1, self.room2, self.room3))


    def test_number_of_full_rooms(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.room1.add_guest_to_room(self.guest3)
        self.room1.add_guest_to_room(self.guest3)
        self.room2.add_guest_to_room(self.guest1)
        self.room2.add_guest_to_room(self.guest2)
        self.room2.add_guest_to_room(self.guest2)
        self.room2.add_guest_to_room(self.guest2)
        self.room2.add_guest_to_room(self.guest2)
        self.room3.add_guest_to_room(self.guest1)
        self.room3.add_guest_to_room(self.guest2)
        self.room3.add_guest_to_room(self.guest3)
        self.assertEqual(2, self.venue.how_many_rooms_are_full_capacity(self.room1, self.room2, self.room3))
        

    def test_total_revenue(self):
        self.bar1.add_drink_to_bar(self.drink1)
        self.venue.add_room(self.room1)
        self.bar1.sell_drink_to_guest(self.guest1, self.drink1)
        self.venue.sell_guest_entry_to_room(self.guest1, self.room1)
        self.venue.what_is_venue_total_revenue(self.bar1)
        self.assertEqual(10.00, self.venue.total_revenue)
        


 