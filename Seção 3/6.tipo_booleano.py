"""
- Tipo booleano

- 2 constantes, Verdadeiro(True) ou Falso(False)
#    Sempre com a inicial maiuscula

#    Errado: true / false

#    Correto: True / False

"""

ativo = True
print(f'ativo ={ativo}')

"""
- Operações básicas
"""


#    Negação = not
"""
- Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso, e se for
falso, o resultado será verdadeiro. Ou seja, sempre o contrário
"""
print(f'not ativo = {not ativo}')
logado = False
print(f'logado = {logado}')
print(f'not logado = {not logado}')
#    Ou (or)
"""
- É uma operação binária, ou seja, depende de dois valores. ou um ou outro deve ser Verdadeiro
"""
print(f'1.True or True ={True or True}')
print(f'2.True or False ={True or False}')
print(f'3.False or True ={False or True}')
print(f'4.False or False ={False or False}')

print(f'Ativo or Logado = {ativo or logado}')


#    E (and)
"""
- Também é uma operação binaria, ou seja depende de dois valores. Ambos os dois valores devem
ser verdadeiros
"""
print(f'1.True e True ={True and True}')
print(f'2.True and False ={True and False}')
print(f'3.False and True ={False and True}')
print(f'4.False and False ={False and False}')

print(f'Ativo and Logado = {ativo and logado}')
