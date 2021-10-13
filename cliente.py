class Cliente():

	__slots__ = ['_nome', '_cpf', '_endereco', '_email', '_telefone', '_historico']

	def __init__(self, nome, cpf, endereco, email, telefone, historico):
		self._nome = nome
		self._cpf = cpf 
		self._endereco = endereco
		self._email = email
		self._telefone = telefone
		self._historico = historico

	@property
	def nome(self):
		return self._nome

	@property
	def cpf(self):
		return self._cpf

	@property
	def endereco(self):
		return self._endereco

	@property
	def email(self):
		return self._email

	@property
	def telefone(self):
		return self._telefone

	@property
	def historico(self):
		return self._historico

	# ----------------------------------- #

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@endereco.setter
	def endereco(self, endereco):
		self._endereco = endereco

	@email.setter
	def email(self, email):
		self._email = email

	@telefone.setter
	def telefone(self, telefone):
		self._telefone = telefone

	@historico.setter
	def historico(self, historico):
		self._historico = historico





