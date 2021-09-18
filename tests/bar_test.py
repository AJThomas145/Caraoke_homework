import unittest
from src.bar import Bar
from src.guest import Guest

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar(100.00)
        # self.drink1 = 

    def test_bar_has_till(self):
        self.assertEqual(100.00, self.bar.till)

    def test_add_drink_to_bar(self, drink):

    def test_remove_drink_from_bar(self, drink):

    def test_number_of_drinks(self):

    def test_add_cash_to_till(self, drink):

    def sell_drink_to_guest(self, guest, drink):


  