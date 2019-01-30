from collections import Counter

def conta_10_maiores_ocorrencias(contavel):

   contador = None

   if (type(contavel) == type("")):
      palavras = contavel.split()
      contador = Counter(palavras)
   else:
      contador = Counter(contavel)

   return contador.most_common(10)
