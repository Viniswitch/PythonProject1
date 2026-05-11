"""
 - Maps : Com map, fazemos mapeamento de valores para a função. É uma função que recebe 2 parametros, sendo o primeiro
  a função e, o segundo uma iteravel ou mais iteraiveis que o map irá mapear e aplicar a função

#    OBS : Após ultilizar a função map, depois da primeira ultilização, o conteudo armazenado é zerado

"""

import math

def area(r):
    return math.pi * r ** 2

print(area(2))

raios = [0.42, 1, 2, 3.14, 4]


#    Forma 1 "comum" :
areas = []
for r in raios:
    areas.append(area(r))
print(areas)


#    Usando 2 usando o map :
areas = map(area, raios)
print(list(areas))
print(type(areas))#    Retorna um Map Object


print(list(map(area, raios)))#    Forma 2.2 mais curta


#    Forma 3 map com lambda :
print(list(map(lambda r2: math.pi * (r2 ** 2), raios)))


#    Outro exemplo :

cidades = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Tokyo", 27), ("Recife", 31)]





