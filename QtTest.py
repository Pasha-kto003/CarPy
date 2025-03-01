import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создаем макет
        layout = QVBoxLayout()

        # Добавляем текстовую метку
        self.label = QLabel("Привет, PyQt6!", self)
        self.label.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #2E86C1;
                padding: 10px;
                background-color: #F4D03F;
                border-radius: 10px;
                border: 2px solid #2E86C1;
            }
        """)
        layout.addWidget(self.label)

        # Добавляем кнопку
        self.button = QPushButton("Нажми меня", self)
        self.button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: #2E86C1;
                padding: 10px 20px;
                border-radius: 10px;
                border: 2px solid #1B4F72;
            }
            QPushButton:hover {
                background-color: #3498DB;
            }
            QPushButton:pressed {
                background-color: #1B4F72;
            }
        """)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        # Устанавливаем макет для окна
        self.setLayout(layout)

        # Настройки окна
        self.setWindowTitle("Стилизованное окно PyQt6")
        self.setGeometry(100, 100, 300, 200)

        # Стилизация основного окна
        self.setStyleSheet("""
            QWidget {
                background-color: #F7F9F9;
            }
        """)

    def on_button_click(self):
        self.label.setText("Кнопка нажата!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())