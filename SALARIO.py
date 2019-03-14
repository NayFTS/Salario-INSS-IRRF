class Salario_1:
    def __init__(self, salario_bruto):
        self.salario_bruto = salario_bruto

    def inss1():
        if salario_bruto >= 0 and salario_bruto <= 1693.72:
            return (((salario_bruto * 0.08) *100 + 0.5) / 100.0)
        if salario_bruto >= 1693.73 and salario_bruto <= 2822.90:
            return (((salario_bruto * 0.09) *100 + 0.5) / 100.0)
        if salario_bruto >= 2822.91 and salario_bruto <= 5645.80:
           return (((salario_bruto* 0.11) *100 + 0.5) / 100.0)

    def salario_com_contribuicao():
        return (salario_bruto - self.inss1())

    def irrf1():
        atual = salario_com_contribuicao()

        if (atual >= 0 and atual < 1903.99):
            return (((atual *0) * 100 + 0.5) / 100.0)

        if (atual > 1903.99 and atual < 2826.65):
            return ((((atual * 0.075) - 142.80)* 100 + 0.5) / 100.0)

        if (atual > 2826.66 and atual < 3751.05):
            return((((atual* 0.15) - 354.80)* 100 + 0.5) / 100.0)

        if (atual > 3751.06 and atual < 4664.68):
            return ((((atual * 0.225) - 636.13)* 100 + 0.5) / 100.0)

        if (atual> 4664.69):
            return ((((atual * 0.275) - 869.36) * 100 + 0.5) / 100.0)

    def salarioliquido():
        salario_bruto - sel.inss1() - self.irrf1()
