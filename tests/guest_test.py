import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Andy", 30.00)
        self.room = Room("One", 5.00)

    def test_does_guest_have_name(self):
        self.assertEqual("Andy", self.guest.name)

    def test_does_guest_have_wallet(self):
        self.assertEqual(30.00, self.guest.wallet)

    def test_pay_for_entry(self):
        self.guest.pay_for_entry(self.room)
        self.assertEqual(25.00, self.guest.wallet)

        
    