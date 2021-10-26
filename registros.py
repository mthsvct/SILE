from pessoa import Pessoa
from cliente import Cliente
from funcionario import Funcionario

class Registros():

	__slots__ = ['_vendas', '_clientes', '_produtos', '_funcionarios']

	def __init__(self):
		self._vendas = []
		self._clientes = []
		self._produtos = []
		self._funcionarios = []

	@property
	def vendas(self):
		return self._vendas

	@property
	def clientes(self):
		return self._clientes

	@property
	def produtos(self):
		return self._produtos

	@property
	def funcionarios(self):
		return self._funcionarios

	# ----------------------------------- #

	def cadastraVENDA(self, venda):
		self.vendas.append(venda)


	def buscaVENDA(self, cpf, produto):
		encontrado = None
		for i in self.vendas:
			if( i.cliente.cpf == cpf and i.produto.nome == produto.nome and encontrado == None ):
				encontrado = i
		return encontrado

	# ----------------------------------- #
	# Função que busca um funcionário na lista de funcionários.
	def buscaFUNC(self, cpf):
		encontrado = None
		for i in self.funcionarios:
			if( i.cpf == cpf ):
				encontrado = i
		return encontrado

	# Função que cadastra um novo funcionário.
	def cadastraFUNC(self, nome, cpf, email, tel, senha, confirmSENHA):
		if '' in [nome, cpf, email, tel, senha, confirmSENHA]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			if self.buscaFUNC(cpf) != None:
				# Existe um funcionario com esse mesmo CPF
				mensagem = "O CPF informado já foi cadastrado!"
			else:
				if senha != confirmSENHA:
					# A senha e a confirmação da senha foram digitadas corretamente.
					mensagem = "Erro na confirmacao de senha!"
				else:
					pessoa = Pessoa(nome, cpf, email, tel)
					funcionario = Funcionario(pessoa, senha)
					self.funcionarios.append(funcionario)
					mensagem = "Cadastro de funcionário realizado com sucesso!"
		return mensagem


	# Retorna uma lista contendo:
		# Retorna o usuário caso seja digitado os dados corretamente, caso contrário retorna retorna None;
		# Junto com o usuário ou None é retornado uma mensagem.
	def fazerLOGIN(self, cpf, senha):

		logado = []

		if cpf != '' and senha != '':
			# todos os campos foram preenchidos
			usuario = self.buscaFUNC(cpf) # busca o usuário na lista de funcionarios cadastrados.

			if(usuario != None):
                # Funcionário existe!
				if(senha == usuario.senha):
					mensagem = ("Bem vindo, "+usuario.nome+"!")
					logado.append(usuario)
                	# logado.append(mensagem)
				else:
					# A senha não existe.
					mensagem = "Senha incorreta!"
			else:
				# O funcionário não existe.
				mensagem = "Conta nao encontrada. \nPor favor, efetue o cadastro antes do login."
		else:
			mensagem = "Todos os valores devem ser preenchidos!"

		if( len(logado) == 0 ):
			logado.append(None)
        	
		logado.append(mensagem)

		return logado


		

    # ----------------------------------- #