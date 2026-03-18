"""
- Escopo de Variaveis
1.Variaveis Globais:
-Variaveis globais são reconhecidas, ou seja, seu escopo coomprende, todo o programa.

2.Variaveis Locais:
-Variaveis locais são reconhecidas, apenas, no bloco onde foram decladas, ou seja, seu escopo
está limitado ao bloco onde foi declarada.

- Para declarar uma variavel em Python fazemos:
nome_da_variavel = valor_da_variavel

- Python é uma linguagem de tipagem dinânima. Isso significa que, ao declararmos
uma variavel, nós não colocamos o tipo de dado dela. Este tipo é inferido ao
atribuirmos o valor à mesma

Exp. em C:
int numero = 42

Exp.: em Java:
int numero = 42
"""

#    Exemplo de variavel global
numero = 42
print(numero)
print(type(numero))

numero = 'Viniswitch'
print(numero)
print(type(numero))

#    Exemplo de variavel local, onde a variavel novo está declarada localmente dentro do blco if
numero = 2
#novo = 0
if numero > 10:
    novo = numero + 10
    print(novo)

#    Se, print(novo), fora do bloco, irá ocorrer um erro
