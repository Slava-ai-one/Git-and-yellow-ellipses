import sys
from random import randint

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRectF
from git_interface import initUI


class Circles_by_orange(QWidget):
    def __init__(self):
        super().__init__(self)
        initUI(self)

    def draw_Event(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(self.color)
            diameter = randint(20, 400)
            x = randint(0, int(800 - diameter))
            y = randint(0, int(600 - diameter))
            form = QRectF(x, y, int((x + diameter) - 10), int((y + diameter) - 10))
            painter.drawEllipse(form)
            painter.end()

        self.do_paint = False



    def paint(self):
        self.do_paint = True
        self.update()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Weapons_base_with_grafic_interface()
    ex.show()
    sys.exit(app.exec())