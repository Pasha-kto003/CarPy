from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QPixmap


class CarListCardView(QWidget):
    def __init__(self, cars):
        super().__init__()

        self.setWindowTitle("Список автомобилей")
        self.resize(800, 600)

        layout = QVBoxLayout(self)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        card_container = QWidget()
        card_layout = QVBoxLayout(card_container)

        for car in cars:
            card = self.create_car_card(car)
            card_layout.addWidget(card)

        scroll_area.setWidget(card_container)
        layout.addWidget(scroll_area)

    def create_car_card(self, car):
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet("background-color: #212121; color: white; border-radius: 10px; padding: 10px;")

        layout = QHBoxLayout(card)
        image_label = QLabel()
        pixmap = QPixmap(car.image_path)
        image_label.setPixmap(pixmap.scaled(150, 150))
        image_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        info_layout = QVBoxLayout()
        info_layout.addWidget(QLabel(f"Марка: {car.mark.name}"))
        info_layout.addWidget(QLabel(f"Модель: {car.model.name}"))
        info_layout.addWidget(QLabel(f"Цена: {car.price}"))
        info_layout.addWidget(QLabel(f"Тип: {car.car_type.name}"))

        layout.addWidget(image_label)
        layout.addLayout(info_layout)

        return card
