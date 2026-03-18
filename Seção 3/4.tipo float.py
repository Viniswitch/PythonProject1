"""
-Tipo float

-Tipo real, decimal

-Casa decimais

-O separador das casas decimais é o (.)ponto e não a (,)virgula
"""

#    Errado do ponto de vista do float, mas gera uma tupla
valor= 1, 44
print(valor)
print(type(valor))

#    Certo do ponto de vista float
valor= 1.44
print(valor)
print(type(valor))

#    É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#    Podemos converter um float para int
""" OBS: Ao converter valores float para int, é perdido precisão"""
res = int(valor)
print(res)
print(type(res))

#    Podemos trabalhar com numeros complexos
variavel = 5j
print (variavel)
print(type(variavel))


