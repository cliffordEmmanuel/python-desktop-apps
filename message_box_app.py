from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys


class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 1000, 700)
        self.setWindowTitle("Trying out the message box!")

    def show_popup(self):
        """displays a message box"""

        # creating a basic message box
        msg = QMessageBox()
        msg.setWindowTitle("Message box tutorial!")
        msg.setText("This is the main text!")
        msg.setIcon(QMessageBox.Information)
        # adding buttons
        msg.setStandardButtons(
            QMessageBox.Cancel | QMessageBox.Retry | QMessageBox.Ignore
        )  # must separate buttons with "|"
        # ok it seems the ordering of the buttons varies per platform to override
        # this use the addButton() instead
        # source: https://stackoverflow.com/questions/37219153/how-to-change-the-buttons-order-in-qmessagebox
        msg.setDefaultButton(QMessageBox.Cancel)

        msg.setInformativeText("informative text, yep!")

        # a new button to show more details:
        msg.setDetailedText("details")

        # event here!
        msg.buttonClicked.connect(self.popup_clicked)
        x = msg.exec_()

    def popup_clicked(self, i):
        """determines which button is clicked.

        By returning the text for that button to the console!

        Args:
            i (_type_): a standard button.
        """
        print(i.text())


def main():
    app = QApplication(sys.argv)
    win = MyWindow()  # object of the window
    win.show()  # displays the window on the screen
    win.show_popup()

    # ensures that the application can exit.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
