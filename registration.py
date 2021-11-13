from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import bcrypt
from passlib.hash import sha256_crypt
from random import *
import os
import hashlib
from login import Ui_login


class Ui_Registration(object):
    def loginShow(self):
        self.login = QtWidgets.QDialog()
        self.ui = Ui_login()
        self.ui.setupUi(self.login)
        self.login.show()
    def loginCheck(self):
        self.loginShow()
        Registration.hide()
    def InsertData(self):
        if self.password.text()!=self.password2.text() or self.name.text()=="" or self.email.text()=="":
            print("error password not matched or the fields are empty")
        else:
            username = self.name.text()
            email = self.email.text()
            password = self.password.text().encode("utf-8")
            passwd = bcrypt.hashpw(password, bcrypt.gensalt())
            connection  = sqlite3.connect("login.db")
            n = randint(1,1000)
            connection.execute("INSERT INTO USERS VALUES(?,?,?,?)",(n,username,email,passwd))
            connection.commit()
            connection.close()
            self.name.setText('')
            self.email.setText('')
            self.password.setText('')
            self.password2.setText('')
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(1409, 742)
        Registration.setStyleSheet("background:#1C8EF9 !important;")
        self.frame = QtWidgets.QFrame(Registration)
        self.frame.setGeometry(QtCore.QRect(340, 80, 731, 601))
        self.frame.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius:25px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 131, 31))
        self.label_3.setStyleSheet("background :transparent;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color : rgb(0, 0, 0)")
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(40, 260, 301, 41))
        self.name.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 251, 255);\n"
"border-radius:10px;")
        self.name.setInputMask("")
        self.name.setObjectName("name")
        self.name.setPlaceholderText('Please enter your name')
        self.password2 = QtWidgets.QLineEdit(self.frame)
        self.password2.setGeometry(QtCore.QRect(400, 390, 301, 41))
        self.password2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 251, 255);\n"
"border-radius:10px;")
        self.password2.setObjectName("password2")
        self.password2.setPlaceholderText('Please confirm your password')
        self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 131, 41))
        self.label_4.setStyleSheet("background :transparent;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color : rgb(0, 0, 0)")
        self.label_4.setObjectName("label_4")
        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(400, 260, 301, 41))
        self.email.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 251, 255);\n"
"border-radius:10px;")
        self.email.setObjectName("email")
        self.email.setPlaceholderText('Please enter your email')
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(400, 200, 131, 41))
        self.label_5.setStyleSheet("background :transparent;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color : rgb(0, 0, 0)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(400, 330, 201, 41))
        self.label_6.setStyleSheet("background :transparent;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color : rgb(0, 0, 0)")
        self.label_6.setObjectName("label_6")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(40, 390, 301, 41))
        self.password.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 251, 255);\n"
"border-radius:10px;")
        self.password.setObjectName("password")
        self.password.setPlaceholderText('Please enter your password')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.singup = QtWidgets.QPushButton(self.frame)
        self.singup.setGeometry(QtCore.QRect(40, 500, 651, 41))
        self.singup.setStyleSheet("color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"background :#1C8EF9 !important;\n"
"")
        self.singup.setObjectName("singup")
        self.singup.clicked.connect(self.InsertData)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 40, 171, 61))
        self.label.setStyleSheet("background:transparent;\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(320, 10, 101, 101))
        self.pushButton.setStyleSheet("background :#1C8EF9 !important;\n"
"border-radius:50px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/103.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(72, 72))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(310, 120, 121, 41))
        self.label_2.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(540, 550, 101, 21))
        self.label_7.setObjectName("label_7")
        self.Signin = QtWidgets.QPushButton(self.frame)
        self.Signin.setGeometry(QtCore.QRect(630, 550, 51, 20))
        self.Signin.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Signin.setObjectName("pushButton_2")
        self.Signin.clicked.connect(self.loginCheck)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Registration"))
        self.label_3.setText(_translate("Registration", "Name"))
        self.label_4.setText(_translate("Registration", "Password"))
        self.label_5.setText(_translate("Registration", "Email address"))
        self.label_6.setText(_translate("Registration", "Confirm Password"))
        self.singup.setText(_translate("Registration", "Sign up"))
        self.label.setText(_translate("Registration", "REGISTRATION"))
        self.label_2.setText(_translate("Registration", "Sign Up"))
        self.label_7.setText(_translate("Registration", "Already registered"))
        self.Signin.setText(_translate("Registration", "Sign in ?"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QDialog()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())
