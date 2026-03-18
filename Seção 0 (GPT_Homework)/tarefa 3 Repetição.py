#    🔹 3. LAÇOS DE REPETIÇÃO (for, while)

#    🟢 Fácil

#    1. Mostre os números de 1 a 10 usando `for`.
for numero in range(1, 11):
    print(numero)

#    2. Mostre os números pares de 1 a 20.
for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)

#    3. Some os números de 1 a 100.
lista = []
for numero in range(1, 101):
    lista.append(numero)
print(sum(lista))



#    🟡 Médio

#    4. Peça números até o usuário digitar 0 e mostre a soma.]
lista = []
num = int(input("Digite um numero inteiro: "))
lista.append(num)
while num != 0:
    num = int(input("Digite um numero inteiro: "))
    lista.append(num)
print(sum(lista))

#    5. Mostre a tabuada de um número usando `for`.
num = int(input("Digite um numero inteiro para mostrar a tabuada: "))
for numero in range(1, 11):
    saida = numero * num
    print(saida)

#    6. Conte quantos números pares foram digitados (até o usuário parar)

lista = []
while True:
    num = int(input("Digite um numero inteiro ou digite 0 para sair: "))
    if num % 2 == 0:
        lista.append(num)
    if num == 0:
        break
print(len(lista) - 1)


#    🔴 Difícil

#    7. Gere os 10 primeiros números da sequência de Fibonacci.
#Não sei fazer

#    8. Peça vários números e mostre o maior e o menor.
lista = []
loop = True
while loop:
    num = int(input("Digite um numero inteiro ou digite 0 para sair: "))
    lista.append(num)
    if num == 0:
        loop = False
lista.remove(0)
print(max(lista))
print(min(lista))

#    9. Simule um jogo onde o usuário tenta adivinhar um número.
numero = int(input("Em qual numero, entre 1 e 10, eu estou pensando ?: "))


from random import random
def aleatorio():
    valor = random()
    if valor < 0.1:
        return 1
    elif valor < 0.2:
        return 2
    elif valor < 0.3:
        return 3
    elif valor < 0.4:
        return 4
    elif valor < 0.5:
        return 5
    elif valor < 0.6:
        return 6
    elif valor < 0.7:
        return 7
    elif valor < 0.8:
        return 8
    elif valor < 0.9:
        return 9
    else:
        return 10

if aleatorio() == numero:
    print(f'Parabens você acertou o numero que eu estava pensando')
else:
    print("Errou")




