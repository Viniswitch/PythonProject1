"""
 - Conjuntos : Em qualquer linguagem de programação, é uma replica da teoria dos conjuntos em matematica. No
 Python, os conjuntos são chamdos de "sets". Dito isso, da mesma forma que na matematica :

    1.Sets não possuem valores duplicados
    2.Sets não possuem valores ordenados
    3.Elementos não são acessados via indice, ou seja, conjuntos não são indexados

 - Conjuntos(Sets) são bons para armazenar elementos, mas quando não nos importamos com a ordenação deles.Quando
 não precisamos nos preocupar com chaves, valores ou itens duplicados

 - Em Python, os sets são referenciados por "{}" chaves
     Diferença entre conjuntos e mapas/dicionarios em Python :
     1.Dicionario possui (chave : valor)
     2.Um conjunto possui apenas (valor)
"""

#    Assim como todo outro conjunto Python, em sets, podemos colocar varios tipos de dados misturados
s = {1, "b", True, 3.14}
print(s)
print(type(s))


#    Definindo um conjunto :

#    Forma 1 :

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #    Repare que temos valores repetidos
print("s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})")
print(s)
print(type(s))
print("Observe que ele não repete valores iguais")


#    Forma 2 : (Mais Comum)

s = {1, 2, 2, 3, 4, 5, 5}
print("print(s)")
print(s)
print("print(type(s))")
print(type(s))


#    transformando outros objetos em conjunto
lista = [1, 2, 3, 4, 5, 5, 6, 3, 2, 3]
print(f"lista ={lista}")
s = set(lista)
print(f"set ={s}")


#    Determinando se um elemento está no set
if 3 in s:
    print("3 está em s")
else:
    print("Não tem 3 em s")


#    Exemplificando a questão da ordem :
dados = (1, 2, 3, 4, 5, 5, 6, 3, 2, 3)

lista = list(dados)
print(f"lista ={lista} com {len(lista)} elementos")
#    listas aceitam valore duplicados, então temos 10 elementos

tupla = tuple(dados)
print(f"tupla = {tupla} com {len(tupla)} elementos")
#    tuplas aceitam valores duplicados, então temos 1o elementos

dicionario = {}.fromkeys(dados, "d")
print(f"dicionario = {dicionario} com {len(dicionario)} elementos")
#    dicionarios não aceitam chaves duplicadas, então temos 6 elementos

conjuntos = set(dados)
print(f"sets ={conjuntos} com {len(conjuntos)} elementos")
#    conjuntos não aceitam valores duplicados, então temos 6 elementos


#    Podemos, normalmente, iterar em um set
s = {1, "b", True, 3.14}
print(s)
for valor in s:
    print(valor)


#    Usos interessantes com sets :
''' Imagine que você está fazendo um formulario de cadastros de pessoas em um museu e os visitantes informam
manualmente de onde vieram. Nós adicionamos cada cidade em uma lista Python, já que em um lista podemos adicionar
novos elementos e ter repetição'''
cadastros = ["Recife", "Vitoria", "Gravata", "Bezerros", "Caruaru", "Recife", "Caruaru","Recife","Vitoria","Bezerros",
           "Gravata", "Recife"]
print(cadastros)
print(f"Nós temos um total de {len(cadastros)} cadastros no sistema")#    Para saber a quantidade de pessoas que vieram, no total

#    E se precisarmos saber quantas cidades distintas(diferentes) temos ? Nós usaremos os sets:
print(f"Nós temos {len(set(cadastros))} cidades diferentes")


#    Adicionando elementos em um conjunto
s = {1, 2, 3, 4, 5}
s.add(6)
print(s)


#    Removendo elementos em conjuntos :

#    Forma 1
s.remove(1)#    Não é indice, informamos o valor a ser removido. Se não houver o valor haverá erro
print(s)

#    Forma 2
s.discard(2)#    Nessa forma, não haverá erro caso o valor a ser removido não estiver no conjunto
print(s)


#    Copiando um conjunto para outro

#    Deep Copy
print(" - Exemplo do Deep Copy :")
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s)
novo = s.copy()

novo.add(11)
print(novo)
print(s)

#    Shallow Copy
print(" - Exemplo do Shallow Copy :")
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s)

novo = s
novo.add(0)
print(novo)
print(s)


#    Metodos matematicos de conjuntos
'''Imagine que temos 2 conjuntos, 1 contendo os estudantes do curso de ciencias e 1 contendo  osestudantes
do curso de engenharia'''

estudantes_ciencias = {"Viniswitch", "Borba", "Chico", "Bento", "Gabriel", "Leticia"}
estudantes_engenharia = {"Leticia", "Aluisio", "Thiago", "Freefire", "Chico"}

#    Se precisarmos gerar um conjunto com nomes unicos ?
print(" - Unindo conjuntos :")
print(estudantes_ciencias)
print(estudantes_engenharia)

#    Forma 1 : usando o "union"
print(' - Forma 1 : Ultilizando o "union"')
unicos1 = estudantes_ciencias.union(estudantes_engenharia)
print(unicos1)

#    Forma 2 : ultilizando o caractere "pipe" "|"
print(' - Forma 2 : Ultilizando o "|" :')
unicos2 = estudantes_ciencias | estudantes_engenharia
print(unicos2)


#    Se precisarmos gerar um conjunto com os estudantes que estão em ambos os conjuntos
print(' - Gerando a interseção dos conjuntos :')

#    Forma 1 : Ultilizando "intersection"
print(' - Forma 1 : Usando o "intersection" :')
intersecao1 = estudantes_ciencias.intersection(estudantes_engenharia)
print(intersecao1)

#    Forma 2 : Ultilizando o "&"
print(' - Forma 2 : Usando o "&" :')
intercecao2 = estudantes_ciencias & estudantes_engenharia
print(intercecao2)


#    Se precisarmos gerar um conjunto de estudantes que estão emapenas 1 curso?
ciencias = estudantes_ciencias.difference(estudantes_engenharia)
print(ciencias)

engenharia = estudantes_engenharia.difference(estudantes_ciencias)
print(engenharia)


#    Soma, valor maximo, valor minimo e tamanho (Se os valores forem int ou float)

s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s)
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
