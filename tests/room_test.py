import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("One", 5.00)
        self.guest1 = Guest("Jon", 30.00)
        self.guest2 = Guest("Craig", 40.00)
        self.guest3 = Guest("Andy", 50.00)
        self.song1 = Song("One Vision")
        self.song2 = Song("Bohemian Rhapsody")
        self.song3 = Song("we Will Rock You")

    def test_room_has_name(self):
        self.assertEqual("One", self.room.name)

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest1)
        self.assertEqual(1, self.room.number_of_guests_in_room())

    def test_remove_guest_from_room(self):
        self.room.add_guest_to_room(self.guest1)
        self.room.add_guest_to_room(self.guest2)
        self.room.add_guest_to_room(self.guest3)
        self.room.remove_guest_from_room(self.guest1)
        self.assertEqual(2, self.room.number_of_guests_in_room())

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song1)
        self.assertEqual(1, self.room.number_of_songs_in_room())

    def test_remove_song_from_room(self):
        self.room.add_song_to_room(self.song1)
        self.room.add_song_to_room(self.song2)
        self.room.remove_song_from_room(self.song1)
        self.assertEqual(1, self.room.number_of_songs_in_room())

    def test_room_capacity(self):
        self.assertEqual(5, self.room.capacity_of_room())

    def test_if_there_space_for_guest_in_room_yes(self):
        self.assertEqual(True, self.room.can_I_add_guest_to_room())

    def test_if_there_space_for_guest_in_room_false(self):
        self.room.add_guest_to_room(self.guest1)
        self.room.add_guest_to_room(self.guest2)
        self.room.add_guest_to_room(self.guest3)
        self.room.add_guest_to_room(self.guest1)
        self.room.add_guest_to_room(self.guest1)
        self.assertEqual(False, self.room.can_I_add_guest_to_room())