import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorModifier()
    window.show()
    sys.exit(app.exec_())