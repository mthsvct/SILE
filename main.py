# main
import sqlite3
from cliente import Cliente
from funcionario import Funcionario
from historico import Historico
from produto import Produto
from pessoa import Pessoa
from registros import Registros
from venda import Venda

# banco = sqlite3.connect('banco.db')
registros = Registros()


# Teste1: criaçao de obejeto Pessoa().
pessoa1 = Pessoa('Maria', '000.999.222-23', 'maria@gmail.com', '99 99999-9999')


print("\n\n")


# Teste: Cadastro de um funcionário
funcionario1 = Funcionario(pessoa1, '123456789')
registros.cadastraFUNC(funcionario1)


print("\n\n")




