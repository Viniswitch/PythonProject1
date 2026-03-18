#    🔹 4. LISTAS

#    🟢 Fácil

#    1. Crie uma lista com 5 números e mostre a soma.
print("#    1. Crie uma lista com 5 números e mostre a soma.")
lista = [1, 2, 3, 4, 5]
print(lista)
print(sum(lista))

#    2. Mostre o maior e o menor valor da lista.
print("#    2. Mostre o maior e o menor valor da lista.")
lista1 = [1, 2, 3, 4, 5]
print(lista1)
print(max(lista1))
print(min(lista1))

#    3. Conte quantos elementos existem.
print("#    3. Conte quantos elementos existem.")
lista2 = [1, 2, 3, 4, 5]
print(lista2)
print(len(lista2))

#    🟡 Médio

#    4. Leia 10 números e armazene em uma lista.
print("#    4. Leia 10 números e armazene em uma lista.")
lista3 =[]
for numero in range(1, 11):
    lista3.append(int(input(f"Digite o numero {len(lista3) + 1}/10: ")))
print(lista3)

#    5. Separe os números pares e ímpares em duas listas.
print("#    5. Separe os números pares e ímpares em duas listas.")
lista4 =[]
impar = []
par = []
for numero in range(10):
    n =(int(input(f"Digite o numero {len(lista4) + 1}/10: ")))
    lista4.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(lista4)
print(par)
print(impar)

#    6. Inverta uma lista.
print("#    6. Inverta uma lista.")
lista5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lista5)
print(lista5[::-1])

#    🔴 Difícil

#    7. Remova valores duplicados de uma lista.
print("#    7. Remova valores duplicados de uma lista.")
lista1 = [1, 2, 1, 5, 3, 4, 1, 3, 4, 5]
print(list(set(lista1)))

#    8. Ordene uma lista sem usar `sort()`.]
print("#    8. Ordene uma lista sem usar `sort()`.")
lista6 = [0, 1, 2, 1, 5, 3, 4, 1, 3, 4, 5]
print(lista6)

for a1 in range(len(lista6)):
    for a2 in range(a1+1, len(lista6)):
        if lista6[a1] > lista6[a2]:
            lista6[a1], lista6[a2] = lista6[a2], lista6[a1]
print(lista6)

#    9. Encontre o segundo maior número da lista.
print("#    9. Encontre o segundo maior número da lista.")
lista7 = [0, 1, 2, 1, 5, 3, 4, 1, 3, 4, 5]

lista7 = list(set(lista7))
lista7.sort()
print(lista7)
print(lista7[-2])




























