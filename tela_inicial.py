# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

ajuste = 20

class Tela_inicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(280, 60, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 180+ajuste, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 210+ajuste, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 240+ajuste, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 150+ajuste, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_SAIR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SAIR.setGeometry(QtCore.QRect(290, 370, 80, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_SAIR.setFont(font)
        self.pushButton_SAIR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_SAIR.setObjectName("pushButton_SAIR")
        '''self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 270+ajuste, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")'''
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label_bem_vindo = QtWidgets.QLabel(self.centralwidget)
        self.label_bem_vindo.setGeometry(QtCore.QRect(210, 105, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_bem_vindo.setFont(font)
        self.label_bem_vindo.setText("")
        self.label_bem_vindo.setObjectName("label_bem_vindo")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Inicio"))
        self.pushButton.setText(_translate("MainWindow", "Vendas"))
        self.pushButton_2.setText(_translate("MainWindow", "Clientes"))
        self.pushButton_3.setText(_translate("MainWindow", "Produtos"))
        self.label_2.setText(_translate("MainWindow", "Selecione a opçao desejada:"))
        self.pushButton_SAIR.setText(_translate("MainWindow", "Sair"))
        #self.pushButton_4.setText(_translate("MainWindow", "Funcionarios"))
        #self.label_bem_vindo.setText(_translate("MainWindow", "Bem vindo, nome!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_inicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
