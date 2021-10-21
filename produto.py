from historico import Historico

class Produto():

	__slots__ = ['_cod','_nome', '_preco', '_qnt', '_historico']

	def __init__(self, cod, nome, preco, qnt=1):
		self._cod = cod
		self._nome = nome 
		self._preco = preco
		self._qnt = qnt 
		self._historico = Historico()

	@property
	def cod(self):
		return self._cod

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

	@cod.setter
	def cod(self, cod):
		self._cod = cod

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@preco.setter
	def preco(self, preco):
		self._preco = preco

	@qnt.setter
	def qnt(self, qnt):
		self._qnt = qnt



