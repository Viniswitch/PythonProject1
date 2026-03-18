""""
1.Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.

3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

"""

#    Exercicio 1 :

num : int = int (input(f"Digite um numero inteiro:"))
num1 : int = int (input(f"Digite outro numero inteiro:"))
if num == num1:
    print("Os Números são iguais")
if num > num1:
    print(f"O primeiro número {num} é maior que o segundo {num1}")
if num < num1:
    print(f"O segundo número {num1} é maior que o primeiro {num}")


#    Exercicio 2:

num : int = int (input(f"Digite um numero inteiro:"))
if num > 0 :
    print(num ** 0.5)
else:
    print("O numero não possui raiz real")


#    Exercicio 3:

num : int = int (input(f"Digite um numero inteiro:"))
if num % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")
