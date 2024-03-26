from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:

	def funcionario(self):
		return Funcionario('Lucas Bragança', '13/03/2000', 100_000)

	def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
		esperado= 24

		func_teste = self.funcionario()

		#When:
		result = func_teste.idade()

		#Then:
		assert result == esperado

	def test_quando_sobrenome_recebe_lucas_braganca_deve_retornar_braganca(self):
		esperado = 'Bragança'
		func_teste = self.funcionario()
		result = func_teste.sobrenome()
		assert result == esperado

	def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
		esperado = 90_000
		func_teste = self.funcionario()
		func_teste.decrescimo_salario()
		result = func_teste.salario
		assert result == esperado
	
	@mark.calcular_bonus
	def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
		with pytest.raises(Exception):
			func_teste= self.funcionario()
			result = func_teste.calcular_bonus()
			assert result

	@mark.calcular_bonus
	def test_quando_calcular_bonus_recebe_4600_deve_retornar_460(self):
		esperado = 460
		func_teste= Funcionario('Teste', '21/12/1981', 4600)
		result = func_teste.calcular_bonus()
		assert result == esperado
