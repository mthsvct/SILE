class Funcionario():

	__slots__ = ['_nome', '_cpf', '_categoria']

	def __init__(self, nome, cpf, categoria, historico):
		self._nome = nome
		self._cpf = cpf 
		self._categoria = categoria

	@property
	def nome(self):
		return self._nome

	@property
	def cpf(self):
		return self._cpf

	@property
	def categoria(self):
		return self._categoria

	# ----------------------------------- #

	def registraVENDA(self):
		pass










