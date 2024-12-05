from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6.QtGui import QColor

def initUI(self):
    self.setGeometry(100, 100, 800, 600)
    self.setWindowTitle('Git и желтые окружности')

    self.button = QPushButton('Рисовать', self)
    self.button.move(50, 20)
    self.button.clicked.connect(self.paint)

    self.do_paint = False

    self.color = QColor(255, 255, 0)
