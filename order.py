class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class CashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} in cash."

class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card."

class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        return sum(pizza.get_price() for pizza in self.pizzas)

    def __str__(self):
        return "\n".join(str(pizza) for pizza in self.pizzas)