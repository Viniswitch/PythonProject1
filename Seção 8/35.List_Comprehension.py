"""
 - List Comprehension : Nós podemos gerar novas listas com dados procesados a partir de outro iteravel

#    Sintaxe da List Comprehension :
[dado for dado in iteravel]

"""

#    Exemplo 1 :

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [numero * 10 for numero in numeros]

print(res)


#    Exemplo 2 :

res = [numero / 2 for numero in numeros]
print(res)


#    Exemplo 3 :

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]

print(res)


#    List Comprehension VS Loop :

#    Usando o loop :
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

#    Usando List Comprehension :
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [numero * 2 for numero in numeros]

print(res)


#    Outros Exemplos :

#    Exemplo 1 :
nome = 'Viniswitch'

print([letra.upper() for letra in nome])


#    Exemplo 2 :
cachorros = ['Açucar', 'Xubaca', 'Zelda', 'Pumba']

print([cachorro_nome.upper() for cachorro_nome in cachorros])

print([cachorro_nome[0].upper() for cachorro_nome in cachorros])

def cachorro_nomezao(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome
print([cachorro_nomezao(nome) for nome in cachorros])


#    Exemplo 3 :
print([numero * 3 for numero in range(1, 10)])


#    Exemplo 4 ;
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])


#    Exemplo 5 :
print([str(numero) for numero in range(1, 10)])




#    - List Comprehension Pt. 2 :
"""
 - List Comprehension Pt. 2 : 
 Nós podemos adicionar estruturas condicionais logicas as nossas list comprehensions
"""

#    Exemplo 1 :
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numeros for numeros in lista if numeros % 2 == 0]
impares = [numeros for numeros in lista if numeros % 2 != 0]

print(pares)
print(impares)

#    Refatoração
pares = [numeros for numeros in lista if not numeros % 2 == 0]
impares = [numeros for numeros in lista if numeros % 2 == 0]

print(pares)
print(impares)


#    Exemplo 3 :
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in lista]
print(res)







