"""
 -  documentando funções com Docstrings

 - Podemos ter acesso a uma documentação em Python, ultilizando a propiedade especial ".__doc__"
"""


def diz_oi():
    """Uma função simples, que retorna a string "Oi"""
    return "Oi"

print(diz_oi())


def exponencial(numero, pototencia = 2):
    """
    - Função que retorna por padrão o quadrado de numero, ou numero a potencia informada
    :param numero: numero que desejamos gerar o exponencial
    :param pototencia: potencia que desejamos gerar o exponencial, por padrão 2
    :return: retorna o exponencial de numero por potencia
    """
    return numero ** pototencia

print(exponencial(9))







