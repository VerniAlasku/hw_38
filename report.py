from storage import OrderStorage


def generate_report(file_name):
    storage = OrderStorage(file_name)
    orders = storage.load_orders()

    total_pizzas = sum(len(order['pizzas']) for order in orders)
    total_revenue = sum(order['total'] for order in orders)

    print(f"Total Pizzas Sold: {total_pizzas}")
    print(f"Total Revenue: ${total_revenue:.2f}")


if __name__ == "__main__":
    generate_report("orders.txt")