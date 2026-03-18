"""
- Estruturas logicas {and (e); or (ou); not (não); is (é).

- Operadores unários
    -not : Para o 'not' o valor é invertido

- Operadores binários
    -and : Para o 'and', ambos os valores precisam ser True
    -or : Para o 'or', um ou outro valor precisa ser True
    -is : Para o 'is' o valor é comparado à outro

"""

#    Exemplo para o and:
print('- Exemplo do "and" :')
ativo = False
logado = True

if ativo and logado:
    print('Bem-vindo Usuario')
else:
    print('Você precisa acessar sua conta. Por favor, cheque o seu E-mail')

#    Exemplo para o or:
print('- Exemplo do "or" :')
ativo = False
logado = True

if ativo or logado:
    print('Bem-vindo Usuario')
else:
    print('Você precisa acessar sua conta. Por favor, cheque o seu E-mail')


#    Exemplo para o not:
print('- Exemplo do "not" :')
ativo = True
logado = True
if not ativo:
    print('Você precisa ativar a sua conta. Por favor, cheque o seu E-mail')
else :
    print('Bem-vindo Usuario')

#    Exemplo para o is:
print('- Exemplo do "is" :')
"""
 #    Forma errada :

ativo = True
logado = False

if ativo is True:
    print('E-mail está ativo')
else:
    print('E-mail está inativo')
if logado is True:
    print('Usuario logado')
else:
    print('Usuario Deslogado')

"""

ativo = True
logado = False

if ativo:
    print('Bem-vindo Usuario')
else:
    print('Você precisa ativar sua conta. cheque seu E-mail')

#    ativo é falso ?:
print(ativo is False)
#    ativo é verdadeiro ?:
print(ativo is True)

