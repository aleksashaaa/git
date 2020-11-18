import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.do)
        self.t = False

    def do(self):
        self.t = True
        self.n = random.randint(0, 300)

    def paintEvent(self, event):
        if self.t:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(0, 0, self.n, self.n)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())