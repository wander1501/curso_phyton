import requests
import json
lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)
dicionario = {}

for numero in lista:
    try:
      dicionario[numero] += 1
    except KeyError:
      dicionario[numero] = 1

print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
