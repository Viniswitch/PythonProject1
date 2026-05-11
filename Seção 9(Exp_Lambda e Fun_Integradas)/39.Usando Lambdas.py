"""
 - Ultilizando Lambdas : Conhecidas por expressões lambdas ou, simplesmente, lambdas, são funções sem nome, ou seja
 funções anonimas

'''
#    Função em Python :
def funcao(x):
    return 3 * x + 1

print(funcao(7))


#    Exemplo de função Lambda :
lambda x: 3 * x + 1

#    Como ultilizar a expressão lambda :
calculo = lambda x: 3 * x + 1
print(calculo(7))
'''


"""


#    Função em Python :
def funcao(x):
    return 3 * x + 1

print(funcao(7))


#    Exemplo de função Lambda :
#lambda x: 3 * x + 1

#    Como ultilizar a expressão lambda :
calculo = lambda x: 3 * x + 1
print(calculo(7))


#    Podemos ter expressões lambdas com multiplas entradas :
'''
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
print(nome_completo(nome, sobrenome))
print(nome_completo("wells", "404"))
'''

#    Em funções python, podemos ter nenhuma ou varias entradas. Em lambda tambem
sla = lambda : 'Como sla de python'

uma = lambda x: 3 * x + 1

duas = lambda x, y : (x * y) ** 1.5

tres = lambda x, y, z : 3 / (1 / x + 1 / y + 1 / z)

#n = lambda x1, x2, ..., xn : <expressão>

print(sla())
print(uma(6))
print(duas(6, 7))
print(tres(2, 2, 2))

#    OBS : Se passarmos mais argumentos do que parametros esperados, teremos erro


#    Outro Exemplo :
autores = ["Tolkien", "C. S. Lewis", "Chesterton", "Arthur Conan Doyle", "Brandon Sanderson", "George Orwel"]

print(autores)

autores.sort(key = lambda sobrenome : sobrenome.split(" ")[-1].lower())

print(autores)



#    Função Quadratica : F(x) = aX**2 + bX + c

#    Definindo a função :
def funcao_quaratica(a, b, c):
    return lambda x: a * (x ** 2) + b * x + c

teste = funcao_quaratica(3, 4, -5)
print(teste(0))
print(teste(1))

