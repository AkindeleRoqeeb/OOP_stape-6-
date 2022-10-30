import csv

class item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: float, quality=0):
        ############### run validation to the recieve argument ######################
        # assert price >= 0
        ##################### OR ###############
        assert price >= 0, f"price {price} is not greater or equal zero"

        # assert quality >= 0
        ##################### OR ###############
        assert quality >= 0, f"quality {quality} is not greater or equal zero"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality

        # Actions to execute
        item.all.append(self)

    ############## Asign to self object ############################
    def calculate_total_price(self):
        return self.price * self.quality

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('Items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                print(item)

    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.quantity}, {self.quality})"

item.instantiate_from_csv()

##############################################################################################################################

