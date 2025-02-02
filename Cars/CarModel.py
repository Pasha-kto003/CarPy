import json
from Marks.MarkCar import Mark
from Models.ModelCar import Model
from Types.TypesCar import Type


class Car:
    def __init__(self, mark, model, price, characteristics, image_path, car_type):
        self.mark = mark
        self.model = model
        self.price = price
        self.characteristics = characteristics
        self.image_path = image_path
        self.car_type = car_type

    def to_dict(self):
        return {
            "mark": self.mark.name,
            "model": self.model.name,
            "price": self.price,
            "characteristics": self.characteristics,
            "image_path": self.image_path,
            "car_type": self.car_type
        }

    @staticmethod
    def save_to_json(car, filename="Cars/cars.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                cars = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            cars = []

        cars.append(car.to_dict())

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(cars, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename="Cars/cars.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            return [
                Car(
                    Mark(car["mark"]),
                    Model(car["model"], car["mark"]),
                    car["price"],
                    car["characteristics"],
                    car["image_path"],
                    Type(car["car_type"]) if "car_type" in car else None  # ✅ Теперь car_type не будет None
                )
                for car in data
            ]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Ошибка при загрузке JSON: {e}")
            return []

