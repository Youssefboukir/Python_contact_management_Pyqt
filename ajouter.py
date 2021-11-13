from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import sqlite3
from random import *

class Ui_ajouter(object):
    def __init__(self,iduser,fname=""):
        self.iduser=iduser
        self.fname=fname
    def getphoto(self):
        self.fname, _  = QFileDialog.getOpenFileName()
        image=QPixmap(self.fname)
        self.photos.setPixmap(image)
    def InsertData(self):
        if  self.adresscont.text()=="" or  self.nomcont.text()=="" or self.prenomcont.text()=="" or self.emailcont.text()=="" or self.telcont.text()=="" :
            print("the field are empty")    
        else:
            username = self.nomcont.text()
            prenom = self.prenomcont.text()
            email = self.emailcont.text()
            telepone = self.telcont.text()
            adresse = self.adresscont.text()
            connection  = sqlite3.connect("login.db")
            n = randint(1,1000)
            connection.execute("INSERT INTO contact VALUES(?,?,?,?,?,?,?,?)",(n,self.iduser,username,prenom,email,telepone,self.fname,adresse))
            connection.commit()
            connection.close()
            self.nomcont.setText('')
            self.prenomcont.setText('')
            self.emailcont.setText('')
            self.telcont.setText('')
            self.adresscont.setText('')
    def setupUi(self, ajouter):
        ajouter.setObjectName("ajouter")
        ajouter.resize(1015, 685)
        ajouter.setStyleSheet("background:#1C8EF9 !important;")
        self.frame = QtWidgets.QFrame(ajouter)
        self.frame.setGeometry(QtCore.QRect(140, 150, 751, 431))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nomcont = QtWidgets.QLineEdit(self.frame)
        self.nomcont.setGeometry(QtCore.QRect(340, 60, 351, 31))
        self.nomcont.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.nomcont.setObjectName("nomcont")
        self.nomcont.setPlaceholderText('Name')
        self.emailcont = QtWidgets.QLineEdit(self.frame)
        self.emailcont.setGeometry(QtCore.QRect(340, 170, 351, 31))
        self.emailcont.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.emailcont.setObjectName("emailcont")
        self.emailcont.setPlaceholderText('Email')
        self.prenomcont = QtWidgets.QLineEdit(self.frame)
        self.prenomcont.setGeometry(QtCore.QRect(340, 120, 351, 31))
        self.prenomcont.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.prenomcont.setObjectName("prenomcont")
        self.prenomcont.setPlaceholderText('Last Name')
        self.telcont = QtWidgets.QLineEdit(self.frame)
        self.telcont.setGeometry(QtCore.QRect(340, 220, 351, 31))
        self.telcont.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.telcont.setObjectName("telcont")
        self.telcont.setPlaceholderText('Mobile')
        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(410, 370, 211, 31))
        self.save.setStyleSheet("background:#1C8EF9 !important;\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.save.setObjectName("save")
        self.save.clicked.connect(self.InsertData)
        self.adresscont = QtWidgets.QLineEdit(self.frame)
        self.adresscont.setGeometry(QtCore.QRect(340, 270, 351, 81))
        self.adresscont.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.adresscont.setObjectName("adresscont")
        self.adresscont.setPlaceholderText('Adresse')

        self.photos = QtWidgets.QLabel(self.frame)
        self.photos.setGeometry(QtCore.QRect(100, 120, 91, 91))
        self.photos.setStyleSheet("")
        self.photos.setText("")
        self.photos.setObjectName("photos")
        self.addphoto = QtWidgets.QPushButton(self.frame)
        self.addphoto.setGeometry(QtCore.QRect(80, 240, 131, 31))
        self.addphoto.setStyleSheet("background:#1C8EF9 !important;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.addphoto.setObjectName("addphoto")
        self.addphoto.clicked.connect(self.getphoto)
        self.label = QtWidgets.QLabel(ajouter)
        self.label.setGeometry(QtCore.QRect(390, 80, 251, 21))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.retranslateUi(ajouter)
        QtCore.QMetaObject.connectSlotsByName(ajouter)

    def retranslateUi(self, ajouter):
        _translate = QtCore.QCoreApplication.translate
        ajouter.setWindowTitle(_translate("ajouter", "Add new contact"))
        self.save.setText(_translate("ajouter", "Save"))
        self.addphoto.setText(_translate("ajouter", "Add Photo"))
        self.label.setText(_translate("ajouter", "ADD NEW CONTACT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ajouter = QtWidgets.QDialog()
    ui = Ui_ajouter()
    ui.setupUi(ajouter)
    ajouter.show()
    sys.exit(app.exec_())
