from historico import Historico

class Cliente:
	
	__slots__ = ['_pessoa', '_historico']

	def __init__(self, pessoa):
		self._pessoa = pessoa
		self._historico = Historico()

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
	def historico(self):
		return self._historico

	
		
