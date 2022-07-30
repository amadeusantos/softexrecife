copia = []
lista = [7, 6, 3, 6, 5, 6, 8, 1, 0, 16, 14]
print(lista)
while copia != lista:
    copia = lista.copy()
    for i in range(len(lista) - 1):
        v1 = lista[i]
        v2 = lista[i + 1]
        if v1 > v2:
            lista[i] = v2
            lista[i + 1] = v1
print(lista)    # [0, 1, 3, 5, 6, 6, 6, 7, 8, 14, 16]
