from historico import Historico

class Cliente:
	
	__slots__ = ['_pessoa', '_historico']

	def __init__(self, pessoa=None):
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

	# --------------- SETERS -------------- #

	@nome.setter
	def nome(self, nome):
		self._pessoa.nome = nome

	@cpf.setter
	def cpf(self, cpf):
		self._pessoa.cpf = cpf

	@email.setter
	def email(self, email):
		self._pessoa.email = email
	
	@telefone.setter
	def telefone(self, telefone):
		self._pessoa.telefone = telefone

	# --------------- MÉTODOS -------------- #

	# Função que edita os dados de um cliente.
	def editar(self, nome='', cpf='', email='', tel=''):

		editado = []

		if( nome != '' and self.nome != nome):
			self.nome = nome
			editado.append('nome\n')

		if ( cpf != '' and self.cpf != cpf ):
			self.cpf = cpf
			editado.append('cpf\n')

		if( email != '' and self.email != email ):
			self.email = email
			editado.append('email\n')

		if ( tel != '' and self.telefone != tel ):
			self.telefone = tel
			editado.append('telefone\n')

		if(len(editado) == 0):
			mensagem = "Nenhum dado foi alterado!"
		else:
			mensagem = "Os seguintes dados foram alterados:\n"
			for i in editado: mensagem = mensagem + i

		return mensagem

