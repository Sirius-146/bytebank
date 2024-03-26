#Criando Ambiente Virtual
#nome_do_ambiente_virtual geralmente também é venv
#python3 -m venv nome_do_ambiente_virtual
#Ativando Ambiente Virtual
#nome_do_ambiente_virtual\Scripts\Activate
#Desativando Ambiente Virtual
#deactivate

from datetime import date

class Funcionario:
	def __init__(self, nome, data_nascimento, salario):
		self._nome = nome
		self._data_nascimento = data_nascimento
		self._salario = salario
	
	@property
	def nome(self):
		return self._nome
	
	@property
	def salario(self):
		return self._salario
	
	def idade(self):
		*_, ano = tuple(self._data_nascimento.split('/'))
		ano_atual = date.today().year
		return ano_atual - int(ano)
	
	def sobrenome(self):
		nome_completo = self.nome.strip()
		*_, sobrenome = nome_completo.split(' ')
		return sobrenome
	
	def _testa_diretor(self):
		sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Khan', 'Tudor']
		return (self._salario >= 100_000) and (self.sobrenome() in sobrenomes)

	def decrescimo_salario(self):
		if self._testa_diretor():
			self._salario = self._salario - (self._salario * 0.1)

	def calcular_bonus(self):
		valor = self._salario * 0.1
		if valor > 1000:
			raise Exception('Salary_too_High')
		return valor
	
	def __str__(self):
		return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'