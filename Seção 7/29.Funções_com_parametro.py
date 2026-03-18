"""
 - Funções com parametro : Funções que recebem dados, para serem processados dentro dela mesma

 - Se nós pensarmos em um programa qualquer, temos :
   Entrada -> Processamento -> Saída

 - Se nós pensarmos em uma função qualquer, sabemos que temos funções que:
 1.Não possuem entrada
 2.Não possuem saída(a não ser que, usemos "return")
 3.Possuem entrada, mas não possuem saída
 4.Não possuem entrada, mas possuem saída
 5.Possuem entrada e saída

"""


#    Refatorando uma função 1
def quadrado_de_sete():
    return 7 * 7

print(quadrado_de_sete())
print(quadrado_de_sete())
print(quadrado_de_sete())

def quadrado(numero):
    return numero * numero

print(quadrado(6))
print(quadrado(5))
print(quadrado(4))


#    Refatorando uma função 2
def cantar_parabens(aniversariante):
    print("Parabens pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print(f"Viva {aniversariante}!")

cantar_parabens("Viniswitch")


""" - Funções podem ter n parametros de entrada, ou seja, podemos receber como entrada em uma função
 quantos parametros forem necessarios. Sendo eles, sepados por virgula"""

#    Exemplo 1
def somar(a,b,c):
    return a+b+c

print(somar(32,64,128))
print(somar(9, 27, 81))

#    Exemplo 2
def multiplicar(num1,num2):
    return num1*num2

print(multiplicar(11,11))
print(multiplicar(12,12))

#    Exemplo 3
def sla (num1, b, msg):
    return (num1*b) * msg

print(sla(2,3,"(I walk a lonely road)_"))
print(sla(3,2,"(The only one i have ever known)_"))

#    Obs : Se informarmos um numero de parametro ou argumento errado, teremos erro. Exemplo :
#   def erro(a, b, c):    *Passando 3 argumentos
#       return(a + b + c)
#   print(erro(2, 3)    *Informando apenas 2 parametros


#    Nomeando parametros
def nome_completo(nome, sobrenome):
    return f"Seu nome é : {nome} {sobrenome}"

print(nome_completo("Vinicius", "Andrade"))


#    Diferença entre parametros e argumentos:

#    - Parametros são variaveis declaradas na definição de uma função
#    - Argumentos são dados passados durante a execução de uma função

#    - A ordem dos parametros importam, em quanto a dos argumentos não. Ex:
nome = "Black"
sobrenome = "Sabah"
print(nome_completo(sobrenome, nome))

#   -  Caso ultilizemos nomes dos parametros dentro do argumento para informa-los, a ordem não importa. Ex:
print(nome_completo(nome = "Iron", sobrenome = "Maiden"))
print(nome_completo(nome = nome, sobrenome = sobrenome))


#    Erro comum na ultilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))














