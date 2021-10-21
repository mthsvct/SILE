class Funcionario:
	
	__slots__ = ['_pessoa', '_senha']

	def __init__(self, pessoa, senha):
		self._pessoa = pessoa
		self._senha = senha

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
		return self._pessoa.enderecoa

	@property
	def senha(self):
		return self._senha

	# ----------------------- #

	@pessoa.setter
	def pessoa(self, pessoa):
		self._pessoa = pessoa

