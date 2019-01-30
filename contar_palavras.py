import requests
import json
from collections import Counter

texto = requests.get("https://bit.ly/2Cu73N6").text

palavras = texto.split()
print("Imprimindo as palavras do texto.")
print(palavras)

contador = Counter(palavras)
print(" ")
print("Imprimindo o contador de palavras")
print(contador)
print(" ")
print("Imprimindo as 10 palavras mais comuns no texto")
print(contador.most_common(10))
