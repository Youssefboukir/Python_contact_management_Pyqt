from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QApplication
from PyQt5.QtWidgets import QPushButton,QGridLayout
from PyQt5.QtGui import QPixmap
from ajouter import Ui_ajouter
import sys
import csv 
import sqlite3
from random import *
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5 import*
from sendmessage import Ui_Message
from boitereception import Ui_Dialog

class Ui_Contact(object):
    def __init__(self,iduser,name,email,idcontact="",n="",contact="",j=0,y=1,impo=""):
        self.j=j
        self.contact=contact
        self.iduser=iduser
        self.y=y
        self.name=name
        self.impo=impo
        self.email=email
        self.idcontact=idcontact
        self.n=n
        print("welcome :"+email)
        print("welcome :"+name)
        print(iduser)
    def reception(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog(self.email)
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def welcomeWindowShow(self):
        emailcontact = self.email_2.text()
        self.Message = QtWidgets.QDialog()
        self.ui = Ui_Message(self.iduser,self.name,emailcontact)
        self.ui.setupUi(self.Message)
        self.Message.show()
    def saveFileDialog(self):
        expo=[]
        connection  = sqlite3.connect("login.db")
        result = connection.execute("SELECT fname,lname,EMAIL,phone,adress FROM contact WHERE iduser = ? ",(self.iduser,))
        for i in result:
            expo.append(i)
        print(expo)

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
                        None,
                        "QFileDialog.getSaveFileName()",
                        "",
                        "All Files (*);;Python Files (*.csv)",
                        options=options)
        fieldname = ['first_name', 'last_name','Email','telephone','adress','birthday']
        path=path+".csv"
        with open(path, 'w',newline='') as csvfile:
           wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
           wr.writerow(fieldname)
           for x in expo:
                wr.writerow(x)
    def impor(self):
        self.impo=[]
        connection  = sqlite3.connect("login.db")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Python Files (*.csv)",
                        options=options)
        fil = open(path)
        reader = csv.reader(fil)
        lines= len(list(reader))
        print(lines)
        
        with open(path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                self.impo.append(row)
        i=0
        while i < len(self.impo)-1:
            n = randint(1,1000)
            connection.execute("INSERT INTO contact VALUES(?,?,?,?,?,?,?,?)",(n,self.iduser,self.impo[self.y][0],self.impo[self.y][1],self.impo[self.y][2],self.impo[self.y][3],"./projetpython/icons/8.png",self.impo[self.y][4]))
            connection.commit()
            self.y=self.y+1 
            i=i+1
        connection.close()  
    def nouvea(self):
        self.fname.setText("")
        self.lname.setText("")
        self.email_2.setText("")
        self.telephone.setText("")
        self.Adresse.setText("") 
        self.contact=[]
        self.j=0     
        self.routeur.show()
        self.continue_2.show()
    def delete(self):
        connection  = sqlite3.connect("login.db")
        connection.execute("DELETE  FROM contact WHERE id = ? ",(self.idcontact,))
        connection.commit()
        connection.close()
        self.fname.setText("")
        self.lname.setText("")
        self.email_2.setText("")
        self.telephone.setText("")
        self.Adresse.setText("") 
    def update(self):
        if self.fname.text()=="" or self.lname.text()=="" or self.email_2.text()=="" or  self.telephone.text()=="":
             print("the field are empty")    
        else:
             username = self.fname.text()
             prenom = self.lname.text()
             email = self.email_2.text()
             telepone = self.telephone.text()
             Adresse = self.Adresse.text()
             connection  = sqlite3.connect("login.db")
             cursor = connection.cursor()
             req="""Update contact set iduser=? ,fname = ? , lname = ? , EMAIL = ? , phone = ?, photo = ?,adress = ? where id =?"""
             inputData = (self.iduser,username,prenom,email,telepone,self.n,Adresse,self.idcontact)
             cursor.execute(req,inputData)
             connection.commit()
             connection.close()
    def selcrechercher(self):
        if   self.rechercher.text() =="":
             print("the field are empty")    
        else:
             self.contact=[]
             connection  = sqlite3.connect("login.db")
             result = connection.execute("SELECT * FROM contact WHERE iduser = ? ",(self.iduser,))
             self.n=""
             for data in result:
                if data[6]== self.rechercher.text() or data[5]== self.rechercher.text() or data[4]== self.rechercher.text() or data[3]== self.rechercher.text() or data[2]== self.rechercher.text():
                   self.contact.append(data)
             self.idcontact=self.contact[0][0]
             self.fname.setText(self.contact[0][2])
             self.lname.setText(self.contact[0][3])
             self.email_2.setText(self.contact[0][4])
             self.telephone.setText(self.contact[0][5])
             self.n=self.contact[0][6]
             image=QPixmap(self.n)
             self.img.setPixmap(image)
             self.Adresse.setText(self.contact[0][7])
        if(self.j==len(self.contact)-1):
           self.continue_2.hide()
        if self.j==0:
           self.routeur.hide()
        else:
              print("this contact not found")
    def adduser(self):
        self.ajouter = QtWidgets.QDialog()
        self.ui = Ui_ajouter(self.iduser)
        self.ui.setupUi(self.ajouter)
        self.ajouter.show()
    def getphoto(self):
        self.n, _  = QFileDialog.getOpenFileName()
        image=QPixmap(self.n)
        self.img.setPixmap(image)
    def select(self):
        self.contact=[]
        connection  = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM contact WHERE iduser = ? ",(self.iduser,))
        for i in result:
            self.contact.append(i)
        if not self.contact:
             print("list is empty")
        else:
             self.idcontact=self.contact[0][0]
             self.fname.setText(self.contact[0][2])
             self.lname.setText(self.contact[0][3])
             self.email_2.setText(self.contact[0][4])
             self.telephone.setText(self.contact[0][5])
             self.Adresse.setText(self.contact[0][7])
             self.n=self.contact[0][6]
             image=QPixmap(self.n)
             self.img.setPixmap(image)
        if(self.j==len(self.contact)-1):
           self.continue_2.hide()
        if self.j==0:
           self.routeur.hide()
    def continu(self): 
        layout = QVBoxLayout()
        if(self.j<len(self.contact)-1):
           self.routeur.show()
           self.j=self.j+1
           self.idcontact=self.contact[self.j][0]
           self.fname.setText(self.contact[self.j][2])
           self.lname.setText(self.contact[self.j][3])
           self.email_2.setText(self.contact[self.j][4])
           self.telephone.setText(self.contact[self.j][5])
           self.Adresse.setText(self.contact[self.j][7])
           self.n=self.contact[self.j][6]
           image=QPixmap(self.n)
           self.img.setPixmap(image)


        if(self.j==len(self.contact)-1):
           self.continue_2.hide()
    def rout(self):
        if self.j>0 :
           self.j=self.j-1
           self.idcontact=self.contact[self.j][0]
           self.fname.setText(self.contact[self.j][2])
           self.lname.setText(self.contact[self.j][3])
           self.email_2.setText(self.contact[self.j][4])
           self.telephone.setText(self.contact[self.j][5])
           self.n=self.contact[self.j][6]
           image=QPixmap(self.n)
           self.img.setPixmap(image)
           self.Adresse.setText(self.contact[self.j][7])
           self.continue_2.show()
        if self.j==0:
           self.routeur.hide()

    def setupUi(self, Contact):
        Contact.setObjectName("Contact")
        Contact.resize(1414, 724)
        Contact.setStyleSheet("background:#1C8EF9 !important;")
        self.img = QtWidgets.QLabel(Contact)
        self.img.setGeometry(QtCore.QRect(370, 310, 101, 121))
        self.img.setStyleSheet("background: rgb(0, 0, 127,80)")
        self.img.setText("")
        self.img.setObjectName("img")
        self.show = QtWidgets.QPushButton(Contact)
        self.show.setGeometry(QtCore.QRect(650, 620, 211, 31))
        self.show.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.show.setObjectName("show")
        self.show.clicked.connect(self.select)
        self.modify = QtWidgets.QPushButton(Contact)
        self.modify.setGeometry(QtCore.QRect(1060, 340, 201, 51))
        self.modify.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.modify.setObjectName("modify")
        self.modify.clicked.connect(self.update)
        self.delete_2 = QtWidgets.QPushButton(Contact)
        self.delete_2.setGeometry(QtCore.QRect(1060, 410, 201, 51))
        self.delete_2.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.delete)
        self.Add = QtWidgets.QPushButton(Contact)
        self.Add.setGeometry(QtCore.QRect(1060, 270, 201, 51))
        self.Add.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.Add.setObjectName("Add")
        self.Add.clicked.connect(self.adduser)
        self.routeur = QtWidgets.QPushButton(Contact)
        self.routeur.setGeometry(QtCore.QRect(580, 600, 61, 61))
        self.routeur.setStyleSheet("background : transparent;\n"
"background-image: url(./icons/27.png);\n"
"")
        self.routeur.setText("")
        self.routeur.setObjectName("routeur")
        self.routeur.clicked.connect(self.rout)
        self.continue_2 = QtWidgets.QPushButton(Contact)
        self.continue_2.setGeometry(QtCore.QRect(870, 600, 61, 61))
        self.continue_2.setStyleSheet("background:transparent;\n"
"background-image: url(./icons/26.png);")
        self.continue_2.setText("")
        self.continue_2.setObjectName("continue_2")
        self.continue_2.clicked.connect(self.continu)
        self.addphoto = QtWidgets.QPushButton(Contact)
        self.addphoto.setGeometry(QtCore.QRect(340, 450, 161, 31))
        self.addphoto.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.addphoto.setObjectName("addphoto")
        self.addphoto.clicked.connect(self.getphoto)
        self.rechercher = QtWidgets.QLineEdit(Contact)
        self.rechercher.setGeometry(QtCore.QRect(520, 70, 421, 31))
        self.rechercher.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.rechercher.setObjectName("rechercher")
        self.recherche = QtWidgets.QPushButton(Contact)
        self.recherche.setGeometry(QtCore.QRect(970, 50, 51, 51))
        self.recherche.setStyleSheet("background : transparent;\n"
"background-image: url(./icons/30.png);")
        self.recherche.setText("")
        self.recherche.setObjectName("recherche")
        self.recherche.clicked.connect(self.selcrechercher)
        self.nouveau = QtWidgets.QPushButton(Contact)
        self.nouveau.setGeometry(QtCore.QRect(1060, 200, 201, 51))
        self.nouveau.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.nouveau.setObjectName("nouveau")
        self.nouveau.clicked.connect(self.nouvea)
        self.exporter = QtWidgets.QPushButton(Contact)
        self.exporter.setGeometry(QtCore.QRect(1060, 480, 201, 51))
        self.exporter.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.exporter.setObjectName("exporter")
        self.exporter.clicked.connect(self.saveFileDialog)
        self.frame_2 = QtWidgets.QFrame(Contact)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 291, 751))
        self.frame_2.setStyleSheet("background:#1C8EF9 !important;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.photologin = QtWidgets.QLabel(self.frame_2)
        self.photologin.setGeometry(QtCore.QRect(90, 100, 101, 91))
        self.photologin.setStyleSheet("background:transparent;\n"
"border-radius:50px;\n"
"background-image: url(./icons/12.png);")
        self.photologin.setText("")
        self.photologin.setObjectName("photologin")
        self.nom = QtWidgets.QLabel(self.frame_2)
        self.nom.setGeometry(QtCore.QRect(50, 30, 201, 41))
        self.nom.setStyleSheet("color :white ;\n"
                "font: 75 20pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"")
        self.nom.setObjectName("nom")
        self.changepicture = QtWidgets.QPushButton(self.frame_2)
        self.changepicture.setGeometry(QtCore.QRect(60, 200, 151, 31))
        self.changepicture.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.changepicture.setObjectName("changepicture")
        self.lname = QtWidgets.QLineEdit(Contact)
        self.lname.setGeometry(QtCore.QRect(580, 270, 351, 41))
        self.lname.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.lname.setObjectName("lname_2")
        self.telephone = QtWidgets.QLineEdit(Contact)
        self.telephone.setGeometry(QtCore.QRect(580, 410, 351, 41))
        self.telephone.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.telephone.setObjectName("telephone_2")
        self.fname = QtWidgets.QLineEdit(Contact)
        self.fname.setGeometry(QtCore.QRect(580, 200, 351, 41))
        self.fname.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.fname.setObjectName("fname")
        self.email_2 = QtWidgets.QLineEdit(Contact)
        self.email_2.setGeometry(QtCore.QRect(580, 340, 351, 41))
        self.email_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.email_2.setObjectName("email_2")
        self.Adresse = QtWidgets.QLineEdit(Contact)
        self.Adresse.setGeometry(QtCore.QRect(580, 480, 351, 101))
        self.Adresse.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 246, 255);\n"
"border-radius:5px;")
        self.Adresse.setObjectName("Adresse")
        self.boitereception = QtWidgets.QPushButton(Contact)
        self.boitereception.setGeometry(QtCore.QRect(1060, 50, 211, 51))
        self.boitereception.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.boitereception.setObjectName("boitereception")
        self.boitereception.clicked.connect(self.reception)
        self.pushButton_3 = QtWidgets.QPushButton(Contact)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 10, 111, 111))
        self.pushButton_3.setStyleSheet("background: transparent;")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/22.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_3.setObjectName("pushButton_3")
        self.sendmessag = QtWidgets.QPushButton(Contact)
        self.sendmessag.setGeometry(QtCore.QRect(824, 580, 101, 23))
        self.sendmessag.setStyleSheet("background: transparent;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 10pt \"Microsoft YaHei UI\";")
        self.sendmessag.setObjectName("sendmessag")
        self.sendmessag.clicked.connect(self.welcomeWindowShow)
        self.import_2 = QtWidgets.QPushButton(Contact)
        self.import_2.setGeometry(QtCore.QRect(1060, 550, 201, 51))
        self.import_2.setStyleSheet("background:rgb(50,205,50);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.import_2.setObjectName("import_2")
        self.import_2.clicked.connect(self.impor)
        self.retranslateUi(Contact)
        QtCore.QMetaObject.connectSlotsByName(Contact)

    def retranslateUi(self, Contact):
        _translate = QtCore.QCoreApplication.translate
        Contact.setWindowTitle(_translate("Contact", "Contact"))
        self.show.setText(_translate("Contact", "Show"))
        self.modify.setText(_translate("Contact", "Modify"))
        self.delete_2.setText(_translate("Contact", "Delete"))
        self.Add.setText(_translate("Contact", "Add New Contact"))
        self.addphoto.setText(_translate("Contact", "Add New Photo"))
        self.nouveau.setText(_translate("Contact", "New"))
        self.exporter.setText(_translate("Contact", "Export"))
        self.nom.setText(_translate("Contact", self.name))
        self.changepicture.setText(_translate("Contact", "Profile"))
        self.boitereception.setText(_translate("Contact", "Boite de réception"))
        self.sendmessag.setText(_translate("Contact", "Send message ?"))
        self.import_2.setText(_translate("Contact", "Import"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Contact = QtWidgets.QDialog()
    ui = Ui_Contact()
    ui.setupUi(Contact)
    Contact.show()
    sys.exit(app.exec_())
