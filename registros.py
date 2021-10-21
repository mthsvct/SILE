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

	def cadastraFUNC(self, funcionario):
		self.funcionarios.append(funcionario)
		print("Cadastro de funcionário realizado com sucesso! ")
