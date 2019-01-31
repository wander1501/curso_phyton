import csv

def read_csv(file):
    table = list() # Tabela é uma lista de linhas

    with open(file) as csv_file:
         reader = csv.DictReader(csv_file)
         for row in reader:
             table.append(row)
    return table

def is_float(idade):
    try:
      float(idade)
      return True
    except ValueError:
      return False

titanic_tbl = read_csv("train.csv")

idades = [float(passg["age"]) for passg in titanic_tbl if is_float(passg["age"])]
idades_vivos = [float(passg["age"]) for passg in titanic_tbl
                if is_float(passg["age"]) and passg["survived"] == "1"]
idades_mortos = [float(passg["age"]) for passg in titanic_tbl
                 if is_float(passg["age"]) and passg["survived"] == "0"]

media = sum(idades) / len(idades)
media_vivos = sum(idades_vivos) / len(idades_vivos)
media_mortos = sum(idades_mortos) / len(idades_mortos)

print("Média de idade de todos passageiros: ",  media)
print("Média de idade dos sobreviventes: ", media_vivos)
print("Média de idade dos passageiros mortos: ", media_mortos)
