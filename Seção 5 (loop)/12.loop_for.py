"""
- loop : É uma estrurura de repetição

- for : É um dessas estruturas
#    for indice, letra in enumerate(name):
        print(name[indice])

#    Em C ou em Java :

for(int i = 0; i < 10; i++){
    //execuço do loop
}

#    Em Python :

for iten in interavel:
    //execução do loop


- Ultilizamos loops para iterar sobre sequencias ou sobre valores iteraveis
Exemplos de iteraveis :
-strings
    nome="Viniswitch"
-Lista
    {01, 02, 03, 04, 05, 06, 07, 08, 09, 010}
-range
    numeros = range(1, 10)

"""


nome = "Viniswitch"
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = range(1, 10) #    Temos que transformar em uma lista

for letra in nome:#    Exemplo de for 1 : iterando em uma string
    print(letra)

for numero in lista:#    Exemplo de for 2 : iterando sobre uma lista
    print(numero)

for numero in range(11, 21):#    Exemplo de for 3 : iterando sobre um range
    print(numero)


name = "Viniswitch"

qtd = int(input("Qual é a quantidade de vezes que o loop deve repetir ?"))
for n in range(1, qtd+1):
    print(f"Imprimindo {n} vezes")


qnt = int(input("Quantas vezes o loop deve repetir ?"))
soma = 0

for n in range(1, qnt+1):
    num = int(input(f"Informe o {n}/{qnt} valor"))
    soma = soma + num
print(f"A soma é {soma}")

name = "Viniswitch"#    Para deixar as letras separadas na mesma linha
for letra in name:
    print(letra, end='_')#    Para dixar a lista na mesma linha




