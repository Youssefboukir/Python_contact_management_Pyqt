

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ajouter(object):
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
"background-color:rgb(242, 250, 255);\n"
"border-radius:5px;")
        self.nomcont.setObjectName("nomcont")
        self.emailcont = QtWidgets.QLineEdit(self.frame)
        self.emailcont.setGeometry(QtCore.QRect(340, 170, 351, 31))
        self.emailcont.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 250, 255);\n"
"border-radius:5px;")
        self.emailcont.setObjectName("emailcont")
        self.prenomcont = QtWidgets.QLineEdit(self.frame)
        self.prenomcont.setGeometry(QtCore.QRect(340, 120, 351, 31))
        self.prenomcont.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 250, 255);\n"
"border-radius:5px;")
        self.prenomcont.setObjectName("prenomcont")
        self.telcont = QtWidgets.QLineEdit(self.frame)
        self.telcont.setGeometry(QtCore.QRect(340, 220, 351, 31))
        self.telcont.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 250, 255);\n"
"border-radius:5px;")
        self.telcont.setObjectName("telcont")
        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(120, 380, 211, 31))
        self.save.setStyleSheet("background:#1C8EF9 !important;\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.save.setObjectName("save")
        self.emailcont_2 = QtWidgets.QLineEdit(self.frame)
        self.emailcont_2.setGeometry(QtCore.QRect(340, 270, 351, 81))
        self.emailcont_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border : 1px solid;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(242, 250, 255);\n"
"border-radius:5px;")
        self.emailcont_2.setObjectName("emailcont_2")
        self.photos = QtWidgets.QLabel(self.frame)
        self.photos.setGeometry(QtCore.QRect(90, 110, 111, 101))
        self.photos.setStyleSheet("background-color: rgb(0, 85, 255,100);")
        self.photos.setText("")
        self.photos.setObjectName("photos")
        self.addphoto = QtWidgets.QPushButton(self.frame)
        self.addphoto.setGeometry(QtCore.QRect(80, 240, 131, 31))
        self.addphoto.setStyleSheet("background:#1C8EF9 !important;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.addphoto.setObjectName("addphoto")
        self.update = QtWidgets.QPushButton(self.frame)
        self.update.setGeometry(QtCore.QRect(440, 380, 211, 31))
        self.update.setStyleSheet("background:#1C8EF9 !important;\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"\n"
"")
        self.update.setObjectName("update")
        self.label = QtWidgets.QLabel(ajouter)
        self.label.setGeometry(QtCore.QRect(470, 80, 81, 21))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.retranslateUi(ajouter)
        QtCore.QMetaObject.connectSlotsByName(ajouter)

    def retranslateUi(self, ajouter):
        _translate = QtCore.QCoreApplication.translate
        ajouter.setWindowTitle(_translate("ajouter", "Profile"))
        self.save.setText(_translate("ajouter", "Save"))
        self.addphoto.setText(_translate("ajouter", "Add Photo"))
        self.update.setText(_translate("ajouter", "Update"))
        self.label.setText(_translate("ajouter", "Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ajouter = QtWidgets.QDialog()
    ui = Ui_ajouter()
    ui.setupUi(ajouter)
    ajouter.show()
    sys.exit(app.exec_())
