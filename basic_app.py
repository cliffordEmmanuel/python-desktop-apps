from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def clicked():
    """This will be called when a button is clicked!!"""
    print("Clicked")


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 1000, 700)
    win.setWindowTitle("First Desktop App")

    label = QtWidgets.QLabel(win)
    label.setText("My First Label")
    label.move(50, 50)

    #  a button here!
    b1 = QtWidgets.QPushButton(win)
    b1.setText("click me!")
    b1.move(100, 100)

    # call the click function when the button is clicked!!
    b1.clicked.connect(clicked)

    win.show()

    # ensures that the application can exit.
    sys.exit(app.exec_())


window()
