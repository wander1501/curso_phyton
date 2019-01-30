import requests
import json
from collections import Counter

lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)

contador = Counter(lista)
print(contador)
