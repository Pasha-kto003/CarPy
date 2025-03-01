import json

from Cars.CarModel import Car
from Marks.MarkCar import Mark
from Models.ModelCar import Model
from Types.TypesCar import Type


class WareHouse:
    FILE_PATH = "WareHouses/warehouse.json"

    def __init__(self, record_number, quantity, car):
        self.record_number = record_number
        self.quantity = quantity
        self.car = car

    def to_dict(self):
        return {
            "record_number": self.record_number,
            "quantity": self.quantity,
            "car": {
                "mark": self.car.mark.name,
                "model": self.car.model.name,
                "price": self.car.price,
                "image_path": self.car.image_path,
                "characteristics": self.car.characteristics,
                "car_type": self.car.car_type.name
            }
        }

    @staticmethod
    def load_from_json():
        try:
            with open(WareHouse.FILE_PATH, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:
                    return []
                data = json.loads(content)

            warehouses = []
            for wh in data:
                if "record_number" not in wh:
                    print(f"Ошибка: отсутствует 'record_number' в записи: {wh}")
                    continue

                car_data = wh.get("car", {})
                car_type = car_data.get("car_type", "Неизвестно")

                warehouses.append(WareHouse(
                    wh["record_number"],
                    wh.get("quantity", 0),
                    Car(
                        Mark(car_data.get("mark", "Неизвестно")),
                        Model(car_data.get("model", "Неизвестно"), car_data.get("mark", "Неизвестно")),
                        car_data.get("price", 0),
                        car_data.get("image_path", ""),
                        car_data.get("characteristics"),
                        Type(car_data.get("car_type", "Неизвестно"))
                    )
                ))

            return warehouses

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Ошибка при загрузке JSON: {e}")
            return []

    @staticmethod
    def add_to_json(entry):
        try:
            data = WareHouse.load_from_json()
            if any(wh.record_number == entry.record_number for wh in data):
                print(f"Запись с номером {entry.record_number} уже существует.")
                return

            entry.record_number = len(data) + 1
            data.append(entry)

            with open(WareHouse.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump([wh.to_dict() for wh in data], file, indent=4, ensure_ascii=False)

            print("Запись добавлена в склад!")

        except Exception as e:
            print(f"Ошибка при сохранении склада: {e}")


