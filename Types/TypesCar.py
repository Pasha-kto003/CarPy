import json


class Type:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

    @staticmethod
    def save_to_json(car_type, filename="Types/types.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                types = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            types = []

        if car_type.to_dict() not in types:
            types.append(car_type.to_dict())
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(types, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename="Types/types.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Type(item["name"]) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
