class Bar:

    def __init__(self, input_till):
        self.till = input_till
        self.drinks_list = []

    def add_drink_to_bar(self, drink):
        self.drinks_list.append(drink)

    def number_of_drinks(self):
        return len(self.drinks_list)

    def remove_drink_from_bar(self, drink):
        self.drinks_list.remove(drink)

    def add_cash_to_till(self, drink):
        self.till += drink.price

    def sell_drink_to_guest(self, guest, drink):
        guest.pay_for_drink(drink)
        self.add_cash_to_till(drink)
        self.remove_drink_from_bar(drink)
