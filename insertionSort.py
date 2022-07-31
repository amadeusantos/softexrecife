lista = [8, 68, 26, 78, 40, 86, 33, 63, 33, 59, 78, 27, 89, 1, 79, 91, 36, 77, 93, 10, 27, 39, 68, 56, 98, 90, 90, 70, 90, 7]
for key, n in enumerate(lista):
    for c in range(key - 1, -1, -1):
        if n < lista[c]:
            lista[c + 1] = lista[c]
            if c == 0:
                lista[0] = n
        else:
            lista[c + 1] = n
            break

print(lista)
# [1, 7, 8, 10, 26, 27, 27, 33, 33, 36, 39, 40, 56, 59, 63, 68, 68, 70, 77, 78, 78, 79, 86, 89, 90, 90, 90, 91, 93, 98]
