"""
 - Definindo funções : São pequenoas partes de código, que realizam tarefas espécificas. Podendo ou não receber
 entrada de dados e, retornar uma saída de dados. Sendo muito úteis para executar procedimentos similares por
 repetidadas vezes.

 - Se você escrever uma função que realiza varias tarefas dentro dela, é bom fazer uma verificação para que a
 função seja simplificada

 #    DRY - Don't Repeat Yourself

 - Exemplos de funções básicas :
 - print()
 - len()
 - count()
 - min()
 - max()
"""


#    Exemplo de ultilização de funções :

cores = ["verde", "amarelo", "azul", "roxo"]

#    Ultilizando a função integrada do Python (Built-in) : print()
print(cores)

'''
 - Como definir funções: Em Python, a forma geral de definir uma função é :
   def nome_da_função(parametros_de_entrada):
       bloco_da_função

 - onde :
 - O nome da função deve estar sempre em letras minusculas, e se for nome composto, deve ser separado
 por snake case "_".
 - Parametros de entrada são opcionais, onde, tendo mais de um, cada um separado por virgula ",". Podendo
 ser opcionais ou não.
 - Bloco da função, tambem chamado de "corpo da função" ou "implementação", é onde o processamento da função
 acontece. Este bloco pode ter ou não retorno da função.
 
 OBS : Veja que, para definir uma função, ultilizamos a palavra reservada "def", informando ao Python que
 estamos definindo uma função. Também abrimos o bloco de codigo com, o já conhecido, ":", que é ultilizado
 em Python para abrir blocos
'''


#    Definindo a primeira função :
def diz_oi():
    print("oi!")
'''
 - Obs.1 : Veja que, dentro das nossas funções, nós podemos ultilizar outras funções
 - Obs.2 : Veja que, nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer "oi!"
 - Obs.3 : Veja que, essa função não recebe nenhum parametro de entrada
 - Obs.4 : Veja que esta função não retorna nada
'''

#    Ultilizando a primeira função definida:
diz_oi()


#    Exemplo 2 :
def cantar_parabens():
    print("Parabens pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")

for n in range(3):
    cantar_parabens()


#    Em python, podemos criar variaveis do tipo de uma função e executar essa função atraves da variavel
canta = cantar_parabens

canta()





