import unittest
from src.bar import Bar
from src.guest import Guest
from src.drink import Drink

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar(100.00)
        self.drink1 = Drink("Beer", 5.00)
        self.drink2 = Drink("Wine", 6.00)
        self.drink3 = Drink("Whiskey", 6.50)
        self.guest1 = Guest("Jon", 25.00)
        self.guest2 = Guest("Craig", 40.00)
        self.guest3 = Guest("Andy", 50.00)

    def test_bar_has_till(self):
        self.assertEqual(100.00, self.bar.till)

    def test_add_drink_to_bar(self):
        self.bar.add_drink_to_bar(self.drink1)
        self.bar.add_drink_to_bar(self.drink2)
        self.assertEqual(2, self.bar.number_of_drinks())


    def test_remove_drink_from_bar(self):
        self.bar.add_drink_to_bar(self.drink1)
        self.bar.add_drink_to_bar(self.drink2)
        self.bar.remove_drink_from_bar(self.drink1)
        self.assertEqual(1, self.bar.number_of_drinks())


    def test_add_cash_to_till(self):
         self.bar.add_cash_to_till(self.drink3)
         self.assertEqual(106.50, self.bar.till)

    def test_sell_drink_to_guest(self):
        self.bar.add_drink_to_bar(self.drink1)
        self.bar.sell_drink_to_guest(self.guest1, self.drink1)
        self.assertEqual(20, self.guest1.wallet)
        self.assertEqual(105, self.bar.till)
        self.assertEqual(0, self.bar.number_of_drinks())



  