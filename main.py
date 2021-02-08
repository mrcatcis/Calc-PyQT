from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QGridLayout
from PyQt5.QtCore import Qt, pyqtSlot


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('nice calc')
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.addButton = QPushButton('+', self)
        self.addButton.clicked.connect(self.add)
        grid.addWidget(self.addButton, 0, 1)

        self.subButton = QPushButton('-', self)
        self.subButton.clicked.connect(self.sub)
        grid.addWidget(self.subButton, 1, 1)

        self.mulButton = QPushButton('*', self)
        self.mulButton.clicked.connect(self.mul)
        grid.addWidget(self.mulButton, 2, 1)

        self.divButton = QPushButton('/', self)
        self.divButton.clicked.connect(self.div)
        grid.addWidget(self.divButton, 3, 1)

        self.var1 = QLineEdit(self)
        grid.addWidget(self.var1, 1, 0)
        self.var2 = QLineEdit(self)
        grid.addWidget(self.var2, 2, 0)

        self.show()

    @pyqtSlot()
    def add(self):
        pass

    @pyqtSlot()
    def sub(self):
        pass

    @pyqtSlot()
    def mul(self):
        pass

    @pyqtSlot()
    def div(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    root = Window()
    app.exec()
