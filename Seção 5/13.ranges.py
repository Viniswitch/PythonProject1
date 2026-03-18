"""
#    Precisamos conhecer o loop for para saber o range
#    Para trabalhar com o loop for é necessario aprende o ranges

- ranges : São ultilizados para gerar sequencias numericas, não de forma aleatoria, mas sim de maneira especificada

#    Formas gerais:

range(valor_de_parada)#   Valor de parada não inclusive (inicio padrão 0, e passo de 1 em 1)



"""

#    Exemplo 1

for num in range(11):
    print(num)


#    Exemplo 2

for num in range(11, 16):#    (valor_de_inicio, valor_de_parada)
    print(num)


#    Exemplo 3

for num in range(5, 50, 5):#    (valor_de_inicio, valor_de_parada, passo especificado pelo usuario)
    print(num)


#    Exemplo 4 (Inversa)

for num in range(12, 1, -2):
    print(num)


#    Exemplo extra (Lista)
lista = list(range(40))
print(lista)