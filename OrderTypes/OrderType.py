import json
import os


class OrderType:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

    @staticmethod
    def save_to_json(types, filename="OrderTypes/order_types.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([t.to_dict() if isinstance(t, OrderType) else {"name": t} for t in types],
                      file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename="OrderTypes/order_types.json"):
        if not os.path.exists(filename):
            return []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return [OrderType(d["name"]) if isinstance(d, dict) and "name" in d else OrderType(d)
                            for d in data]
                else:
                    return []
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def add_new_order_type(order_type, filename="OrderTypes/order_types.json"):
        types = OrderType.load_from_json(filename)
        types.append(order_type if isinstance(order_type, OrderType) else OrderType(order_type))
        OrderType.save_to_json(types, filename)
