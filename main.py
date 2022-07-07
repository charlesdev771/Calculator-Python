import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculator(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Chameleon Calculator')
        self.setFixedSize(500, 500)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet('* {background: white; color: #000; font-size: 30px;}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


        self.add_btn(QPushButton('7'), 1, 0, 1,1)

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        btn.clicked.connect(
            lambda: self.display.setText(
                self.display.text() + btn.text()
            )
        )
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec()
