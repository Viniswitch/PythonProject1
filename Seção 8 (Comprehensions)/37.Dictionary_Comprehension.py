"""
 - Dictionary Comprehension :

Se quisermos criar uma listas temos :
    Listas = [1, 2, 3, 4]

Se quisermos criar uma tuplas :
    tupla = (1, 2, 3, 4)

Se quisermos criar um set :
    set = {1, 2, 3, 4}

Se quisermos criar um dicionario :
    dicionario = {'a' :1, 'b' : 2, 'c' : 3, 'd' : 4}

- Sintaxe do Dictionary Comprehension :
{chave : valor for valor in iteravel}
"""


#    Exemplo 1 :
dicionario = {'a' :1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6}

quadrado = {chave : valor ** 2 for chave, valor in dicionario.items()}

print(quadrado)

#    Exemplo 2 :

chaves = 'abcdefghij'

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mistura = {chaves[i] : valores[i] for i in range(len(chaves))}

print(mistura)


#    Exemplo com logica condicional :
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = {num : ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)








