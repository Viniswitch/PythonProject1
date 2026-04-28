"""
 - **Kwargs : Este é só mais um parametro, mas diferente do "*args" que coloca valores extras em uma tupla, o **Kwargs
 exige que ultilizemos valores numerados, e transforma esses parametros numerados extra em um Dict

- OBS : Poderiamos usar "**xis", mas por convenção, ultilizamos "**Kwargs" para defini-lo


 - Nas nossas funções, podemos ter (Nessa ordem) :
 1. Parametros obrigatorios :
 2. *args
 3. Parametros default (Não obrigatorios) :
 4. Kwargs

"""


#    Exemplo 1 :

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(leticia = "preto", vini = "verde", marcela = "azul")


#    Exemplo 2 :

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(leticia = "preto", vini = "verde", marcela = "azul")

#    Nem *args ou **Kwargs são obrigatorios


#    Exemplo 3 :

def cumprimento_especial(**kwargs):
    if "Vini" in kwargs and kwargs["Vini"] == "Switch":
        return "Você recebeu um cumprimento especial"
    elif "Vini" in kwargs:
        return f'{kwargs["Vini"]} Switch'
    return "Não sei quem é você"

print(cumprimento_especial())
print(cumprimento_especial(Vini = "Switch"))
print(cumprimento_especial(Vini = "Quem ?"))
print(cumprimento_especial(Vini = "especial"))


#    Exemplo 4 Ordem das paradas :

def minha_funcao(idade, nome, *args, depressao = True, **kwargs):
    print(f'O {nome} tem {idade} anos')
    print(args)
    if depressao:
        print("sim")
    else:
        print("não")
    print(kwargs)


minha_funcao(18, "Viniswitch")
minha_funcao(19, "Potter", 1, 2, 3, depressao = False)
minha_funcao(20, "Welzinho", eu = "não", voce = "vai")
minha_funcao(21, "Gabriela", 4, 5, 6, java = False, python = True)


#    Entendendo porque é importante manter a ordem dos parametros na declaração

#    Função com a ordem correta :
#    def mostra_info(a, b, *args, nome = "Viniswitch", **kwargs):

#    Função com a ordem errada
def mostra_info(a, b, nome = "Viniswitch", *args,  **kwargs):
    return [a, b, args, nome, kwargs]
'''
a =1
b = 2
args = 3
nome = "Viniswitch"
kwargs = {nickname = "Viniswitch" : cargo = "vagabundo"}

'''
print(mostra_info(1, 2, 3, nickname = "Viniswitch", cargo = "vagabundo"))


#    Desempacotar com o kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

nomes = {'nome' : 'thomas', 'sobrenome' : 'Shelby'}
print(mostra_nomes(**nomes))


#    Kwargs desempacotam dicionarios :
def soma_dict(a, b, c):
    print(a + b + c)

dicionario = dict(a =1, b = 2, c = 3)

soma_dict(**dicionario)

#    Os nomes das chaves devem ser iguais aos parametros da função
