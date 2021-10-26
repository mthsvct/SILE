# main_telas.py

# Convertemos as interfaces desenvolvidas no programa QtDesign em códigos python;
# remover a classe endereco

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from cliente import Cliente
from funcionario import Funcionario
from historico import Historico
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
from tela_apagar_funcionario import Tela_apagar_funcionario


nome_auto = "Matheus"
cpf_auto = "123"
email_auto = "123"
tel_auto = "123"
senha_auto = "123"
confirmSENHA_auto = "123"

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
        self.stack5 = QtWidgets.QMainWindow()

        # Criação do objeto para cada tela
        self.tela_login = Tela_login()
        self.tela_login.setupUi(self.stack0)

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack1)

        self.tela_cadastro_funcionario  = Tela_cadastro_funcionario()
        self.tela_cadastro_funcionario.setupUi(self.stack2)

        self.tela_produtos_menu = Tela_produtos_menu()
        self.tela_produtos_menu.setupUi(self.stack3)

        #
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        #self.QtStack.addWidget(self.stack5)



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cadastros = Registros()
        self.logado = Funcionario('','')

        self.cadastros.cadastraFUNC(nome_auto, cpf_auto, email_auto, tel_auto, senha_auto, confirmSENHA_auto)
        

        # Configuação dos botões de cada tela:
        # Funções dos botões da tela:

        # botões de voltar:
        self.tela_inicial.pushButton_SAIR.clicked.connect(self.botaoSAIR)
        self.tela_cadastro_funcionario.voltar.clicked.connect(self.abrir_tela_login)

        # Tela de Login:
        self.tela_login.pushButton.clicked.connect(self.botaoENTRAR)
        self.tela_login.pushButton_2.clicked.connect(self.abrir_tela_cadastro_pessoa)

        # Tela de cadastro de Funcionário:
        self.tela_cadastro_funcionario.cadastrar.clicked.connect(self.cadastrar_novo_FUNC)

        # Tela inicial:
        # self.tela_inicial.pushButton.clicked.connect()   # Vendas
        # self.tela_inicial.pushButton_2.clicked.connect() # Clientes
        # self.tela_inicial.pushButton_3.clicked.connect() # Produtos
        
    
    def botaoSAIR(self):
        self.usuario_logado = None
        self.usuario_logado = Funcionario('','')
        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")
        self.QtStack.setCurrentIndex(0)

    def abrir_tela_login(self):
        self.QtStack.setCurrentIndex(0)

    def abrir_tela_inicial(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_cadastro_pessoa(self):
        self.QtStack.setCurrentIndex(3)












    def botaoENTRAR(self):
        cpf = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        usuario = self.cadastros.fazerLOGIN(cpf, senha)
        if usuario[0] != None:
            self.logado = usuario[0]
            self.tela_inicial.label_bem_vindo.setText(f"Bem vindo, {usuario[0].nome}!")
            self.QtStack.setCurrentIndex(1)
        QMessageBox.information(None,'POOII',f'{usuario[1]}')
        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")
        
    def cadastrar_novo_FUNC(self):
        nome = self.tela_cadastro_funcionario.lineEdit.text()
        cpf = self.tela_cadastro_funcionario.lineEdit_2.text()
        email = self.tela_cadastro_funcionario.lineEdit_3.text()
        tel = self.tela_cadastro_funcionario.lineEdit_4.text()
        senha = self.tela_cadastro_funcionario.lineEdit_6.text()
        confirmSENHA = self.tela_cadastro_funcionario.lineEdit_7.text()

        mensagem = self.cadastros.cadastraFUNC(nome, cpf, email, tel, senha, confirmSENHA)
        QMessageBox.information(None,'POOII',f'{mensagem}')
        self.QtStack.setCurrentIndex(0)

        self.tela_cadastro_funcionario.lineEdit.setText('')
        self.tela_cadastro_funcionario.lineEdit_2.setText('')
        self.tela_cadastro_funcionario.lineEdit_3.setText('')
        self.tela_cadastro_funcionario.lineEdit_4.setText('')
        self.tela_cadastro_funcionario.lineEdit_6.setText('')
        self.tela_cadastro_funcionario.lineEdit_7.setText('')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

print("tudo certo! ")