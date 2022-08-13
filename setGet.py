class Carro:
    def __init__(self, ano, modelo):
        self.__ano = ano
        self.__modelo = modelo

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getModelo(self):
        return self.__modelo

    def setModelo(self, modelo):
        self.__modelo = modelo


c = Carro(2000, "wert")
print(c.getAno(), c.getModelo())
