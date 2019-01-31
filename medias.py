import csv

def read_csv(file):
    table = list() # Tabela é uma lista de linhas

    with open(file) as csv_file:
         reader = csv.DictReader(csv_file)
         for row in reader:
             table.append(row)
    return table

titanic_tbl = read_csv("train.csv")

soma_idades = 0
soma_idades_vivos = 0
soma_idades_mortos = 0
contados = 0
contados_vivos = 0
contados_mortos = 0

for passg in titanic_tbl:
    try:
       soma_idades += float(passg["age"])
       if (passg["survived"] == "1"):
          soma_idades_vivos += float(passg["age"])
          contados_vivos += 1
       else:
          soma_idades_mortos += float(passg["age"])
          contados_mortos += 1
       contados += 1
    except (ValueError):
       pass

media = soma_idades / contados
print("Média de idade de todos passageiros: ", "%.1f" % media)
media_vivos = soma_idades_vivos / contados_vivos
print("Média de idade dos sobreviventes: ", "%.1f" % media_vivos)
media_mortos = soma_idades_mortos / contados_mortos
print("Média de idade dos passageiros mortos: ", "%.1f" % media_mortos)
