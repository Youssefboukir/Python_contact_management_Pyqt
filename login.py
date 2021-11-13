from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import bcrypt
from passlib.hash import sha256_crypt
from random import *
from contacts import Ui_Contact

class Ui_login(object):
    def signUpShow(self):
        self.Registration =QtWidgets.QDialog()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.Registration)
        self.Registration.show()
    def signUpCheck(self):
        self.signUpShow()
        login.hide()
    def welcomeWindowShow(self,iduser,name,email):
        self.Contact = QtWidgets.QDialog()
        self.ui = Ui_Contact(iduser,name,email)
        self.ui.setupUi(self.Contact)
        self.Contact.show()
    def loginCheck(self):
        email = self.name.text()
        passwd = self.password.text().encode("utf-8")
        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS ")
        for data in result:
            if  data[2]==email and bcrypt.checkpw(passwd, data[3]):
               iduser=data[0]
               name=data[1]
               email=data[2]
               self.welcomeWindowShow(iduser,name,email)      
        else:
            print("User Not Found !")
            self.name.setText("")
            self.password.setText("")
        connection.close()
        
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1411, 746)
        login.setStyleSheet("background:#1C8EF9 !important;")
        self.frame = QtWidgets.QFrame(login)
        self.frame.setGeometry(QtCore.QRect(490, 110, 411, 521))
        self.frame.setStyleSheet("background:rgb(255, 255, 255);\n"
       "border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(50, 260, 311, 31))
        self.name.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 251, 255);\n"
"border-radius:5px;")
        self.name.setInputMask("")
        self.name.setText("")
        self.name.setObjectName("name")
        self.name.setPlaceholderText('Please enter your email')
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(50, 360, 311, 31))
        self.password.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 251, 255);\n"
"border-radius:5px;")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setObjectName("password")
        self.password.setPlaceholderText('Please enter your password')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login2 = QtWidgets.QPushButton(self.frame)
        self.login2.setGeometry(QtCore.QRect(50, 440, 311, 41))
        self.login2.setStyleSheet("color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"background :#1C8EF9 !important;\n"
"")
        self.login2.setObjectName("login2")
        self.login2.clicked.connect(self.loginCheck)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 220, 111, 20))
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(60, 320, 121, 21))
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 140, 101, 41))
        self.label.setStyleSheet("background : transparent;\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 20, 101, 101))
        self.pushButton.setStyleSheet("background:#1C8EF9 !important;\n"
"border-radius:50px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/103.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(72, 72))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(50, 400, 16, 17))
        self.checkBox.setStyleSheet("border-radius:100px;")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 400, 91, 16))
        self.label_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.singup = QtWidgets.QPushButton(self.frame)
        self.singup.setGeometry(QtCore.QRect(290, 490, 75, 21))
        self.singup.setStyleSheet("color :#1C8EF9 !important;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.singup.setObjectName("pushButton_2")
        self.singup.clicked.connect(self.signUpCheck)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "login"))
        self.login2.setText(_translate("login", "Login"))
        self.label_4.setText(_translate("login", "Email address"))
        self.label_5.setText(_translate("login", "Password"))
        self.label.setText(_translate("login", "Sign In"))
        self.label_6.setText(_translate("login", "Remember me"))
        self.singup.setText(_translate("login", "Sign Up ?"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
