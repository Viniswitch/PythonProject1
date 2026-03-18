"""
PEP8 - Python enhancement proposal

São propostas de melhorias para a linguagem Python

The Zen Of Python

Import This

A ideia do PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Ultilize Camel Case para nomes de classes:


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Ultilize nomes em minusculo, separados em "_" para funções ou variaveis:

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5


[3] - Ultilize 4 espaços para Identação!!!!!

if "a" in "banana":
    print("tem")


[4] - Linhas em branco:
-Separar as funções e definições de classe em (2)duas linhas em branco;
-Métodos dentro de uma classe devem ser separados com 1 unica linha em branco;

[5] - Imports:
-Imports devem sempre ser feitos em linhas separadas;

# Import Errado

import sis, os

# Import Certo
import sys
import os

# Não há problemas em ultilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer
# comentarios ou docstrings e antes de constantes ou variaveis globais

[6] - Espaços em instruções e impressões

# Não faça:
funcao( algo[ 1 ], { outro: 2 } )

# Faça:
funcao(algo[1], {outro: 2})

#Não faça:
algo (1)

# Faça:
algo(1)

# Não faça
dict ["chave"] = list[indice]

# Faça:
dict["chave"] = list[indice]

# Não faça
x              = 1
y              = 3
variavel_longa = 5

# Faça
x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""
import this


