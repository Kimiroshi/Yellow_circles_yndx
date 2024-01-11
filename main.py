import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from random import randint


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.initUI()

    def initUI(self):
        self.f = False
        self.size = 1
        self.x = -1
        self.y = -1
        self.btn.clicked.connect(self.start)

    def start(self):
        self.f = not self.f

    def paintEvent(self, event):
            drawer = QPainter(self)
            drawer.setPen(QPen(Qt.yellow, 8))
            drawer.setBrush(QBrush(Qt.yellow))
            if self.f:
                self.size = randint(10, 50)
                self.x = randint(1, 400)
                self.y = randint(1, 300)
                self.f = False
            drawer.drawEllipse(self.x, self.y, self.size, self.size)
            drawer.end()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())