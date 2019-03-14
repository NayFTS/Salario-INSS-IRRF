class Salario_1:
    def __init__(self, salario_bruto):
        self.salario_bruto = salario_bruto

    def inss1(self):
        sb = self.salario_bruto
        if sb >= 0 and sb <= 1693.72:
            inss = (sb * 0.08)
        if sb >= 1693.73 and sb <= 2822.90:
            inss = (sb * 0.09)
        if sb >= 2822.91 and sb <= 5645.80:
           inss = (sb* 0.11)
        inss = ((inss*100 + 0.5) / 100.0)
        return inss

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
