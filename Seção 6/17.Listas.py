"""
- Listas : Em Python, funcionam como vetores ou matrizes (arrays) em outras linguagens, com a diferença de
serem dinamicos, e também de podermos colocar quaLquer tipo de dado

#    Linguagens C/Java : Os "arrays" possuem tamanho e tipo de dado fixo, ou seja, nessas linguagens
                          se você criar um array do tipo "int" e com "tamanho 5", este "array" sera
                          sempre do tipo "int" e poderá ter sempre "no maximo 5 valores"

- Em Python : Não possuem tamanho fixo, ou seja, podemos criar a lista e simplismente adicionar mais elementos em
              quanto houver memoria na maquina. As listas não possuem tipo de dado fixo, ou seja, podemos colocar
              qualquer tipo de dado

#    As listas, em Python, são representadas por cochetes []
"""

type([])

lista = [1852, 22, 38, 4125, 516, 25, 705, 22, 18, 103]

lista2 = ["V", "i", "n", "i", "s", "w", "i", "t", "c", "h"]

lista3 = [  ]

lista4 = list(range(11))

#    Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f"Encontrei o Nº{num} na lista!")
else:
    print(f"Não encontrei o Nº{num} na lista!")


#    Podemos facilmente ordenar uma lista
lista.sort()
print(lista)
print(type(lista))

#    Podemos facilmente contar o numero de ocorrencias de um valor de uma lista
print(lista.count(22))
print(lista2.count("i"))


#    Podemos facilmente adicionar elementos em uma lista (Ultilizamos  a função "append")
print(f"lista 1 ={lista}")
lista.append(955084845)
print(f"lista 1 com mais um elemento {lista}")


#   Obs: Nós só conseguimos adicionar um elemento por vez, mas é possivel adicionar uma lista dentro de outra Exp.:
lista.append((655, 9786, 48498, 404))#    Coloca a lista como elemento unico
print(lista)

if [655, 9786, 48498, 404] in lista:
    print("Encontrei a lista")

else:
    print("Não encontrei a lista")

lista.extend([666, 1227, 404])#    Colocar a lista como cada elemento
print(lista)

#    _______________________________________________________________________________________________________________

list1 = [1, 2, 3, 4, 5]

list2 = ["Viniswitch"]

list3 = ['W', 'e', 'l', 'l', 's', '404']

#    Podemos inserir um novo elemento na lista informando a posição do indice
list1.insert(2, "Novo Valor")
print(f"Inserindo Novo valor na lista:{list1}")


#    Podemos facilmente juntar duas listas

list4 = list1 + list2
print(f"Ex1 : {list4}")

list1 = list1 + list2
print(f"Ex2 :{list1}")

list1.extend(list2)
print(f"Ex3 :{list1}")


#    Podemos facilmente inverter uma lista
#    Exp.1:
list1.reverse()
list2.reverse()
print(f"Lista 1 reveretida :{list1}")
print(f"Lista 2 reveretida :{list2}")
#   Exp.2:
print("Exemplo 2:")
print(f"Lista 1 revertida :{list1[::-1]}")


#    Podemos facilmente copiar uma lista

list1 = [1, 2, 3, 4, 5]

list2 = ["Viniswitch"]

#list3 = ['W', 'e', 'l', 'l', 's', '404']

list4 = [1, 3, 22, 64, 'w', 'e', 'l', 'l', 's', 16, 5, "Viniswitch"]

listx = list1[2:4].copy()
print(listx)


#    Podemos facilmente contar quantos elementos existem dentro de uma lista
print(len(list2))
print(len(list3))


#    Podemos facilmente remover o ultimo elemento de uma lista, devolvendo o elemento retirado
print(list3)
list3.pop()
print(list3)


#    Podemos também retirar um elemento pelo indice
list3.pop(0)
print(list3)


#    Podemos facilmente remover todos os elementos de uma lista
print(list4)
list4.clear()
print(list4)


#    Podemos facilmente repetir/multiplicar elementos em uma lista
nova = [1, 2, 3, 4, 5]
print(nova)
nova = nova * 3
print(nova)


#    Podemos facilmente converter uma string para uma lista

#    Exp.1:
nome = "The Lord of The Rings"
print(nome)
nome = nome.split()
print(nome)

#    Exp.2:
nome = "The,Lord,of,The,Rings"
print(nome)
nome = nome.split(",")#   definindo a ","como separador de elemento
print(nome)


#    Podemos facilmente converter uma lista para string
filme = ['The', 'Chronicles', 'of', 'Narnia']
print(filme)
filme = " ".join(filme)
print(filme)


tudo =[1, 2, 3.14, True, "Sherlock Holmes", "A", ['Lista dentro da lista'] ]
print(tudo)
print(type(tudo))

'''
#    Iterando sobre uma lista

#    Exp.1: Ultilizando o for
book = ['A', 'r', 's', 'e', 'n', 'e', ' ', 'L', 'u', 'p', 'i', 'n']
for elemento in book:
    print(elemento, end="   ")#    Para dixar a lista na mesma linha
print(" ")

#   Exp.2: Ultilizando o while
carrinho = [ ]#    Lista vazia
produto = ""#    Variavel tipo string

while produto != "sair":
    print("Adicione um produto no carrinho, ou digite 'sair' para sair")
    produto = input()
    print(f'O produto {produto} foi cadastrado com sucesso')
    if produto != "sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
'''


#    Ultilizano variaveis em uma lista
listnum = [1, 2, 3, 4, 5]
print(listnum)

num = 1
num1 = 2
num2 = 3
num3 = 4
num4 = 5

nums = [num, num1, num2, num3, num4]
print(nums)


#    Em listas, fazemos o acesso aos elementos de forma indexada
casa = ["corvinal", "grifinoria", "lufa-lufa", "snserina"]
#        [   0,         1,         2        3   ]
print(casa[0])
print(casa[1])
print(casa[2])
print(casa[3])

#    Fazendo acesso aos elementos indexados de forma inversa
print(casa[-1])
print(casa[-2])
print(casa[-3])
print(casa[-4])


#    Relembrando o loop
elemento = ['água', 'terra', 'fogo', 'ar']
for elemento in elemento:
    print(elemento)

elemento = ['água', 'terra', 'fogo', 'ar']
indice = 0#    variavel começando em 0
while indice < len(elemento):#    en quanto o "indicice" for menor q o tamanho de [casa]
    print(elemento[indice])
    indice = indice + 1#    Para incrementar o valor de indice, mudando a posição de [casa]


#    Como saber o indice dos elementos em uma lista
sla = ["Sherlock Holmes", "Corvinal", "Aldebaran", "Iron Man", "Naruto", "Cyberpunk 2077", "God of War",
    "Batman","Superman", "Mulher-Maravilha", "Homem-Aranha", "Darth Vader", "Skywalker", "Yoda", "Gandalf", "Bolseiro",
    "Aragorn", "Geralt de Rívia", "Kratos", "Link", "Zelda", "Samurai", "Fullmetal", "Lara Croft","Neo", "Thanos",
    "Capitão América", "Flash", "One Piece", "Dragon Ball"]

for indice, sla in enumerate(sla):
    print(indice, sla)



#    Como saber o indice de um elemento especifico
sla = ["Sherlock Holmes", "Corvinal", "Aldebaran", "Iron Man", "Naruto", "Cyberpunk 2077", "God of War",
    "Batman","Superman", "Mulher-Maravilha", "Homem-Aranha", "Darth Vader", "Skywalker", "Yoda", "Gandalf", "Bolseiro",
    "Aragorn", "Geralt de Rívia", "Kratos", "Link", "Zelda", "Samurai", "Fullmetal", "Lara Croft","Neo", "Thanos",
    "Capitão América", "Flash", "One Piece", "Dragon Ball", "Dante"]

print(sla.index("Link"))
print(sla.index("Dante"))


#    Podemos fazer uma busca na lista, de um elementos à partir de um indice especifico, até outro indice
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num.index(5, 4))

print(num.index(5, 2, 5))


#    listas aceitam valores repetidos
list = []
list.append(42)
list.append(42)
list.append(33)
list.append(33)
list.append(42)
print(list)


#    Relembrando o "Slice"
#    Lista = [inicio:fim:passo]
#    range = [Inicio:fim:passo]

#    Trabalhando com "slice" de lista com o parametro "inicio"
sla = ["Sherlock Holmes", "Corvinal", "Aldebaran", "Iron Man", "Naruto", "Cyberpunk 2077", "God of War",
    "Batman","Superman", "Mulher-Maravilha", "Homem-Aranha", "Darth Vader", "Skywalker", "Yoda", "Gandalf", "Bolseiro",
    "Aragorn", "Geralt de Rívia", "Kratos", "Link", "Zelda", "Samurai", "Fullmetal", "Lara Croft","Neo", "Thanos",
    "Capitão América", "Flash", "One Piece", "Dragon Ball"]

print(f"Exemplo 1 :{(sla[0:10])}")
print(f"Exemplo 2 :{(sla[-10:])}")
print(f"Exemplo 3 :{(sla[0::3])}")#    começa em 0 e pega o 3ºnumero, em seguida do outro, até o final


#    Invertendo valores em uma lista
names = ["Viniswitch", "Potter", "Wells_404", "Ash_Br0708"]

names[0], names[1], names[2], names[3] = names[3], names[2], names[1], names[0]
print(names)
#    Forma melhor:
names = ["Viniswitch", "Potter", "Wells_404", "Ash_Br0708"]

names.reverse()
print(names)


#    Soma, Valor máximo, Valor minimo e tamanho de uma lista
#    *Se todos os elementos forem numeros "int" ou "float"

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'soma dos elementos da lista :{sum(num)}')
print(f'Maior valor da lista :{max(num)}')
print(f'Menor valor da lista :{min(num)}')
print(f'Quantidade de elementos da lista :{len(num)}')


#    Transformar uma lista em tupla
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = tuple(num)
print(tupla)
print(type(tupla))


#    Desempacotamento de lista
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = num
print(num1)
print(num2)
print(num3)
#    Se tivermos mais elementos para desempacotar do que variaveis, teremos erro. isso vale para o inverso


#    Copiando uma lista para outra (Shallow Copy e Deep Copy)

#    Forma 1 : Deep Copy
list = [1, 2, 3, 4, 5]
print(list)

nova = list.copy()
print(nova)

nova.append(6)

print(list)
print(nova)
""" Veja que quando ultilizamos o list.copy(), copiamos os dados de uma lista para uma nova lista, criando uma lista
 igual a lista anterior, mas que são independetes à alterações . Ou seja, modificar a nova lista não afeta a lista
 antiga, e virse versa : Isso em Python é chamado de Deep Copy"""


#    Forma 2 : Shallow Copy
lista = [1, 2, 3, 4, 5]
print(lista)

nova = lista
print(nova)

nova.append(6)

print(lista)
print(nova)
''' Veja que ultilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar uma
modificação em uma lista, essa modificação foi realizada nas duas listas : Isso em Python é chamado de Shallow Copy'''


