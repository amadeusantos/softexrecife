import pandas as pd

alunos = pd.read_csv("./planilha_da_sala/notas_alunos.csv")
"""
        nota_1  nota_2  faltas
João       8.4     4.5       2
Mateus     8.4     7.4       9
Maria      8.1     9.3       3
"""


alunos["media"] = (alunos["nota_1"] + alunos["nota_2"]) / 2
alunos.loc[alunos["media"] >= 7, "situacao"] = "APROVADO"
alunos.loc[alunos["faltas"] <= 5, "situacao"] = "APROVADO"
alunos.loc[alunos["media"] < 7, "situacao"] = "REPROVADO"
alunos.loc[alunos["faltas"] > 5, "situacao"] = "REPROVADO"

alunos.to_csv("./planilha_da_sala/alunos_situacao.csv")
