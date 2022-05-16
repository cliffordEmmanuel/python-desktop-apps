from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    """Defines a window class

    Args:
        QMainWindow (_type_): inherits from the base QMainWindow object
    """

    def __init__(self) -> None:
        super(MyWindow, self).__init__()
        self.initUI()

    def button_clicked(self):
        """responds to a click signal on the button by changing label text"""

        self.label.setText("you pressed the button")  # changes the label text
        self.update_label_size()  # update the size

    def initUI(self):
        self.setGeometry(200, 200, 1000, 700)
        self.setWindowTitle("App with OOP implementation")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!!")
        self.b1.clicked.connect(self.button_clicked)  # responds to the click event on the button

    def update_label_size(self):
        """Adjusts the size of the label element"""
        self.label.adjustSize()


def main():
    app = QApplication(sys.argv)
    win = MyWindow()  # object of the window
    win.show()  # displays the window on the screen

    # ensures that the application can exit.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
