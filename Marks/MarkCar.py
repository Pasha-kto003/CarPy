import json


class Mark:
    def __init__(self, name):
        self.name = name
        self.models = []

    def __str__(self):
        return self.name

    def add_model(self, model):
        if model not in self.models:
            self.models.append(model)

    def to_dict(self):
        return {
            "name": self.name,
            "models": self.models
        }

    @staticmethod
    def save_to_json(mark, filename="Marks/marks.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                marks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            marks = []

        for existing_mark in marks:
            if existing_mark["name"] == mark.name:
                existing_mark["models"] = mark.models
                break
        else:
            marks.append(mark.to_dict())

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(marks, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename="Marks/marks.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return [Mark(mark["name"]) for mark in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
