"""
 - Set Comprehension :

 Lista = [1, 2, 3, 4]

 Set = {1, 2, 3, 4}
"""


#    Exemplo 1 :
numeros ={num for num in range(1,11)}
print(numeros)


#    Exemplo 2 (Set para Dict):
numeros = {x : x ** 2 for x in range(1,11)}
print(numeros)


#    Exemplo 3 :
letras = {letra for letra in "Viniswitch"}
print(letras)





