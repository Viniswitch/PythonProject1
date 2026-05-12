"""
 - Filter : Serve para filtrar dados de uma determinada coleção. Assim como a função map, a funcão, filter recebe 2
  parametros, sendo o primeiro uma função e o segundo uma iteravel


"""

#    biblioteca para trabalhar com dados estatisticos :
import statistics

#    Dados coletados de algum lugar :
dados = [1.3, 3.14, 5, 0.42, -2, 7]

#    Calculando a media dos dados ultilizando a função mean (media) :
media = statistics.mean(dados)
print(f'Media : {media}')


#    Fazendo uma lista filtrando os numeros menores que a media
res = filter(lambda x : x > media, dados)
print(list(res))

print(list(filter(lambda x: x > media, dados)))







