import json


class Order:
    def __init__(self, order_number, order_type, warehouse):
        self.order_number = order_number  # Уникальный номер заказа
        self.order_type = order_type  # Тип заказа (покупка, продажа, утилизация)
        self.warehouse = warehouse  # Объект WareHouse

    def to_dict(self):
        return {
            "order_number": self.order_number,
            "order_type": self.order_type,
            "warehouse": self.warehouse.to_dict()
        }

    @staticmethod
    def save_to_json(order, filename="Order/orders.json"):
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
