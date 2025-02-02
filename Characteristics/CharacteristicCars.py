import json


class Characteristic:
    def __init__(self, name, meaning, unit):
        self.name = name
        self.meaning = meaning
        self.unit = unit

    def to_dict(self):
        return {"name": self.name, "meaning": self.meaning, "unit": self.unit}

    @staticmethod
    def save_to_json(characteristic, filename="Characteristics/characteristics.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                characteristics = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            characteristics = []
        if characteristic.name not in [c["name"] for c in characteristics]:
            characteristics.append(characteristic.to_dict())
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(characteristics, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename="Characteristics/characteristics.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Characteristic(c["name"], c["meaning"], c["unit"]) for c in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
