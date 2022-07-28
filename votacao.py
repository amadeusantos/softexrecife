import enum


class Candidatos(enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0


lista = {Candidatos.candidato_Z: 0, Candidatos.candidato_X: 0, Candidatos.candidato_Y: 0, Candidatos.branco: 0}
quantVotos = int(input("Quantos eleitores?"))
for e in range(0, quantVotos):
    try:
        voto = int(input("Número do candidato: "))
    except ValueError:
        voto = int(input("Por favor digite um número! ex. 346 "))
    finally:
        if Candidatos.candidato_X.value == voto:
            lista[Candidatos.candidato_X] += 1
        elif Candidatos.candidato_Y.value == voto:
            lista[Candidatos.candidato_Y] += 1
        elif Candidatos.candidato_Z.value == voto:
            lista[Candidatos.candidato_Z] += 1
        else:
            lista[Candidatos.branco] += 1

ganhador = ["", 0]
for c, v in lista.items():
    print(f"{str(c).removeprefix('Candidatos.')}: {v}")
    if ganhador[1] < v and c != Candidatos.branco:
        ganhador = [c, v]

if ganhador[0] == Candidatos.branco:
    print("O resultado foi empate.")
else:
    print(f"{str(ganhador[0]).removeprefix('Candidatos.')} foi o ganhador com {ganhador[1]} votos.")
