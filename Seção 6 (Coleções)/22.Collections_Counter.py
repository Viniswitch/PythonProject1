"""
 - Collections - Counter(Contador):

 - Collections : Hight-performance Container Datetypes
               "tipos de dado container de alta performance"

 - Counter : Recebe um iteravel qualquer, como parametro e cria um objeto do tipo Collections counter, que é parecido
 com dicionarios, contendo como chave o elemento da lista passado como parametro e como valor a quantidade
 de elementos desse elemento


"""

#    Ultilizando o Counter
from collections import Counter

#    Exemplo 1 :

lista = [1, 1, 1, 2, 2, 3, 4, 4, 4, 1, 1, 2, 3, 5, 5, 5, 2]

res = Counter(lista)

print(res)
print(type(res))

#    Exemplo 2 :
name = "Viniswitch"
res = Counter(name)
#    print(Counter(name)) dá no mesmo
print(res)
print(type(res))

#    Exemplo 3 :
texto = '''Cyberpunk 2077 é um jogo eletrônico de RPG de ação desenvolvido pela CD Projekt Red e publicado pela
 CD Projekt. A história do jogo é ambientada em Night City, um mundo aberto situado no universo fictício de Cyberpunk.
Ele é jogado a partir de uma perspectiva em primeira pessoa, com os jogadores controlando um mercenário personalizável
conhecido como V, que pode adquirir habilidades de hacking e maquinários, um arsenal de armas de longo alcance e opções
de combate no estilo corpo a corpo. A trama segue a luta de V enquanto tenta lidar com um misterioso implante
cibernético que ameaça substituir seu corpo com a personalidade e as memórias de uma celebridade falecida perceptível 
apenas por V; os dois devem trabalhar juntos se houver alguma esperança de separar os dois e salvar a vida de V'''

palavras = texto.split()
#    print(palavras)

res = Counter(palavras)
print(res)
print(Counter(texto))

print(res.most_common(5))#    Para mostrar as 5 palavras mais repetidas

