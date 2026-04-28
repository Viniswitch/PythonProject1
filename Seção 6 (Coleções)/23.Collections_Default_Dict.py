"""
 - Collections - Default Dict (Dicionario)
    Ao criar um dicionario ultilizando o Default Dict, nós informamos um valor default, podendo ultilizar um lambda
    para isso. Este valor será ultilizado sempre que houver um valor definido. Caso tentemos acessar uma chave que não
    existe, essa chave será criada e o valor default" será atribuido

 - lambdas : são funções sem nomes, que podem ou não receber parametros de entrada e retornar valores
"""

#    Recap Dicionarios :
dici = {"nome" : "Viniswitch", "num" : "3.14", "cidade" : "Bezerros" }
print(dici)
print(dici["nome"])
print(type(dici))

#    Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario["nome"] = "Viniswitch"

print(dicionario)
print(dicionario["Não existe"])#    Diferente dos dicionarios normais, esse não gera erro com uma chave inexistente






























