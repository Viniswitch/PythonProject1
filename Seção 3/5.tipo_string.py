"""
- Tipo string
Em python, um dado é considerado tipo string quando:
1.Estiver entre aspas simples Ex.:('Viniswitch') ou ('02')
2.Sempre que estiver entre aspas duplas Ex.:("Viniswitch") ou ("02")
3.Sempre que estiver entre aspas simples triplas Ex.:('''Viniswitch''') ou ('''02''')
4.Sempre que estiver entre aspas duplas triplas

"""

#    Exemplo de string 1
nome = 'Viniswitch'
print(nome)
print(type(nome))

#    Exemplo de string 2
nome = "02"
print(nome)
print(type(nome))

#    Exemplo de string 3
nome = '''True'''
print(nome)
print(type(nome))

#    Exemplo de string 4
nome = """1,4"""
print(nome)
print(type(nome))


#    para dar enter
nome = """Wells \n404"""
print(nome)
print(type(nome))


#    Para deixar em capslock
nome = "viniswitch"
print(nome.upper())


#    Para listar as palavras
nome = "O Senhor Dos Aneis"
print(nome.split())


#    Para selecionar "até onde" o print é selecionado (Slice de string)
nome = "As Cronicas De Narnia"
#    Usar [] e :
#    O caractere inicial é 0. O ultimo é o numero seguinte
print(f'Para listar o nome ={nome.split()}')
print(f'Para selecionar o intervalo de 0/11 ={nome[0:11]}')
print(f'Para selecionar o intervalo 12/21 ={nome[12:21]}')
#    para inverter a ordem multiplicar por -1
print(f'Para inverter tudo ={nome[::-1]}')


#    Para selecionar as partes da string
print(nome.split()[0], nome.split()[1], nome.split()[2], nome.split()[3])


#    Para trocar as letras
nome = "Banana"
print(nome)
print(nome.replace('a', 'e'))
print(type(nome))

