"""
 - args : É um parametro de entrada, como qualquer outro parametro. Isso significa que, você poderá chamar de
 qualquer coisa, desde de que comece com asterisco

 - Exemplo : poderiamos usar "*xis", mas por convenção, ultilizamos "*args" para defini-lo

 - O'que é "*args" ?
 1.O parametro *args ultilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Emtão
 desde já, lembre-se que tuplas são imutaveis

def somar(*args):
    return sum(args)

print(soma(4, 5, 6))

"""

#    Exemplo sem o "*args"
def soma(num1 = 0, num2 = 0, num3 = 0):
    return num1 + num2 + num3

print(soma(4, 5))
print(soma(4, 5, 6))


#    Exemplo 1 com o "*args"
def soma(*args):
    print(args)
    total = 0
    for num in args:
        total = total + num
    return total

print(soma(4, 5, 6))


#    Exemplo 2 com o "*args"
def somar(*args):
    return sum(args)

print(somar(4, 5, 6))





