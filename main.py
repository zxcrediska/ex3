import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from Ui import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn.clicked.connect(self.draw)

        self.go_draw = False

    def draw(self):
        self.go_draw = True
        self.update()

    def paintEvent(self, event):
        if self.go_draw:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def drawCircle(self, qp):
        qp.setBrush(QColor(255, 204, 0))
        hw = randint(10, 200)  # diameter
        qp.drawEllipse(150 - hw // 2, 200 - hw // 2, hw, hw)  # x, y, w, h


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())
