# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_whatsDirect(object):
    def setupUi(self, whatsDirect):
        whatsDirect.setObjectName("whatsDirect")
        whatsDirect.resize(457, 365)
        whatsDirect.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(186, 189, 182);")
        self.StartButton = QtWidgets.QPushButton(whatsDirect)
        self.StartButton.setGeometry(QtCore.QRect(260, 230, 151, 25))
        self.StartButton.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.StartButton.setObjectName("StartButton")
        self.CancelButton = QtWidgets.QPushButton(whatsDirect)
        self.CancelButton.setGeometry(QtCore.QRect(58, 230, 151, 25))
        self.CancelButton.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Ubuntu Condensed\";")
        self.CancelButton.setObjectName("CancelButton")
        self.ExcelSheetName = QtWidgets.QLineEdit(whatsDirect)
        self.ExcelSheetName.setGeometry(QtCore.QRect(250, 90, 181, 25))
        self.ExcelSheetName.setText("")
        self.ExcelSheetName.setObjectName("ExcelSheetName")
        self.label = QtWidgets.QLabel(whatsDirect)
        self.label.setGeometry(QtCore.QRect(40, 90, 201, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(whatsDirect)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 201, 17))
        self.label_2.setObjectName("label_2")
        self.quizzNo = QtWidgets.QLineEdit(whatsDirect)
        self.quizzNo.setGeometry(QtCore.QRect(250, 140, 181, 25))
        self.quizzNo.setText("")
        self.quizzNo.setObjectName("quizzNo")

        self.retranslateUi(whatsDirect)
        QtCore.QMetaObject.connectSlotsByName(whatsDirect)

    def retranslateUi(self, whatsDirect):
        _translate = QtCore.QCoreApplication.translate
        whatsDirect.setWindowTitle(_translate("whatsDirect", "whatsapp"))
        self.StartButton.setText(_translate("whatsDirect", "Start"))
        self.CancelButton.setText(_translate("whatsDirect", "Cancel"))
        self.label.setText(_translate("whatsDirect", "Enter Your excel sheet Name"))
        self.label_2.setText(_translate("whatsDirect", "Enter your quiz No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    whatsDirect = QtWidgets.QDialog()
    ui = Ui_whatsDirect()
    ui.setupUi(whatsDirect)
    whatsDirect.show()
    sys.exit(app.exec_())
