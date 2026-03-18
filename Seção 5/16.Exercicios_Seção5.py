"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.

2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando
em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.

3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).

"""

#    Exercicio 1

contador : int = 0
indice : int = 1

while contador < 5:
    if indice % 3 == 0:
        print(f"o numero {indice} é multiplo de 3")
        contador = contador + 1
    indice = indice + 1

# Exercicio 2

num = 10
while num != -1:
    print(num)
    num = num - 1
print("FIM")

#    Exercicio 3

num = int(input(f"digite um numero"))
for num in range(0, 101000, 1000):
    print(num)

