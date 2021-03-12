from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QGridLayout
from PyQt5.QtCore import Qt, pyqtSlot


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('nice calc')
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        addButton = QPushButton('+', self)
        addButton.clicked.connect(self.add)
        grid.addWidget(addButton, 0, 1)

        subButton = QPushButton('-', self)
        subButton.clicked.connect(self.sub)
        grid.addWidget(subButton, 1, 1)

        mulButton = QPushButton('*', self)
        mulButton.clicked.connect(self.mul)
        grid.addWidget(mulButton, 2, 1)

        divButton = QPushButton('/', self)
        divButton.clicked.connect(self.div)
        grid.addWidget(divButton, 3, 1)

        self.var1 = QLineEdit(self)
        grid.addWidget(self.var1, 1, 0)
        self.var2 = QLineEdit(self)
        grid.addWidget(self.var2, 2, 0)

        self.ans = QLabel('asd', self)
        grid.addWidget(self.ans, 4, 0, 1, 2, Qt.AlignCenter)


        self.setLayout(grid)
        self.show()

    def get_arguments(self):
        a = self.var1.text()
        b = self.var2.text()
        if not(a.isdigit() and b.isdigit()):
            raise TypeError('not an integers')
        return int(a), int(b)

    @pyqtSlot()
    def add(self):
        try:
            a, b = self.get_arguments()
            self.ans.setText(str(f'{a} + {b} = {a+b}'))
        except Exception as e:
            self.ans.setText(*e.args)

    @pyqtSlot()
    def sub(self):
        try:
            a, b = self.get_arguments()
            self.ans.setText(str(f'{a} - {b} = {a-b}'))
        except Exception as e:
            self.ans.setText(*e.args)

    @pyqtSlot()
    def mul(self):
        try:
            a, b = self.get_arguments()
            self.ans.setText(str(f'{a} * {b} = {a*b}'))
        except Exception as e:
            self.ans.setText(*e.args)

    @pyqtSlot()
    def div(self):
        try:
            a, b = self.get_arguments()
            self.ans.setText(str(f'{a} / {b} = {a/b}'))
        except Exception as e:
            self.ans.setText(*e.args)
        except ZeroDivisionError as e:
            self.ans.setText('second var is 0')


if __name__ == '__main__':
    app = QApplication([])
    root = Window()
    app.exec()
