import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song#
from src.venue import Venue

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.venue = Venue("CodeClanCaraoke", 100.00)
        self.room1 = Room("One", 5.00)
        self.room2 = Room("Two", 6.00)
        self.room3 = Room("Three", 7.00)
        self.guest1 = Guest("Jon", 30.00)
        self.guest2 = Guest("Craig", 40.00)
        self.guest3 = Guest("Andy", 50.00)
        self.song1 = Song("One Vision")
        self.song2 = Song("Bohemian Rhapsody")
        self.song3 = Song("we Will Rock You")
        self.song4 = Song("Show Must Go on")

    def test_venue_has_name(self):
        self.assertEqual("CodeClanCaraoke", self.venue.name)

    def test_venue_has_a_till(self):
        self.assertEqual(100.00, self.venue.till)

    # def test_total_capacity(self):

    # def test_number_of_guest_in_venue(self):

    # def test_number_rooms(self):

    # def test_number_of_full_rooms(self):

    # def test_total_revenue(self):


    # def number_of_rooms(self):


