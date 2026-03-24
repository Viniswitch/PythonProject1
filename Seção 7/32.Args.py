"""
 - args : É um parametro de entrada, como qualquer outro parametro. Isso significa que, você poderá chamar de
 qualquer coisa, desde de que comece com asterisco

 - OBS : poderiamos usar "*xis", mas por convenção, ultilizamos "*args" para defini-lo

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

print(somar(3.14, 5, 6))

def soma2(nome, email, *args):
    return sum(args)

print(soma2("Viniswitch", "@Gmail", 1.42, 1.73, 3.14))


#    Exemplo 3 com o "args"

def verifica_info(*args):
    if "Vini" in args and "Switch" in args:
        return "Olá ViniSwitch"
    return "Como é, amigo ?"

print(verifica_info())
print(verifica_info(1, True, "Vini"))
print(verifica_info(2,"Switch", False, "Vini"))
print(verifica_info(3, False, "Switch", 3.14))


#    Exemplo 4 : Desempacotando uma lista em um args

def soma3(*args):
    return sum(args)

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla1 = (11, 12, 13, 14, 15)
set1 = {16, 17, 18, 19, 20, 21}

#    print(soma3(lista)) Assim gera erro

print(soma3(*lista1))#    O "*" vai desempacotar a lista
print(soma3(*tupla1))
print(soma3(*set1))
#    Não funciona em dicts







