# 📘 LISTA DE EXERCÍCIOS — COMPREHENSIONS


# 🔹 🟡 NÍVEL MÉDIO (base sólida)

#    1.Crie uma lista com os números de 1 a 10 usando **list comprehension**
print([int(numero) for numero in range(1,11)])


#   2.Crie uma lista com os quadrados de 1 a 10
quadrados = [numero ** 2 for numero in range(1,11)]
print(quadrados)


#    3.Crie uma lista apenas com os números pares de 1 a 20
print([par for par in range(1,21) if par % 2 == 0])


#    4.Crie uma lista com os números ímpares de 1 a 20
print([impar for impar in range(1,21) if impar % 2 != 0])


#    5.Dada a lista: [1,2,3,4,5] Crie outra lista com o dobro de cada número
print([numero * 2 for numero in [1, 2, 3, 4, 5]])


# 🔹 🟠 NÍVEL MÉDIO–DIFÍCIL

#    6.Dada uma lista:[1,2,3,4,5] Crie uma nova lista onde: número par → "par" e número ímpar → "ímpar"
print(["par" if num % 2 == 0 else "impar" for num in [1, 2, 3, 4, 5]])


#    7.Dada uma lista de números: retorne apenas os maiores que 10
import random
numeros = [random.randint(1,100) for i in range(10)]
print([num for num in numeros if num > 10])


#    8.Dada uma lista de strings: ["python", "java", "c"] Crie uma lista com o tamanho de cada palavra
print([len(palavra) for palavra in ["python", "java", "c"]])


#    9.Dada uma lista:[1,2,3,4,5] Crie uma nova lista com:
#    número par → multiplicado por 2
#    número ímpar → multiplicado por 3

print([num * 2 if num % 2 == 0 else num * 3 for num in [1, 2, 3, 4, 5]])


# 🔹 🔴 LISTAS ANINHADAS

#    10.Crie uma matriz 3x3 com números 0
print([[0 for _ in range(3)] for _ in range(3)])


#    11.Crie uma matriz 3x3 com números de 1 a 9
print([[random.randint(1,10) for coluna in range (1,4)] for linha in range(1,4)])


#    12.Crie uma matriz 4x4 onde: se a soma dos índices for par → 1. senão → 0
matriz4 = ([[random.randint(1,10) for x in range (1,5)] for y in range(1,5)])
print(matriz4)


#    13.Dada uma matriz:[[1,2],[3,4],[5,6]] Crie uma lista com todos os elementos (flatten)
matriz = [[1,2],[3,4],[5,6]]
print([elemento for linha in matriz for elemento in linha])



# 🔹 🔵 DICTIONARY COMPREHENSION


#    14.Crie um dicionário onde: chave → número de 1 a 5, valor → quadrado do número
dicionario = {num : num ** 2 for num in range(1,6)}
print(dicionario)


#    15.Dada uma lista:[1,2,3,4,5] Crie um dicionário com: chave → número, valor → "par" ou "ímpar"
dicionario = {num : ("par" if num % 2 == 0 else "impar") for num in [1, 2, 3, 4, 5]}
print(dicionario)


#    16.Dada uma lista de palavras:["python", "java", "c"] Crie um dicionário: chave → palavra, valor → tamanho
print({palavra : len(palavra) for palavra in ["python", "java", "c"]})


# 🔹 🟣 SET COMPREHENSION


#    17.Crie um conjunto com números de 1 a 10
print({num for num in range(1,11)})


#    18.Crie um conjunto com apenas números pares de 1 a 20
print({num for num in range(1,21) if num % 2 == 0})


#    19.Dada uma lista com valores repetidos:[1,2,2,3,3,3] Use set comprehension para remover duplicados
lista = [1, 2, 2, 3, 3, 3]
print({num for num in lista})


# 🔥 NÍVEL PROVA (onde você evolui)


#    20.Dada uma lista:[1,2,3,4,5] Crie uma lista de listas: [[1,1],[2,2],[3,3],[4,4],[5,5]]
lista = [1, 2, 3, 3, 4, 5]
print([[n, n] for n in lista])

#    21.Crie uma matriz 3x3 onde:diagonal principal = 1 resto = 0
print([[1 if i==j else 0 for j in range(3)] for i in range(3)])


#    22.Dada uma lista de strings: ["ana", "python", "arara", "java"] Crie uma lista apenas com os palíndromos
nomes = ["ana","python","arara","java"]
print([palavra for palavra in nomes if palavra == palavra[::-1]])
