# from calculadora import calculadora

def calculadora(n1, n2, operation):
    resultado = 0
    if operation == 1:
        resultado = n1 + n2
    elif operation == 2:
        resultado = n1 - n2
    elif operation == 3:
        resultado = n1 * n2
    elif operation == 4:
        resultado = n1 / n2
    return resultado



print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("0- Sair")

operation = int(input("Operação: "))
while operation != 0:
    if 1 <= operation <= 4:
        n1 = float(input("Qual o primeiro valor: "))
        n2 = float(input("Qual o segundo valor: "))
        print(calculadora(n1, n2, operation))
    else:
        print("Essa opção não existe!")
    operation = int(input("Operação: "))

