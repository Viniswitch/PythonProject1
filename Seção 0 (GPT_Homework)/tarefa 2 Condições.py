#    🔹 2. CONDIÇÕES (if, elif, else)


#    🟢 Fácil

#    1. Leia um número e diga se é positivo ou negativo.
num = float(input("Digite um numero qualquer: "))
if num >= 0:
    print("É positivo")
else:
    print("É negativo")

#    2. Leia a idade e diga se é maior de idade.
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("É maior de idade")
else:
    print("É menor de idade")

#    3. Leia dois números e diga qual é maior.
num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

if num1 > num2:
    print(f'O numero "{num1}" é maior que o numero "{num2}"')
else:
    print(f'O numero "{num2}" é maior que o numero "{num1}"')


#    🟡 Médio

#    4. Leia três números e mostre o maior.
lista = []
while len(lista) < 3:
    lista.append(int(input(f"Insira o valor {len(lista)}/3 :")))
print(max(lista))

#    5. Leia um número e diga se é par ou ímpar.
num = int(input("Digite um numero inteiro: "))
if num % 2 == 0:
    print("É par")
else:
    print("É impar")

#    6. Leia a nota de um aluno e diga se está aprovado (≥7), recuperação (5–6.9) ou reprovado.
nota = int(input("Digite sua nota: "))
if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")


#    🔴 Difícil

#    7. Simule um sistema de login (usuário e senha).
usuario_correto = "Viniswitch"
senha_correta = "12345"

usuario_inserido = input("Digite o usuario: ")

if usuario_correto == usuario_inserido:
    print(f"Bem-vindo usuario {usuario_correto}!")
else:
    print(f'O usuario "{usuario_inserido}" não foi identificado')

senha_inserida = input("Digite sua senha: ")

if senha_correta == senha_inserida:
    print("Sua senha está correta")
else:
    print("Sua senha está incorreta")

#    8. Leia um ano e diga se é bissexto.
ano = int(input("Digite o ano: "))
if ano % 4 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print("O ano não é bissexto")

#    9. Crie um programa que calcule o IMC e classifique o resultado.
peso = float(input("Digite o peso em quilos: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura
print(f'Seu IMC é de {imc}')
if imc >= 30:
    print("Você está a cima do peso ideal")
elif imc < 16:
    print("Você está desnutrido")
else:
    print("Você está normal")


