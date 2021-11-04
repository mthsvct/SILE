from pessoa import Pessoa
from cliente import Cliente
from produto import Produto
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

    # Funções referentes a gestão de produtos;

    # Função que busca um produto na lista.
	def buscaPROD(self, codigo):
		encontrado = None
		for i in self.produtos:
			if i.cod == codigo:
				encontrado = i
		return encontrado

    # Função que cadastra um novo produto a lista de produtos.
	def cadastraPROD(self, codigo, nome, preco, qnt):
		if '' in [codigo, nome, preco, qnt]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			if self.buscaPROD(codigo) != None:
				# Existe um produto já cadastrado com o mesmo código
				mensagem = "O código informado já foi cadastrado!"
			else:
				# Produto pode ser cadastrado sem problemas.
				self.produtos.append(Produto(codigo, nome, preco, qnt))
				mensagem = "Cadastro de produto realizado com sucesso!"
		return mensagem

	# Função que apaga um produto da lista de produtos.
	def apagaPROD(self, codigo):

		if '' in [codigo]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			p = self.buscaPROD(codigo)
			if p == None:
				# Produto não encontrado.
				mensagem = "O produto que deseja remover não foi encontrado!"
			else:
				print(self.produtos)
				self.produtos.remove(p)
				mensagem = "Produto removido com sucesso!"
				print(self.produtos)
		return mensagem

	# -------------------------------------------------- #

	# Função que busca um cliente.
	def buscaCLIENTE(self, cpf):
		encontrado = None
		for i in self.clientes:
			if( i.cpf == cpf ):
				encontrado = i
		return encontrado

	# Função que cadastra um novo cliente à lista de clientes
	def cadastraCLIENTE(self, nome, cpf, email, tel):
		if '' in [nome, cpf, email, tel]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			if self.buscaCLIENTE(cpf) != None:
				# Existe um funcionario com esse mesmo CPF
				mensagem = "O CPF informado já foi cadastrado!"
			else:
				p = Pessoa(nome, cpf, email, tel)
				c = Cliente(p)
				self.clientes.append(c)
				mensagem = "Cadastro de cliente realizado com sucesso!"
		return mensagem

	# Função que apaga o registro de um cliente da lista de clientes
	def apagaCLIENTE(self, cpf):
		if cpf == '':
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			# Cpf foi digitado.
			c = self.buscaCLIENTE(cpf)
			if c == None:
				# Cliente não encontrado.
				mensagem = "O cliente buscado não foi encontrado!"
			else:
				print(len(self.clientes))
				self.clientes.remove(c)
				mensagem = "O registro do cliente foi apagado com sucesso!"
				print(len(self.clientes))
		return mensagem


	def editaCLIENTE_busca(self, cpf):
		retorno = []
		if cpf == '':
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			# CPF foi digitado.
			c = self.buscaCLIENTE(cpf)
			if c == None:
				mensagem = "O cliente buscado pelo o CPF não foi encontrado!"
			else:
				mensagem = "Cliente encontrado!"
				retorno.append(c)

		if len(retorno) == 0:
			retorno.append(None)

		retorno.append(mensagem)

		return retorno
