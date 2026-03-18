"""
 - Tuplas : São bastante parecidas com as listas, com o diferencial de serem limitadas por parenteses "()" e
 de serem imutaveis. Isso significa que, ao se criar uma "tupla" ela não muda. Toda operação com uma "tupla" gera
 uma nova "tupla"

"""


#    Por que ultilizar tuplas ?
#    -As tuplas são mais rápidas do que listas (melhores para analise de grandes dados)
#    -As tuplas deixam seu código mais seguro, devido a sua imutabilidade


#    Metodos para adição e remoção de elementos nas tuplas não existem, dado as tuplas serem imutaveis
#    Cuidado 1 : As tuplas são representadas por (), mas observe :
tupla = (1, 2, 3, 4, 5, 6)
print(tupla)
print(type(tupla))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))


#    Cuidado 2 : Tuplas com 1 elemento :
tupla3 = (22)#    Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (22,)
print(tupla4)
print(type(tupla4))
#    Conclusão : Podemos concluir que tuplas são definidas pela virgula, e não pelos parenteses


#   Podemos criar um range de tupla :
tupla = tuple(range(11))
print(tupla)
print(type(tupla))


#   Podemos desempacotar uma tupla
tupla = ("Viniswitch", "Cyberpunk2077", "HunterxHunter", "Gengar")

nome, jogo, anime, pokemon = tupla

print(nome)
print(jogo)
print(anime)
print(pokemon)


#    Soma, Valor Maximo< Valor Minimo e Tamanho de uma tupla
tupla = (1, 2, 3, 4, 5, 6)


print(f'soma dos elementos da tupla :{sum(tupla)}')
print(f'Maior valor da tupla :{max(tupla)}')
print(f'Menor valor da tupla :{min(tupla)}')
print(f'Quantidade de elementos da tupla :{len(tupla)}')


#    Concatenação de tuplas
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
tupla2 = ("Charmander", "Bulbasauro", "Squirtle")
print(tupla2)

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2
print(tupla1)
#    As tuplas não foram alteradas após a soma. São imutaveis


#    Para verificar se determinado elemnto está na tupla :
tupla = ("Lucario", "Gengar", "Rayquaza", "Swampert", "Kartana", "Hydragon")

print("Gengar" in tupla)


#    Iterando sobre uma tupla :
tupla = ("Lucario", "Gengar", "Rayquaza", "Swampert", "Kartana", "Hydragon")

for n in tupla:
    print(n)


for indice, valor in enumerate(tupla):
    print(indice, valor)


#    Contando elementos dentro de uma tupla
tupla = ("Mario", "Zelda", "Pokemon", "chrono trigger")

print(tupla.count("Mario"))

nome = tuple("Viniswitch")
print(nome)
print(nome.count("i"))


#    Devemos ultilizar tuplas sempre que não formos querer que os elementos sejam alterados, Exp.:
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
#       (    0           1          2        3        4       5        6         7          8          9          10           11   )
print(meses)

#    O acesso a elementos em uma tupla, também é semelhante ao de uma lsita
print(meses[7])


#    Iterar com o while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1


#    Para verificar em qual indice o elemento está na tupla
print(meses.index("Agosto"))


#    Slicing :
#    -tupla[inicio:fim:passo]
print(meses[1:11:2])
print(meses[0:8:1])


#    Copiando uma tupla para outra
tupla = (8, 7, 6, 5, 4, 3, 2, 1)
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = (0, -1, -2, -3, -4, -5, -6)
nova = nova + outra
print(nova)
print(tupla)

#    Na tupla não temos Shallow Copy








