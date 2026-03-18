# 📘 LISTA DE EXERCÍCIOS – LISTAS (FOCO NAS SUAS FALHAS)
"""
# 🔹 🟡 NÍVEL MÉDIO (correção de base)
print("#    Questão 1")
#    1. Leia 10 números e:
lista1 = []
for _ in range(10):
    numero = int(input(f'Digite o numero {len(lista1)+1}/10 : '))
    lista1.append(numero)

#    1.1 armazene em uma lista
print(lista1)

#    1.2 mostre apenas os números pares
pares = []
for numero in lista1:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

print("#    Questão 2")
#    2.Leia 10 números e:
lista2 = []
for _ in range(10):
    numero2 = int(input(f'Digite o numero {len(lista2)+1}/10 : '))
    lista2.append(numero2)

#    2.1 armazene em uma lista
print(lista2)

#    2.2 mostre apenas os números maiores que 10
dez = []
for numero2 in lista2:
    if numero2 > 10:
        dez.append(numero2)
print(dez)



print("#    Questão 3")
#    3.Leia 10 números e:
lista3 = []
for _ in range(10):
    numero3 = int(input(f'Digite o numero {len(lista3)+1}/10 : '))
    lista3.append(numero3)

#    3.1 conte quantos são positivos
positivo = []
for numero3 in lista3:
    if numero3 > 0:
        positivo.append(numero3)
print(f'Existem {len(positivo)} numeros positivos')

#    3.2 conte quantos são negativos
negativo = []
for numero3 in lista3:
    if numero3 < 0:
        negativo.append(numero3)
print(f'Existem {len(negativo)} numeros negativos')


#    4.Leia 10 números e crie uma lista com os números multiplicados por 2
print("#    Questão 4")
lista4 = []
for _ in range(10):
    numero4 = int(input(f'Digite o numero {len(lista4)+1}/10 : '))
    lista4.append(numero4 *2 )
print(lista4)

#    5.Leia 10 números e:
print("#    Questão 5")
lista5 = []
for _ in range(10):
    numero5 = int(input(f'Digite o numero {len(lista5)+1}/10 : '))
    lista5.append(numero5)

#    5.1 mostre o maior valor
maximo = max(lista5)
print(maximo)

#    5.2 mostre em qual posição ele apareceu
print(f'O numero {maximo} apareceu na posição : {lista5.index(maximo) + 1}/10')


#    🔹 🟠 NÍVEL MÉDIO–DIFÍCIL

#    6.Leia 10 números e separe em duas listas: pares e ímpares
print("#    Questão 6")
lista6 = []
par6 = []
impar6 = []
for _ in range(10):
    numero6 = int(input(f'Digite o numero {len(lista6)+1}/10 : '))
    if numero6 % 2 == 0:
        par6.append(numero6)
    else:
        impar6.append(numero6)
print(par6)
print(impar6)


#    7.Leia 10 números e remova os valores repetidos **sem usar set**
print("#    Questão 7")
lista7 = []
for _ in range(10):
    numero7 = int(input(f'Digite o numero {len(lista7)+1}/10 : '))
    lista7.append(numero7)
    for a1 in range(len(lista7)):
        for a2 in range(a1 +1, len(lista7)):
            if lista7[a1] > lista7[a2]:
                lista7[a1], lista7[a2] = lista7[a2], lista7[a1]
nova = []
for n in lista7:
    if n not in nova:
        nova.append(n)

print(nova)
print(lista7)

#    8.Leia 10 números e mostre a soma apenas dos números pares
print("#    Questão 8")
lista8 = []
par8 = []
for _ in range(10):
    numero8 = int(input(f'Digite o numero {len(lista8)+1}/10 : '))
    lista8.append(numero8)
for numero in lista8:
    if numero % 2 == 0:
        par8.append(numero)
print(f'A soma dos pares é : {sum(par8)}')

#    9.Leia 10 números e substitua todos os números negativos por 0
print("#    Questão 9")
lista9 = []
for _ in range(10):
    numero9 = int(input(f'Digite o numero {len(lista9)+1}/10 : '))
    lista9.append(numero9)
    for i in range(len(lista9)):
        if lista9[i] < 0:
        lista9[i] = 0
print(lista9)

#    10.Leia 10 números e conte quantas vezes cada número aparece (sem `Counter`)
print("#    Questão 10")
lista10 = []
for _ in range(10):
    numero10 = int(input(f'Digite o numero {len(lista10)+1}/10 : '))
    lista10.append(numero10)

contagem = {}
for num in lista10:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1
print(contagem)



# 🔹 🔴 NÍVEL DIFÍCIL


#    11. (ordenação manual): Leia uma lista e ordene ela sem usar `sort()`
print("#    Questão 11")
lista11 = []
for _ in range(10):
    numero11 = int(input(f'Digite o numero {len(lista11)+1}/10 : '))
    lista11.append(numero11)
    for a1 in range(len(lista11)):
        for a2 in range(a1 + 1, len(lista11)):
            if lista11[a1] > lista11[a2]:
               lista11[a1], lista11[a2] = lista11[a2], lista11[a1]
print(lista11)


#    12. (segundo maior): Leia uma lista e encontre o segundo maior número, sem usar:`sort()` e/ou `set()`
print("#    Questão 12")
lista12 = []
for _ in range(10):
    numero12 = int(input(f'Digite o numero {len(lista12)+1}/10 : '))
    lista12.append(numero12)
    for a1 in range(len(lista12)):
        for a2 in range(a1 + 1, len(lista12)):
            if lista12[a1] > lista12[a2]:
                lista12[a1], lista12[a2] = lista12[a2], lista12[a1]
print(lista12)
print(lista12[8])

#    13. (inversão manual): Inverta uma lista, sem usar `[::-1]` ou `reverse()`
lista13 = []
for _ in range(5):
    numero13 = int(input(f'Digite o numero {len(lista13)+1}/5 : '))
    lista13.append(numero13)
    for a1 in range(len(lista13)):
        for a2 in range(a1 + 1, len(lista13)):
            if lista13[a1] > lista13[a2]:
                lista13[a1], lista13[a2] = lista13[a2], lista13[a1]

from collections import deque
deq = deque()

for num in lista13:
    deq.appendleft(num)
print(deq)
"""
#    14. (maior sequência): Dada uma lista, encontre: o maior número de repetições consecutivas. Ex:[1,1,2,2,2,3] → resposta: 3
lista14= str(input("Digite uma lista: "))
lista14= lista14.split()

contagem = {}
for num in lista14:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1
for chave, receita in contagem.items():
    print(f'Valor da lista : "{chave}" / {contagem[chave]}X')

#    15. (remoção seletiva): Leia uma lista e: remova todos os números que aparecem mais de uma vez. Ex:[1,2,2,3,4,4] → [1,3]



# 🔹 🔥 NÍVEL PROVA (onde você evolui de verdade)


#    16.Leia uma lista e crie outra lista contendo apenas os valores únicos, mantendo a ordem original


#    17.Leia uma lista e encontre o elemento mais frequente (sem `Counter`)


#    18.Leia duas listas e crie uma terceira com elementos em comum


#    19.Leia uma lista e verifique se ela está ordenada


#    20.Leia uma lista e rotacione ela para a direita. Ex:[1,2,3,4] → [4,1,2,3]
