class Produto():

	__slots__ = ['_nome', '_preco', '_qnt', '_historico']

	def __init__(self, nome, preco, qnt=1):
		self._nome = nome 
		self._preco = preco
		self._qnt = qnt 
		self._historico = historico

	@property
	def nome(self):
		return self._nome

	@property
	def preco(self):
		return self._preco

	@property
	def qnt(self):
		return self._qnt

	@property
	def historico(self):
		return self._historico

	# ----------------------------------- #

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@preco.setter
	def preco(self, preco):
		self._preco = preco

	@qnt.setter
	def qnt(self, qnt):
		self._qnt = qnt



