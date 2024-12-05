import sys
from random import randint

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRectF, QPointF
from git_interface import initUI


class Circles_by_orange(QWidget):
    def __init__(self):
        super().__init__()
        initUI(self)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter(self)
            painter.begin(self)
            count = randint(1, 5)
            for _ in range(count):
                painter.setPen(self.color)
                radius = randint(20, 200)
                x = randint(int(10 + radius), int(800 - radius))
                y = randint(int(10 + radius), int(600 - radius))
                painter.drawEllipse(QPointF(x, y), radius, radius)
            painter.end()

        self.do_paint = False



    def paint(self):
        self.do_paint = True
        self.update()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles_by_orange()
    ex.show()
    sys.exit(app.exec())