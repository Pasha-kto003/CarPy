import json


class Model:
    def __init__(self, name, mark_name):
        self.name = name
        self.mark_name = mark_name

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "mark_name": self.mark_name
        }

    @staticmethod
    def save_to_json(model, filename="Models/models.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                models = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            models = []

        models.append(model.to_dict())

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(models, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename="Models/models.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return [Model(model["name"], model["mark_name"]) for model in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
