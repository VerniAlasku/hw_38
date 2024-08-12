class Pizza:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def get_price(self):
        return self.base_price + sum(topping.price for topping in self.toppings)

    def __str__(self):
        toppings_str = ", ".join(topping.name for topping in self.toppings)
        return f"{self.name} with {toppings_str} - ${self.get_price():.2f}"

class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price