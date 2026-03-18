# 🔹 1. FUNDAMENTOS (variáveis, entrada e saída)


#    🟢 Fácil

#    1. Leia dois números e mostre a soma.
num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
print(num1 + num2)

#    2. Leia o nome e a idade de uma pessoa e mostre uma mensagem formatada.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"{nome} tem {idade} anos")

#    3. Leia um número e mostre seu dobro, triplo e raiz quadrada.
num1 = int(input("Digite um numero inteiro: "))
print(num1 * 2)
print(num1 * 3)
print(num1 ** (1/2))


#   🟡 Médio

#    4. Leia um valor em metros e converta para centímetros e milímetros.
centimetro = int(input("Digite o valor em milimetros: "))
print(f"{centimetro / 100} metros")

#    5. Leia um número e mostre a sua tabuada até 10.
num = int(input("Digite um numero inteiro: "))
for numero in range(1, 11):
    print(num * numero)

#    6. Leia quanto dinheiro uma pessoa tem e mostre quantos dólares ela pode comprar (defina uma taxa fixa).
valor = float(input("Digite o valor possuido: "))
dolar = 5.24

print(f"{valor / dolar} dolares")


#    🔴 Difícil

#    7. Leia o salário de um funcionário e aplique um aumento de 15%.
salario = float(input("Digite o valor do salario: "))
print(f"O aumento de 15% resultou em {int(salario * 1.15)} reais")

#    8. Leia um preço e aplique um desconto de 10%.
preco = float(input("Digite o preço do produto: "))
print(f"O deconto de 10% resultou no valor : {int(preco * 0.9)} reais")

#    9. Crie um programa que leia 3 valores e mostre a média formatada.
lista = []
while len(lista) < 3:
    lista.append(int(input(f"Insira o valor {len(lista)}/3 :")))
print(f"A media é : {sum(lista)/3}")



