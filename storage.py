import json

class OrderStorage:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_order(self, order):
        with open(self.file_name, 'a') as f:
            f.write(json.dumps({
                "pizzas": [pizza.__dict__ for pizza in order.pizzas],
                "total": order.get_total()
            }) + "\n")

    def load_orders(self):
        with open(self.file_name, 'r') as f:
            return [json.loads(line) for line in f]