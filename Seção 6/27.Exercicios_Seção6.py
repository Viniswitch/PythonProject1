"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
n4 = int(input("Digite o quarto valor: "))
n5 = int(input("Digite o quinto valor: "))
n6 = int(input("Digite o sexto valor: "))

lista = [n1, n2, n3, n4, n5, n6]
print(f"A Lista é : {lista}")



2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:
a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha.


A = [1, 0, 5, -2, -5, 7]
print(f'A Lista "A" é : {A}')
soma = int(A[0] + A[1] + A[5])
print(f'A soma da lista "A" é :{soma}')

A.pop(5)
A.insert(5, 100)
print(f'Trocando o quinto elemento da lista "A" para o valor "100" : {A}')
for elemento in A:
    print(f' Cada elemento da lista "A" é : {elemento}')



3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
n4 = int(input("Digite o quarto valor: "))
n5 = int(input("Digite o quinto valor: "))
n6 = int(input("Digite o sexto valor: "))
n7 = int(input("Digite o setimo valor: "))
n8 = int(input("Digite o oitavo valor: "))
n9 = int(input("Digite o nono valor: "))
n10 = int(input("Digite o decimo valor: "))
lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
print(lista)
soma =[]
for elemento in lista:
    if elemento % 2 == 0:
        soma.append(elemento)
print(sum(soma))
"""

#    Correção

#    Exercicio 1
lista : list[int] = []

while len(lista) < 6:
    valor : int = int(input(f"Informe o valor{len(lista) + 1}/6: "))
    lista.append(valor)

for valor in lista:
    print(valor)


#    Exercicio 2
A : list[int] = [1, 0, 5, -2, -5, 7]

soma : int = A[0] + A[1] + A[5]
print(f'A soma dos valores é {soma}')

A[5] = 100

for valor in A:
    print(valor)


#    Exercicio 3
lista : list[int] = []

contador_pares : int = 0

while len(lista) < 10:
    valor = int(input(f"Informe o valor {len(lista) + 1}/10: "))
    lista.append(valor)

    if valor % 2 == 0:
        contador_pares += 1

if contador_pares > 0:
    print(f"A lista {lista} possui {contador_pares} valores pares. ")
else:
    print(f"A lista {lista} não possui valor par. ")
