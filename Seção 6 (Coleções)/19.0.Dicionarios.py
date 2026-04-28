"""
 - Dicionarios : São coleções de chave/valor
Obs: Em algumas linguagens de programação, dicionários são conhecidos por mapas, por serem coleções de chave/valor

Chave : [0,  1, 2, 3,  4,  5]
Valor :[10, 44, 3, 93, 22, 17]

 - Sobre dicionarios:
#    Dicionários são representado por chaves "{}"
#    chave e valor são separados por dois pontos ":"
#    Tanto chave quanto valor podem ser de qualquer tipo de dado
#    Podemos misturar diferentes tipos de dados
#    Podemos usar qualquer tipo de dado, tipo:"int", "float", "str", "booleano", "lista", "tupla"...

"""

#    - Criação de dicionários:

#   Forma 1 : (Mais Comum)
paises = {"br" : "Brasil", "eua" : "Estados Unidos", "arg" : "Argentina"}
#        {chave : valor,   chave : valor,            chave : valor      }

print(paises)
print(type(paises))


#   Forma 2 : (Menos Comum)
paises = dict(br="Brasil", eua="Estados Unidos", arg="Argentina")
print(paises)
print(type(paises))


#    - Acessando elementos

#    Forma 1 : Acessando via chave(Parecido com lista/tupla)
tipo = {"fire" : "Charmander", "watter" : "Squirtle", "leaf" : "bulbasaur"}

print(tipo["fire"])
print(tipo["watter"])
#    print(tipo["inexistente"]) vai gerar um erro, caso a chave não exista

#    Forma 2 : Acessando via "get" (Forma mais recomendada)
paises = {"br" : "Brasil", "eua" : "Estados Unidos", "arg" : "Argentina"}

print(paises.get("br"))
print(paises.get("arg"))
print(paises.get("inexistente"))#    vai gerar o tipo de dado "none"


#    - Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

#    forma 1 :
paises = {"br" : "Brasil", "eua" : "Estados Unidos", "arg" : "Argentina"}
pais = paises.get("ru", "Não existe")

print(pais)

#    Forma 2: (forma grande)
paises = {"br" : "Brasil", "eua" : "Estados Unidos", "arg" : "Argentina"}
pais = paises.get("ru")

if pais:
    print(f"Encontrei o país {pais}")
else:
    print("Não encontrei o país")


#    Podemos verificar se determinada chave se encontra em um dicionario
tipo = {"fire" : "Charmander", "watter" : "Squirtle", "leaf" : "bulbasaur"}

print("fire" in tipo)
print("leaf" in tipo)
print("Squirtle" in tipo)



lugares = {
    (35.6895, 39.6917) : "Escritorio em Tokyo",
    (40.7128, 74.0060) : "Escritorio em Nova York",
    (37.7749, 122.4194): "Escritorio em São Paulo",
}

print(lugares)
print(type(lugares))


#    Adicionar elementos em um dicionario
Lucro = {"Janeiro" : 425, "Fevereiro" : 241, "Março" : 124, "Abril" : 679}
print(Lucro)
print(type(Lucro))

#    Forma 1
Lucro["Maio"] = 567
print(Lucro)

#    Forma 2
novo_dado = {"Junho" : 342}
Lucro.update(novo_dado)#    Lucro.update({"Junho" : 342})
print(Lucro)


#    Atualizando dados em um dicionario

#    Forma 1 :
Lucro["Maio"] = 550
print(Lucro)

#    Forma 2 :
Lucro.update({"Junho" : 660})
print(Lucro)

'''
#    Conclusão 1 : O metodo para adicionar novos alementos e atualizar elementos já existentes é o mesmo

#    Conclusão 2 : Em dicionarios, não podemos ter chaves repetidas
'''


#    Como remover dados de um dicionario
Lucro = {"Janeiro" : 425, "Fevereiro" : 241, "Março" : 124, "Abril" : 679, "Maio" : 550, "Junho" : 660}
print(Lucro)

#    Forma 1:
Lucro.pop("Junho")
print(Lucro)

#    Desse modo, sempre, será necessaario informar a chave. Se não, haverá erro

#    Forma 2 :
luc = Lucro.pop("Maio")
print(luc)

print(Lucro)

#    desse modo, ao removermos um objeto, esse objeto será retornado

#    Forma 3 :
del Lucro["Abril"]
print(Lucro)

#    Neste caso o valor removido não é retornado
#    Se a chave não existir haverá erro


#    Imagine que você está criando um carrinho de compras
'''
Carrinho de Compras
    Produto 1 :
        - nome;
        - quantidade;
        - preço
    Produto 2 :
        - nome;
        - quantidade;
        - preço;
'''

#    Forma 1 : Ultilizando listas
carrinho = []

produto1 = ["playstation 5", 1, 3500.00]

produto2 = ["Nintendo switch 2", 1, 4000.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#    Nesse caso, teriamos que saber qual é o indice de cada informação do produto

#    Forma 2 : Ultilizando tulplas
produto1 = ("Katana", 1, 500.00)

produto2 = ("Sabre de Luz", 1, 400.00)

carrinho = [produto1, produto2]
print(carrinho)

#    Nesse caso, ainda teriamos que saber qual é o indice de cada informação do produto

#    Forma 3 : Ultilizando dicionarios
carrinho = []

produto1 = {"Nome" : "Impressora 3d", "Quantidade" : 1, "Preço" : 900.00}

produto2 = {"Nome" : "Guitarra", "Quantidade" : 1, "Preço" : 1500.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

produto1["Preço"] = 1000
print(carrinho)

#    Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
#    Tambem temos mais certeza da informação de cada produto


#    Para limpar um dicionario:
valor = dict(x=1, y=2, z=3)#    Não esta de acordo com o pep8

print(valor)
print(type(valor))

valor.clear()
print(valor)
print(type(valor))


#    Copiando um dicionario para outro :
valor = dict(x=1, y=2, z=3)#    Não esta de acordo com o pep8

#    Forma 1 : Deep Copy
novo = valor.copy()
print(novo)

valor["a"] = 10
print(valor)
print(novo)

#    Forma 2 : Shallow Copy
valor = dict(x=1, y=2, z=3)
novo = valor
print(novo)
novo["a"] = 40
print(valor)
print(novo)


#    Forma não usual de criação de dicionarios
outro = {}.fromkeys("a", "b")

print(outro)
print(type(outro))


usuario = {}.fromkeys(["nome", "pontos", "email", "profile"], "desconhecido")
print(usuario)
print(type(usuario))
'''
- O metodo fromkeys recebe dois parametros: Um iteravel e um valor
- Ele vai gerar para cada valor iteravel uma chave, e irá atribuir a essa chave o valor informado'''

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), "novo")
print(veja)












