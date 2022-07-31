class numeroComplexo:
    def real(self, n1):
        return int(n1[:n1.index("+")])

    def img(self, n1):
        return int(n1[n1.index("+") + 1: n1.index("i")])

    def soma(self, n1, n2):
        real = self.real(n1) + self.real(n2)
        img = self.img(n1) + self.img(n2)
        return f"{real} + {img}i" if img > 0 else f"{real} - {abs(img)}i"

    def subtracao(self, n1, n2):
        real = self.real(n1) - self.real(n2)
        img = self.img(n1) - self.img(n2)
        return f"{real} + {img}i" if img > 0 else f"{real} - {abs(img)}i"

    def multiplicacao(self, n1, n2):
        a = self.real(n1)
        b = self.img(n1)
        c = self.real(n2)
        d = self.img(n2)
        real = a * c - b * d
        img = a * d + b * c
        return f"{real} + {img}i" if img > 0 else f"{real} - {abs(img)}i"

    def divisao(self, n1, n2):
        a = self.real(n1)
        b = self.img(n1)
        c = self.real(n2)
        d = self.img(n2)
        real = (a * c + b * d) / (c ** 2 + d ** 2)
        img = (b * c - a * d) / (c ** 2 + d ** 2)
        return f"{real} + {img}i" if img > 0 else f"{real} - {abs(img)}i"


# testes
x = numeroComplexo()
print(x.soma("7+4i", "8+7i"))
print(x.subtracao("7+4i", "8+7i"))
print(x.multiplicacao("7+4i", "8+7i"))
print(x.divisao("7+4i", "8+7i"))
