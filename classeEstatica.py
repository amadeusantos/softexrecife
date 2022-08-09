class Cambio:
    IOF = 0.6
    dolar = 5.10

    @staticmethod
    def paraDolar(valor: float):
        return Cambio.dolar * valor * (1 + Cambio.IOF)

    @staticmethod
    def variacaoDolar(variacao: float):
        Cambio.dolar += variacao


a = Cambio
print(a.paraDolar(7))  # 5.10 * 7 * 1.6 == 57.12
b = Cambio.paraDolar(7)
Cambio.variacaoDolar(-0.90)
c = Cambio.paraDolar(7)  # 5.10 * 7 * 1.6 == 47.04
print(b)
print(c)

