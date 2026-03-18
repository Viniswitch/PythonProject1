"""
- Recebendo dados do usuario
- input() -> todo dado recebido via input é string

Em python "string" é tudo que estiver entre:
-Aspas simples:    'Viniswitch'
-Aspas duplas:    "Viniswitch"
-Aspas simples triplas:    '''Viniswitch'''
-Aspas duplas triplas

"""

#    Entrada de dados:
#    print("Qual é o seu nome ?")
#    nome = input()  #input -> entrada
nome=input("Qual é o seu nome ?")

#    Exemplo de print "Antiquado"2.x
#    print('Seja bem vindo(a) %s' % nome)

#    Exemplo de print "Moderno"3.x
#    print("Seja bem vindo(a) {0}".format(nome))
# Exemplo de print "Mais moderno" 3.7
print(f'Seja bem vindo(a) {nome}')

#    print("Qual é a sua idade ?")
#    idade = input()
idade=input("Qual é a sua idade ?")

#    Processamento

#    Saida
#    Exemplo de print "Antiquado"2.x
#    print('A %s tem %s anos' % (nome, idade))

#    Exemplo de print "Moderno"3.x
#    print("A {0} tem {1} anos de idade".format (nome,idade))
#    Exemplo de print "Mais moderno"3.7
print(f'A {nome} tem {idade} anos')

"""
#    int(idade) -> cast

- cast é a "conversão" de um tipo de dado para outro
"""
print(f'A {nome} nasceu em {2025 - int(idade)}')
