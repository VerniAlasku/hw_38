from pizza import Pizza, Topping
from order import Order, CashPayment, CardPayment
from storage import OrderStorage


def main():
    # Создание пицц
    margherita = Pizza("Margherita", 8.00)
    pepperoni = Pizza("Pepperoni", 9.00)

    # Добавление топпингов
    cheese = Topping("Cheese", 1.00)
    olives = Topping("Olives", 0.50)

    margherita.add_topping(cheese)
    pepperoni.add_topping(olives)

    # Создание заказа
    order = Order()
    order.add_pizza(margherita)
    order.add_pizza(pepperoni)

    # Сохранение заказа
    storage = OrderStorage("orders.txt")
    storage.save_order(order)

    # Вывод информации
    print(order)

    # Оплата
    payment_method = CardPayment()
    print(payment_method.pay(order.get_total()))


if __name__ == "__main__":
    main()