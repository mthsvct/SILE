class Login:

	__slots__ = []

	def __init__(self, senha, pessoa):
		self._usuario = pessoa.email
		self._senha = senha
		self._tel_recuperacao = pessoa.telefone

	@property
	def usuario(self):
		return self._usuario

	@property
	def senha(self):
		return self._senha

	@property
	def tel_recuperacao(self):
		return self._tel_recuperacao

	# ----------------------- #

	@usuario.setter
	def usuario(self, usuario):
		self._usuario = usuario

	@senha.setter
	def senha(self, senha):
		self._senha = senha

	@tel_recuperacao.setter
	def tel_recuperacao(self, tel_recuperacao):
		self._tel_recuperacao = tel_recuperacao






