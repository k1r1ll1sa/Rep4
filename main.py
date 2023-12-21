import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, \
     QLineEdit, QPushButton


def lighten(color: str, percent: int) -> str:
    # Преобразование строки в строку без символа '#'
    color = color[1:]
    # Разделение цвета на составляющие
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    # Расчет нового значения для каждой составляющей
    r += int((255 - r) * (percent / 100))
    g += int((255 - g) * (percent / 100))
    b += int((255 - b) * (percent / 100))
    # Преобразование новых значений в шестнадцатеричную строку
    new_color = f"#{r:02X}{g:02X}{b:02X}"
    return new_color


def darken(color: str, percent: int) -> str:
    # Преобразование строки в без символа '#'
    color = color[1:]
    # Разделение цвета на составляющие
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    # Расчет нового значения для каждой составляющей
    r -= int(r * (percent / 100))
    g -= int(g * (percent / 100))
    b -= int(b * (percent / 100))
    # Преобразование новых значений в шестнадцатеричную строку
    new_color = f"#{r:02X}{g:02X}{b:02X}"
    return new_color


class ColorModifier(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label_color = QLabel("Цвет:")
        self.input_color = QLineEdit()
        self.label_percent = QLabel("Процент:")
        self.input_percent = QLineEdit()
        self.btn_lighten = QPushButton("Осветлить")
        self.btn_lighten.clicked.connect(self.lighten_color)
        self.btn_darken = QPushButton("Затемнить")
        self.btn_darken.clicked.connect(self.darken_color)
        layout = QVBoxLayout()
        layout.addWidget(self.label_color)
        layout.addWidget(self.input_color)
        layout.addWidget(self.label_percent)
        layout.addWidget(self.input_percent)
        layout.addWidget(self.btn_lighten)
        layout.addWidget(self.btn_darken)
        self.setLayout(layout)

    def lighten_color(self):
        color = self.input_color.text()
        percent = int(self.input_percent.text())
        new_color = lighten(color, percent)
        self.input_color.setText(new_color)

    def darken_color(self):
        color = self.input_color.text()
        percent = int(self.input_percent.text())
        new_color = darken(color, percent)
        self.input_color.setText(new_color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorModifier()
    window.show()
    sys.exit(app.exec_())
