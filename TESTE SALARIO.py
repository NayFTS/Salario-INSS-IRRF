import unittest

from SALARIO import Salario_1

class SalarioTest(unittest.TestCase):


    def test_salario_bruto(self):
        salario = Salario_1(4620)
        self.assertEqual(4620, salario.salario_bruto)


    def test_inss(self):
        salario = Salario_1(4620)
        self.assertEqual(508.205, salario.inss1())

    def test_salario_com_contribuicao(self):
        salario = Salario_1(4620)
        self.assertEqual(4111.795, salario.salario_com_contribuicao())

    def test_irrf1(self):
        salario = Salario_1(4620)
        self.assertEqual(289.0288750000001, salario.irrf1())

    def test_salario_liquido(self):
        salario = Salario_1(4620)
        self.assertEqual(3822.766125, salario.salarioliquido())
