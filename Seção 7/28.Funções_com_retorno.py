"""
 - Funções com retorno :

 - Em Python, quando uma função não retorna nenhum valor, o retorno é "None"

 - Não precisamos, necessariamente, criar uma variavel para receber o retorno de uma função. Podemos passar
 a execução dessa função para outras funções

  - Funções Python que retoranm valores, devem retornar estes valores com a palavra reservada "return"

  - Observações sobre o "return": (ver exemplos 3)
  1.Ela finaliza a função
  2.Podemos ter em uma função diferentes "returns"
  3.Podemos em uma função, retornar qualquer tipo de dado, e até mesmo multiplos valores

"""


#    Exemplo 1 :
def quadrado_de_sete():
    print(7*7)

ret = quadrado_de_sete()
print(f"Retorno de {ret}")#    "None" não retorna nada


#    Refatorando esta função, para que ela retorne um valor
def quadrado_de_sete():
    return 7 * 7

#    Criamos uma variavel para receber o retorno da função
ret = quadrado_de_sete()
print(f"Retorno de {ret}")

print(f"Retorno de {quadrado_de_sete()}")#    Forma mais direta, do que ultilizando a variavel "ret"
print(f"Retorno de {quadrado_de_sete() + 32}")


#    Exemplo 2
def diz_oi():
    return "Hello "

nome = "Viniswitch"

print(diz_oi() + nome)


#    Exemplo 3.1 : return
def diz_oi():
    return "Hello "
#   print("Estou sendo executado após o retorno")#    Nada é executado depois do "return"

print(diz_oi())


#    Exemplo 3.2 : Para testar funções com mais de um "return"
def nova_funcao():
    variavel = None#    Modifique a variavel para verificar os "return"
    if variavel:
        return 4
    elif variavel is None :
        return 3.2
    return "b"

print(nova_funcao())


#    Exemplo 3.3
def another_funcion():
    return 1, 2, 3, 4, 5

num1, num2, num3, num4, num5 = another_funcion()
#    print(num1, num2, num3, num4, num5)#    Desempacotando a tupla

print(another_funcion())#    Vira uma tupla
print(type(another_funcion()))


#    Vamos criar uma função para jogar uma moeda
#    importando a função random
from random import random

def joga_moeda():
    valor = random()#    ultilizando a função importada, que gera um numero pseudo-randomico entre 0 e 1
    if valor > 0.5:
        return "cara"
    return "coroa"


#    Exemplo de codificação desnecessaria :
def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:#    Não precisamos de else
        return False

print(eh_impar())

