import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from Cars.CarModel import Car
from QtCar.CarListForm import CarListCardView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление автомобилями")
        self.setGeometry(100, 100, 800, 600)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной макет
        layout = QVBoxLayout()

        # Кнопки
        btn_add_car = QPushButton("Добавить автомобиль")
        self.car_list_button = QPushButton("Список автомобилей")

        # Добавление кнопок в макет
        layout.addWidget(self.car_list_button)
        layout.addWidget(btn_add_car)

        # Установка выравнивания и макета
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        central_widget.setLayout(layout)

        # Стили
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
                color: #F5F5F5;
            }

            QPushButton {
                background-color: #FF0000;
                color: #FFFFFF;
                border: none;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #B22222;
            }

            QLabel {
                color: #F5F5F5;
                font-size: 14px;
            }

            QLineEdit, QTextEdit {
                background-color: #1c1c1c;
                color: #F5F5F5;
                border: 1px solid #FF0000;
                padding: 5px;
                border-radius: 3px;
            }
        """)

        # Связывание кнопок с действиями
        btn_add_car.clicked.connect(self.add_car)
        self.car_list_button.clicked.connect(self.show_car_list_form)

    def add_car(self):
        # Здесь можно добавить логику для добавления автомобиля
        QMessageBox.information(self, "Добавить автомобиль", "Добавление автомобиля")

    def show_car_list_form(self):
        # Показ формы списка автомобилей
        self.car_list_form = CarListCardView(Car.load_from_json())
        self.car_list_form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
