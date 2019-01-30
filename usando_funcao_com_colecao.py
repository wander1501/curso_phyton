from conta_10_maiores_ocorrencias import conta_10_maiores_ocorrencias
import requests
import json

resultado = conta_10_maiores_ocorrencias(requests.get("https://bit.ly/2RXuXsD").text)
print(resultado)
