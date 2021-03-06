# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_designs/textfields.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self) -> None:
        self._raw_text = None
        self._processed_text = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Text Field that gets the input from user.
        self.input_text = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(20, 180, 261, 191))
        self.input_text.setObjectName("input_text")

        # move button
        self.move_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_button.setGeometry(QtCore.QRect(330, 240, 89, 25))
        self.move_button.setObjectName("move_button")
        self.move_button.clicked.connect(self._copy_text)

        # Text field that outputs to the user
        self.output_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(480, 180, 261, 191))
        self.output_text.setObjectName("output_text")

        # clears the text fields
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(330, 300, 89, 25))
        self.reset_button.setObjectName("reset_button")
        self.reset_button.clicked.connect(self._reset_field)

        # Other window objects
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.move_button.setText(_translate("MainWindow", "move"))
        self.reset_button.setText(_translate("MainWindow", "reset"))

    def _copy_text(self):
        # stores the contents of the text field into a variable
        self._raw_text = self.input_text.toPlainText()
        # call to the output function.
        self._output_text(self._raw_text)
        print(type(self._raw_text))

    def _reset_field(self):
        self.input_text.clear()
        self.output_text.clear()
        print("text fields cleared!")

    def _output_text(self, text):
        # move writing output make sure it is empty, don't append to an existing content
        self.output_text.clear()
        self.output_text.insertPlainText(text)
        print("text outputed")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
