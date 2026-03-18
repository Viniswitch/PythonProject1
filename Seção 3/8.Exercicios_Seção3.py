"""
1.Faça um programa que leia um número primo e imprima-o

2.Faça um programa que peça para o usuário digitar 3 valolores inteiros e imprima a soma deles

3.Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos

"""

#    Exercicio 1 :

numero : int = int (input ("Digite 1 Número inteiro") )
print(int(numero))


#    Exercicio 2 :

soma = input("Digite 3 valores inteiros")
print(soma.split())
print(int(soma.split()[0]) + int(soma.split()[1]) + int(soma.split()[2]))

#    Exercicio 2:

soma1 : int = int (input ("Digite 1 valor"))
soma2 : int = int (input ("Digite 2 valor"))
soma3 : int = int (input ("Digite 3 valor"))
print(soma1 + soma2 + soma3)

#    Exercicio 3 :

soma = input("Digite 3 valores inteiros")
print(int(soma.split()[0])**2 + int(soma.split()[1])**2 + int(soma.split()[2])**2)

#    Exercicio 3 :
soma1 : int = int (input ("Digite 1 valor"))
soma2 : int = int (input ("Digite 2 valor"))
soma3 : int = int (input ("Digite 3 valor"))
print(soma1**2 + soma2**2 + soma3**2)
