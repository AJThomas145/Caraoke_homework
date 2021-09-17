import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Andy", 30.00)

    def test_does_guest_have_name(self):
        self.assertEqual("Andy", self.guest.name)

    def test_does_guest_have_wallet(self):
        self.assertEqual(30.00, self.guest.wallet)
    