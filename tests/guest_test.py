import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.drink import Drink

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Andy", 30.00)
        self.room = Room("One", 5.00)
        self.song = Song("One Vision")
        self.drink = Drink("Beer", 5.00)

    def test_does_guest_have_name(self):
        self.assertEqual("Andy", self.guest.name)

    def test_does_guest_have_wallet(self):
        self.assertEqual(30.00, self.guest.wallet)

    def test_pay_for_entry(self):
        self.guest.pay_for_entry(self.room)
        self.assertEqual(25.00, self.guest.wallet)

    def test_add_favourite_song_to_guest(self):
        self.guest.add_favourite_song(self.song)
        self.assertEqual("One Vision", self.guest.favourite_song[0])

    def test_does_guest_have_favourite_song(self):
        self.guest.add_favourite_song(self.song)
        self.assertEqual(1, self.guest.does_guest_have_favourite_song())

    def test_guest_pays_for_a_drink(self):
        self.guest.pay_for_drink(self.drink)
        self.assertEqual(25.00, self.guest.wallet)

        
    