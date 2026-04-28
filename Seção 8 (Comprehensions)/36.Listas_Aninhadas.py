"""
 - Listas Aninhadas (Nested Lists) :
      Algumas linguagems de programação (C, Java,...) possuem uma estrutura de dados chamada Arrays :
        1.Unidimensionais (Arrays/Vetores)
        2.Multidimensionais (Matrizes)

  Em Python, nós temos as Listaas :
  Explo : numeros = [1, 'b', 3.14, True, 5]

"""


#    Exemplo 1 :
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]#    Matriz 3x3
'''Sendo cada lista uma linha, e sua posição sua coluna exp: listas[0] = 1 coluna, listas[1] = 2 coluna'''

print(listas)
print(type(listas))
print(listas[0])
print(listas[1])
print(listas[2])


#    Como fazemos para acessar os dados :
print(listas[0][1])#    Fazendo o acesso ao elemento da primeira linha da segunda coluna
print(listas[-3][-2])#    Fazendo acesso ao mesmo alemento de forma invertida
print(listas[2][2])#    Fazendo o acesso ao elemento da terceira linha da terceira coluna


#    Iterando com loops em uma lista aninhada :
for lista in listas:
    for numero in lista:
        print(numero)


#    Usando List Comprehension :
[[print(num) for num in lista] for lista in listas]


#    Outros Exemplos :

#    Gerando um tabuleiro(Matriz) 3x3 :
tabuleiro = [[numero for numero in range(1, 4)] for lista in range(1, 4)]
print(tabuleiro)

#    Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for lista in range(1, 4)]
print(velha)

#    Gerando as colunas :
for lista in velha:
    print(lista)

#    Forma mais direta:
[print(lista) for lista in [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for lista in range(1, 4)]]



