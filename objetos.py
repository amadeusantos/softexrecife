class mesa:
    pernas = 4
    tamanho = [160.0, 90.0]
    altura = 77.0
    pesoSuportado = 40.0
    montada = False

    def montar(self):
        if self.montada:
            print("A mesa já esta montada.")
        else:
            print("Motando mesa.")

    def mover(self):
        print("Movendo.")

    def limpar(self):
        print("Limpando mesa.")


class balde:
    formato = "Cilíndrico"
    altura = 26.0
    capacidade = 12.0

    def pegar(self):
        print("Pegando liquido.")

    def dispejar(self):
        print("Dispejando.")

    def lavar(self):
        print("Lavando balde.")


class audio:
    frequencia = 5.000
    decbeis = 60
    tempo = 360

    def reproduzir(self):
        print("Reproduzindo audio.")

    def voltar(self):
        print("Retornando um ponto do audio.")

    def aumentar(self):
        self.decbeis += 2
        print(self.decbeis)

    def diminuir(self):
        self.decbeis -= 2
        print(self.decbeis)


class fronteira:
    paises = ["Brasil", "Argentina"]
    tamanho = 1261.3
    terrestre = 1236.2
    aquatica = 25.1

    def atravezPorAgua(self):
        print("Pegando um barco.")

    def atravezPorTerra(self):
        print("Pegando um carro.")

    def atravezPorAr(self):
        print("Pegando um avião.")
