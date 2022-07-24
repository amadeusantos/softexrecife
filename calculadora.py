def calculadora(n1, n2, operation):
    resultado = 0
    if operation == 1:
        resultado = n1 + n2
    elif operation == 2:
        resultado = n1 - n2
    elif operation == 3:
        resultado = n1 * n2
    elif operation == 4:
        operation = n1 / n2
    return resultado

