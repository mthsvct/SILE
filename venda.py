class Venda():

	__slots__ = ['_cliente', '_funcionario', '_produto', '_historico']

	def __init__(self, cliente, funcionario, produto, pagamento):
		self._cliente = cliente
		self._funcionario = funcionario
		self._produto = produto
		self._pagamento = pagamento
		self._historico = historico

	@property
	def cliente(self):
		return self._cliente

	@property
	def funcionario(self):
		return self._funcionario

	@property
	def produto(self):
		return self._produto

	@property
	def produto(self):
		return self._produto

	@property
	def pagamento(self):
		return self._pagamento

	@property
	def historico(self):
		return self._historico


	# ----------------------------------- #

	@cliente.setter
	def cliente(self, cliente):
		self._cliente = cliente

	@funcionario.setter
	def funcionario(self, funcionario):
		self._funcionario = funcionario

	@produto.setter
	def produto(self, produto):
		self._produto = produto

	@pagamento.setter
	def pagamento(self, pagamento):
		self._pagamento = pagamento

	@historico.setter
	def historico(self, historico):
		self._historico = historico
