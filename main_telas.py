# main_telas.py

# Convertemos as interfaces desenvolvidas no programa QtDesign em códigos python;
# remover a classe endereco

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from cliente import Cliente
from endereco import Endereco
from funcionario import Funcionario
from historico import Historico
from login import Login
from pessoa import Pessoa
from produto import Produto
from registros import Registros
from venda import Venda

from tela_login import Tela_login
from tela_inicial import Tela_inicial
# Menus
from tela_funcionarios_menu import Tela_funcionarios_menu
from tela_produtos_menu import Tela_produtos_menu

# Opcoes Funcionarios
from tela_cadastro_funcionario import Tela_cadastro_funcionario


class Ui_Main(QtWidgets.QWidget):
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640,480) # definição do tamanho da tela

        # Criação das pilhas de interfaces.
        self.QtStack = QtWidgets.QStackedLayout() 
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()

        # Criação do objeto para cada tela
        self.tela_login = Tela_login()
        self.tela_login.setupUi(self.stack0)

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack1)

        self.tela_funcionarios_menu = Tela_funcionarios_menu()
        self.tela_funcionarios_menu.setupUi(self.stack2)

        self.tela_produtos_menu = Tela_produtos_menu()
        self.tela_produtos_menu.setupUi(self.stack3)

        self.tela_cadastro_funcionario  = Tela_cadastro_funcionario()
        self.tela_cadastro_funcionario.setupUi(self.stack4)

        #
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

print("tudo certo! ")