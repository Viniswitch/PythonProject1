"""
 - Funções com parametro padrão :

 - Funções onde a passagem de parametro seja opcional. Exp:]
 print()

 - Exemplo de função, onde a passagem de parametro seja obrigatoria
 def quadrado(numero):
    return numero ** 2

print(quadrado(3))#    Caso não informado o parametro, gera erro

"""

def exponencial(numero, potencia):
    return numero ** potencia

print(exponencial(2, 3))

def exponencial(numero = 2, potencia = 3):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3))
#    Se o usuario passar somente um argumento, esse valor será atribuido ao parametro "numero"

#    Os parametros com valor default devem sempre estar no final da função
def exponencial(numero, potencia = 3):
    return numero ** potencia
print(exponencial(2))

def exponencial(potencia, numero = 3):
    return numero ** potencia
print(exponencial(2))

'''
Porque ultilizar parametros com valor default ?
 - Nós permite ser mais flexivel nas funções
 - Evita erros com parametros incorretos
 - Nos permite trabalhar com exemplos mais legiveis de codigo
 #   Podemos ultilizar qualquer tipo de dado para valores default no parametro, como :
     - numeros, strings, floats, ints, booleanos, listas, tuplas, dict, def...
'''
#    Exemplo mais complexo :
def mostra_informacao(nome="Viniswitch", estudante = False):
    if nome == "Viniswitch" and estudante:
        return "Bem vindo estudante Viniswitch"
    elif nome == "Viniswitch":
        return "Eu pensei que você era o estudante"
    else:
        return f"Olá {nome}"

print(mostra_informacao())
print(mostra_informacao(estudante = True))
print(mostra_informacao("Ozzy"))
print(mostra_informacao(nome = "Osbourne"))
print(mostra_informacao(True))


#    Exemplo de função na função
def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def mat(num1, num2, funcao = soma):
    return funcao(num1, num2)

print(mat(2, 3))
print(mat(2, 3, subtracao))
print(mat(2, 3, soma))


'''
 Escopo : Evitar problemas e confusões :
- Variaveis globais
- Variaveis locais
'''

aluno = "Viniswitch"#    Variavel global

def diz_oi():
    aluno = "wells"#    Variavel local
    return f"oi {aluno}"
print(diz_oi())

def diz_oi():
    return f"Oi {aluno}"
print(diz_oi())

#    Se tivermos uma variavel local igual a uma variavel global, a variavel local terá preferencia
#    Cuidado com variaveis globais (evite ultilizar variaveis globais, se possivel)

#    Ultilizando uma variavel global igual a uma variavel local, sem gerar erro
total = 0

def incrementar():
    global total
    total = total + 1
    return total

print(incrementar())


#    Podemos ter funções que são declaradas dentro dde funções, também tem uma forma especial de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador#    Não é variavel global nem local, é a variavel da função anterior
        contador = contador + 1
        return contador
    return dentro()















