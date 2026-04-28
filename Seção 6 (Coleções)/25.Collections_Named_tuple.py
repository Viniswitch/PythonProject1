"""
 - Collections - Named Tuples : São tuplas onde especificamos parametros e um nome para a mesma

 - Tuples (Comum) : (Imutavel)
tupla = (1, 2, 3)

"""

#    Fazendo o import :
from collections import namedtuple


#    Definido o nome e os parametros :

#    Forma 1 : Declaração "namedtuple"
cachorro1 = namedtuple('cachorro', 'nome raça idade')

#    Forma 2 : Declaração "namedtuple"
cachorro2 = namedtuple('cachorro', 'nome, raça, idade')

#   Forma 3
cachorro3 = namedtuple('cachorro', ['nome', 'raça', 'idade'])


#    Usando a namedtuple
zelda = cachorro3(nome='Zelda', raça='Vira-Lata', idade ='7 Anos')
print(zelda)


#    Acessando os dados

#    Forma 1
print(zelda[0])#    nome
print(zelda[1])#    raça
print(zelda[2])#    idade

#   Forma 2
print(zelda.idade)#    idade
print(zelda.nome)#    nome
print(zelda.raça)#    raça


#    Outros usos
print(zelda.index('Vira-Lata'))#    Para mostrar o indice

print(zelda.count('Vira-Lata'))#    Para mostrar o numero de ocorrencias


