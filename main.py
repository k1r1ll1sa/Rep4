import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorModifier()
    window.show()
    sys.exit(app.exec_())