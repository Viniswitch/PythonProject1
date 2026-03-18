"""
 - Mapas : São conhecidos, em Python, como dicionarios
         -Dicionarios, em Pyhton, são representados por chaves

"""

receita = {'Janeiro': 100, 'Fevereiro' : 200, 'Março': 300, 'Abril': 400}
print(receita)

#    Iterando em Dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

for chave in receita:
    print(f'Em {chave} eu recebi: R${receita[chave]}')

print(receita.keys())#    Para listar as chaves

for chave in receita.keys():
    print(receita[chave])

print(receita.values())#    Para listar os valores

for valor in receita.values():
    print(valor)


#    Desempacotamento de dicionarios
print(receita.items())

for chave, receita in receita.items():
    print(f"Chave = {chave} e valor = {valor}")


#    Soma, Valor maximo, valor minimo e tamanho
receita = {'Janeiro': 100, 'Fevereiro' : 200, 'Março': 300, 'Abril': 400}
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))








