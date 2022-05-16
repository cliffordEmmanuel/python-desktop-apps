# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # the button
        self.clickme = QtWidgets.QPushButton(self.centralwidget)
        self.clickme.setGeometry(QtCore.QRect(330, 340, 89, 25))
        self.clickme.setObjectName("clickme")
        self.clickme.clicked.connect(self.button_clicked)

        # the label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 160, 251, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "First QT App"))
        self.clickme.setText(_translate("MainWindow", "Clickme"))
        self.label.setText(_translate("MainWindow", "Click button to see a reaction"))

    def button_clicked(self):
        """responds to a click signal on the button by changing label text"""

        self.label.setText("You pressed the button")  # changes the label text
        self.update_label_size()  # update the size

    def update_label_size(self):
        """Adjusts the size of the label element"""
        self.label.adjustSize()
        self.label.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
