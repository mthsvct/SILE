class Pessoa:
	
	__slots__ = ['_nome', '_cpf', '_email', '_telefone']

	def __init__(self, nome, cpf, email, telefone):
		self._nome = nome
		self._cpf = cpf
		self._email = email
		self._telefone = telefone

	@property
	def nome(self):
		return self._nome

	@property
	def cpf(self):
		return self._cpf

	@property
	def email(self):
		return self._email

	@property
	def telefone(self):
		return self._telefone

	# ----------------------- #

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf

	@email.setter
	def email(self, email):
		self._email = email

	@telefone.setter
	def telefone(self, telefone):
		self._telefone = telefone

