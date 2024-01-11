import sys

from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(160, 260, 75, 23))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Старт"))


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.f = False
        self.size = 1
        self.x = -1
        self.y = -1
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.btn.clicked.connect(self.start)

    def start(self):
        self.f = True

    def paintEvent(self, event):
        drawer = QPainter(self)
        if self.f:
            self.size = randint(10, 50)
            self.x = randint(1, 400)
            self.y = randint(1, 300)
            self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            self.f = False
        drawer.setPen(QPen(self.color, 8))
        drawer.setBrush(QBrush(self.color))
        drawer.drawEllipse(self.x, self.y, self.size, self.size)
        drawer.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
