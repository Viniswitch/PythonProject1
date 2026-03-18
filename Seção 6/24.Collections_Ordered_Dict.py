"""
 - Collections - Ordered Dict : Igual a um dicionario comum, mas com uma ordem de inserção especificada é garantida

#    Em um dicionario comum, a ordem de inserção dos elementos não é garantida

"""
#    Fazendo o import :
from collections import OrderedDict

dicionario = OrderedDict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})

for chave, valor in dicionario.items():
    print(f'chave = "{chave}" : valor = {valor}')

#    Entendendo a diferença entre DIct e OrderedDict :

#    Dict (Dicionario comum) :
dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"d": 4, "c": 3, "b": 2, "a": 1}

print(dict1)
print(dict2)
print(dict1 == dict2)#    "True" porque a ordem não importa

#    OrderedDict :
odict1 = OrderedDict({"a": 1, "b": 2, "c": 3, "d": 4})
odict2 = OrderedDict({"d": 4, "c": 3, "b": 2, "a": 1})

print(odict1)
print(odict2)
print(odict1 == odict2)#    "False" porque a ordem importa, e nesse caso ela difereentre ambos
