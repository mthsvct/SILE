# main
import sqlite3
from cliente import Cliente
from funcionario import Funcionario
from historico import Historico
from produto import Produto
from registros import Registros
from venda import Venda

banco = sqlite3.connect('banco.db')

funcionarios = []
clientes = []
vendas = []
registros = Registros()

def menu_principal():
	print('-' * 50)
	print('MENU PRINCIPAL: ')
	print('-' * 50)
	print('1 - Entrar area funcionario')
	print('0 - Sair')
	print('\nSelecione: ', end='')
	return ''



def menu_sel():
	op = int(input(menu_principal()))
	if op == 1:
		pass
	elif op == 0:
		pass
	else:
		print()
		menu_sel()
		pass


print()
menu_sel()