# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\User_login_signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1199, 809)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-11, -1, 1221, 201))
        self.widget.setStyleSheet("background-color:rgb(193, 193, 193)")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(-10, 200, 1221, 611))
        self.widget_2.setStyleSheet("background-color:rgb(93, 195, 245)")
        self.widget_2.setObjectName("widget_2")
        self.Philomath_header = QtWidgets.QLabel(self.widget_2)
        self.Philomath_header.setGeometry(QtCore.QRect(390, -10, 451, 161))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(70)
        self.Philomath_header.setFont(font)
        self.Philomath_header.setObjectName("Philomath_header")
        self.Philomath_header_2 = QtWidgets.QLabel(self.widget_2)
        self.Philomath_header_2.setGeometry(QtCore.QRect(540, 150, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(37)
        self.Philomath_header_2.setFont(font)
        self.Philomath_header_2.setObjectName("Philomath_header_2")
        self.Username_space = QtWidgets.QLineEdit(self.widget_2)
        self.Username_space.setGeometry(QtCore.QRect(400, 280, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Username_space.setFont(font)
        self.Username_space.setObjectName("Username_space")
        self.Philomath_header_3 = QtWidgets.QLabel(self.widget_2)
        self.Philomath_header_3.setGeometry(QtCore.QRect(250, 290, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(26)
        self.Philomath_header_3.setFont(font)
        self.Philomath_header_3.setObjectName("Philomath_header_3")
        self.Philomath_header_4 = QtWidgets.QLabel(self.widget_2)
        self.Philomath_header_4.setGeometry(QtCore.QRect(240, 390, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(26)
        self.Philomath_header_4.setFont(font)
        self.Philomath_header_4.setObjectName("Philomath_header_4")
        self.Password_space = QtWidgets.QLineEdit(self.widget_2)
        self.Password_space.setGeometry(QtCore.QRect(400, 380, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Password_space.setFont(font)
        self.Password_space.setObjectName("Password_space")
        self.login_bttn = QtWidgets.QPushButton(self.widget_2)
        self.login_bttn.setGeometry(QtCore.QRect(450, 480, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.login_bttn.setFont(font)
        self.login_bttn.setObjectName("login_bttn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Philomath_header.setText(_translate("Form", "PHILOMATH"))
        self.Philomath_header_2.setText(_translate("Form", "LOG IN"))
        self.Philomath_header_3.setText(_translate("Form", "Username"))
        self.Philomath_header_4.setText(_translate("Form", "Password"))
        self.login_bttn.setText(_translate("Form", "LOG IN "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
