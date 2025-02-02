from Cars.CarModel import Car
from Marks.MarkCar import Mark
from Models.ModelCar import Model
from Characteristics.CharacteristicCars import Characteristic
from Types.TypesCar import Type
from WareHouses.WareHouse import WareHouse
from Orders.Order import Order
from OrderTypes.OrderType import OrderType


class Main:
    #region Car logic
    @staticmethod
    def create_car():
        print("\nВыберите марку автомобиля:")
        marks = Mark.load_from_json()
        if not marks:
            print("Список марок пуст! Сначала создайте марку.")
            return
        for i, mark in enumerate(marks, 1):
            print(f"{i}. {mark.name}")

        mark_choice = int(input("Введите номер марки: ")) - 1
        selected_mark = marks[mark_choice]
        print(f"\nВыбранная марка: {selected_mark.name}")
        models = [model for model in Model.load_from_json() if model.mark_name == selected_mark.name]
        if not models:
            print("У этой марки нет моделей! Сначала создайте модель.")
            return
        print("\nВыберите модель автомобиля:")
        for i, model in enumerate(models, 1):
            print(f"{i}. {model.name}")

        model_choice = int(input("Введите номер модели: ")) - 1
        selected_model = models[model_choice]
        print(f"\nВыбранная модель: {selected_model.name}")
        price = input("Введите цену: ")
        characteristics = Main.choose_characteristics()
        image_path = input("Введите путь к изображению автомобиля (например, CarImages/toyota_camry.jpg): ")
        available_types = Type.load_from_json()
        if available_types:
            print("Доступные типы автомобилей:")
            for idx, car_type in enumerate(available_types, 1):
                print(f"{idx}. {car_type.name}")

            type_index = int(input("Выберите номер типа автомобиля: ")) - 1
            car_type = available_types[type_index]
        else:
            type_name = input("Введите тип автомобиля (например, Легковой, Внедорожник, Кабриолет): ")
            car_type = Type(type_name)
            Type.save_to_json(car_type)
        car = Car(selected_mark, selected_model, price, characteristics, image_path, car_type)
        Car.save_to_json(car)
        print("Автомобиль успешно добавлен!")

    @staticmethod
    def choose_characteristics():
        characteristics = Characteristic.load_from_json()
        if not characteristics:
            print("Нет доступных характеристик. Сначала создайте характеристики.")
            return []
        print("\nВыберите характеристики для автомобиля:")
        selected_characteristics = []
        for i, characteristic in enumerate(characteristics, 1):
            print(f"{i}. {characteristic.name}")
        while True:
            choice = input("Введите номер характеристики (или '0' для завершения): ")
            if choice == "0":
                break
            try:
                index = int(choice) - 1
                if 0 <= index < len(characteristics):
                    selected_characteristics.append(characteristics[index].to_dict())
                else:
                    print("Ошибка: неверный номер характеристики!")
            except ValueError:
                print("Ошибка: введите корректный номер!")
        return selected_characteristics

    @staticmethod
    def create_mark():
        name = input("Введите название марки: ").strip()
        if name:
            Mark.save_to_json(Mark(name))
            print(f"Марка '{name}' успешно добавлена!")
        else:
            print("Ошибка: название марки не может быть пустым!")

    @staticmethod
    def create_model():
        marks = Mark.load_from_json()
        if not marks:
            print("Сначала создайте марку перед добавлением модели!")
            return
        print("\nВыберите марку для модели:")
        for i, mark in enumerate(marks, 1):
            print(f"{i}. {mark.name}")
        mark_choice = int(input("Введите номер марки: ")) - 1
        selected_mark = marks[mark_choice]
        model_name = input("Введите название модели: ").strip()
        if model_name:
            Model.save_to_json(Model(model_name, selected_mark.name))
            print(f"Модель '{model_name}' успешно добавлена в марку '{selected_mark.name}'!")
        else:
            print("Ошибка: название модели не может быть пустым!")

    @staticmethod
    def create_car_type():
        type_name = input("Введите название нового типа автомобиля (например, Легковой, Внедорожник, Кабриолет): ")
        car_type = Type(type_name)
        Type.save_to_json(car_type)
        print(f"Тип автомобиля '{type_name}' успешно добавлен!")
        return car_type

    @staticmethod
    def create_characteristic():
        name = input("Введите название характеристики: ").strip()
        meaning = input("Введите значение характеристики: ").strip()
        unit = input("Введите единицу измерения характеристики: ").strip()

        if name and meaning and unit:
            Characteristic.save_to_json(Characteristic(name, meaning, unit))
            print(f"Характеристика '{name}: {meaning} {unit}' успешно добавлена!")
        else:
            print("Ошибка: все поля должны быть заполнены!")

    @staticmethod
    def list_cars():
        cars = Car.load_from_json()
        if not cars:
            print("Список автомобилей пуст!")
            return
        print("\nСписок автомобилей:")
        for i, car in enumerate(cars, 1):
            print(f"{i}. Марка: {car.mark.name}, Модель: {car.model.name}, Цена: {car.price}")
            print(f"Тип: {car.car_type.name}")
            print(f"Изображение: {car.image_path}\n")
            if car.characteristics:
                print("   Характеристики:")
                for char in car.characteristics:
                    print(f"   - {char['name']}: {char['meaning']} {char['unit']}")
            print("-" * 40)

    #endregion

    #region Order logic
    @staticmethod
    def create_order():
        order_number = input("Введите номер заказа: ")
        order_types = OrderType.load_from_json()
        print("Доступные типы заказов:")
        for idx, order_type in enumerate(order_types, 1):
            print(f"{idx}. {order_type}")

        order_choice = int(input("Выберите тип заказа (номер): "))
        order_type = order_types[order_choice - 1]
        warehouses = WareHouse.load_from_json()
        if not warehouses:
            print("Склад пуст! Сначала добавьте автомобили на склад.")
            return

        print("Доступные автомобили на складе:")
        for idx, wh in enumerate(warehouses, 1):
            print(f"{idx}. {wh['car']['mark']} {wh['car']['model']} (Количество: {wh['quantity']})")

        car_choice = int(input("Выберите автомобиль для заказа (номер): "))
        selected_warehouse = WareHouse(
            warehouses[car_choice - 1]["record_number"],
            Car(Mark(warehouses[car_choice - 1]["car"]["mark"]),
                Model(warehouses[car_choice - 1]["car"]["model"], warehouses[car_choice - 1]["car"]["mark"]),
                warehouses[car_choice - 1]["car"]["price"],
                warehouses[car_choice - 1]["car"]["image_path"], None), warehouses[car_choice - 1]["quantity"]
        )

        order = Order(order_number, order_type, selected_warehouse)
        Order.save_to_json(order)
        print(f"Заказ #{order_number} успешно добавлен!")

    @staticmethod
    def create_warehouse_entry():
        cars = Car.load_from_json()
        if not cars:
            print("Нет доступных автомобилей.")
            return

        print("Выберите автомобиль для добавления в склад:")
        for idx, car in enumerate(cars, start=1):
            print(f"{idx}. {car.mark.name} {car.model.name} {car.car_type.name} (Цена: {car.price})")

        car_choice = int(input("Введите номер автомобиля: ")) - 1
        if 0 <= car_choice < len(cars):
            selected_car = cars[car_choice]
            quantity = int(input("Введите количество: "))

            if not selected_car.car_type:
                print("Ошибка: car_type отсутствует у выбранного автомобиля!")
                return

            selected_car = cars[car_choice]
            warehouse_entry = WareHouse(
                len(WareHouse.load_from_json()) + 1,
                quantity,
                Car(
                    selected_car.mark,
                    selected_car.model,
                    selected_car.price,
                    selected_car.characteristics,
                    selected_car.image_path,
                    selected_car.car_type
                )
            )

            WareHouse.add_to_json(warehouse_entry)
            print("Запись добавлена в склад!")
        else:
            print("Некорректный выбор.")

    @staticmethod
    def create_order_type():
        new_type = input("Введите новый тип заказа: ").strip()
        if new_type:
            OrderType.add_new_order_type(new_type)
        else:
            print("Ошибка: тип заказа не может быть пустым!")

    @staticmethod
    def list_all_order_types():
        types = OrderType.load_from_json()
        if not types:
            print("Нет доступных типов заказов.")
            return

        print("Список типов заказов:")
        for i, order_type in enumerate(types, 1):
            print(f"{i}. {order_type.name}")

    @staticmethod
    def menu():
        while True:
            print("\nМеню:")
            print("1. Добавить автомобиль")
            print("2. Добавить марку")
            print("3. Добавить модель")
            print("4. Добавить характеристику")
            print("5. Показать все автомобили")
            print('6. Добавить тип кузова авто')
            print('7. Добавить накладную')
            print('8. Добавить запись на накладную')
            print("9. Добавить тип накладной")
            print("10. Вывести все типы накладных")
            print("11. Выйти")

            choice = input("Выберите действие: ")

            if choice == "1":
                Main.create_car()
            elif choice == "2":
                Main.create_mark()
            elif choice == "3":
                Main.create_model()
            elif choice == "4":
                Main.create_characteristic()
            elif choice == "5":
                Main.list_cars()
            elif choice == "6":
                Main.create_car_type()
            elif choice == "7":
                Main.create_order()
            elif choice == "8":
                Main.create_warehouse_entry()
            elif choice == "9":
                Main.create_order_type()
            elif choice == "10":
                Main.list_all_order_types()
            elif choice == "11":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    Main.menu()
