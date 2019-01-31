from medias import read_csv
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = [num for num in lista if num % 2 == 0]
print(pares)

titanic_tbl = read_csv("train.csv")
jameses = [passg for passg in titanic_tbl if ("Mr. James" in passg["name"])]
print(jameses)
