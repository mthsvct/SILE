class Registros():

	__slots__ = ['_vendas']

	def __init__(self):
		self._vendas = []

	@property
	def vendas(self):
		return self._vendas

	# ----------------------------------- #

	def cadastraVENDA(self, venda):
		vendas.append(venda)


	def buscaVENDA(self, cpf, produto):
		encontrado = None
		for i in self.vendas:
			if( i.cliente.cpf == cpf and i.produto.nome == produto.nome and encontrado == None ):
				encontrado = i
		return encontrado

