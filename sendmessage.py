from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import sqlite3
from random import *


class Ui_Message(object):
    def __init__(self,iduser,emailcontact,name):
        self.iduser=iduser
        self.name=name
        self.emailcontact=emailcontact
    def InsertData(self):
        if  self.msg.toPlainText() == "" :
            print("the field are empty")    
        else:
            msg = self.msg.toPlainText() 
            connection  = sqlite3.connect("login.db")
            n = randint(1,1000)
            connection.execute("INSERT INTO Message VALUES(?,?,?,?)",(self.iduser,self.emailcontact,self.name,msg))
            connection.commit()
            connection.close()
            self.msg.setPlainText("")
    def setupUi(self, Message):
        Message.setObjectName("Message")
        Message.resize(553, 400)
        Message.setStyleSheet("background:#1C8EF9 !important;")
        self.send = QtWidgets.QPushButton(Message)
        self.send.setGeometry(QtCore.QRect(380, 350, 141, 31))
        self.send.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.send.setObjectName("send")
        self.send.clicked.connect(self.InsertData)
        self.msg = QtWidgets.QPlainTextEdit(Message)
        self.msg.setGeometry(QtCore.QRect(33, 30, 481, 301))
        self.msg.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.msg.setObjectName("plainTextEdit")

        self.retranslateUi(Message)
        QtCore.QMetaObject.connectSlotsByName(Message)

    def retranslateUi(self, Message):
        _translate = QtCore.QCoreApplication.translate
        Message.setWindowTitle(_translate("Message", "Message"))
        self.send.setText(_translate("Message", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Message = QtWidgets.QDialog()
    ui = Ui_Message()
    ui.setupUi(Message)
    Message.show()
    sys.exit(app.exec_())
