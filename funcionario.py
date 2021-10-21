class Funcionario:
	
	__slots__ = ['_pessoa', '_categoria', '_login']

	def __init__(self, pessoa, categoria, senha):
		self._pessoa = pessoa
		self._categoria = categoria
		self._login = login

	@property
	def pessoa(self):
		return self._pessoa

	@property
	def nome(self):
		return self._pessoa.nome

	@property
	def cpf(self):
		return self._pessoa.cpf

	@property
	def email(self):
		return self._pessoa.email

	@property
	def telefone(self):
		return self._pessoa.telefone

	@property
	def endereco(self):
		return self._pessoa.endereco

	@property
	def categoria(self):
		return self._categoria

	@property
	def login(self):
		return self._login

	@property
	def senha(self):
		return self._login.senha

	# ----------------------- #

	@pessoa.setter
	def pessoa(self, pessoa):
		self._pessoa = pessoa

	@categoria.setter
	def categoria(self, categoria):
		self._categoria = categoria

	@login.setter
	def login(self, login):
		self._login = login