import json


class Order:
    def __init__(self, order_number, order_type, warehouses):
        self.order_number = order_number  # Уникальный номер заказа
        self.order_type = order_type  # Тип заказа (покупка, продажа, утилизация)
        self.warehouses = warehouses  # Объект WareHouse

    def display_order_info(self):
        print(f"Номер заказа: {self.order_number}, Тип: {self.order_type}")
        print("Список автомобилей в заказе:")
        for idx, wh in enumerate(self.warehouses, start=1):
            print(f"{idx}. {wh.car.mark} {wh.car.model} (Количество: {wh.quantity})")

    def to_dict(self):
        return {
            "order_number": self.order_number,
            "order_type": str(self.order_type.name),
            "warehouses": [wh.to_dict() for wh in self.warehouses]
        }

    @staticmethod
    def save_to_json(order, filename="Orders/orders.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                orders = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            orders = []

        orders.append(order.to_dict())

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(orders, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename="Order/orders.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def display_all_orders(filename="Orders/orders.json"):
        orders = Order.load_from_json(filename)
        if not orders:
            print("Заказов нет.")
            return

        print("Список всех заказов:")
        for order in orders:
            print(f"Номер заказа: {order['order_number']}, Тип: {order['order_type']}")
            print("Автомобили в заказе:")
            for idx, wh in enumerate(order["warehouses"], start=1):
                print(f"{idx}. {wh['car']['mark']} {wh['car']['model']} (Количество: {wh['quantity']})")
            print("-" * 40)
