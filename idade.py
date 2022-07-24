from datetime import datetime

while True:
    try:
        nome = str(input("Nome: "))
        ano = int(input("ano de nascimento: "))
        if 1922 <= ano <= 2021:
            break
        else:
            print("Idade invalida! Tente novamente.")
    except ValueError:
        print("Idade invalida! Digite o ano na forma númerica. ex: 2021")
print(f"nome: {nome}: {datetime.today().year - ano} anos")
