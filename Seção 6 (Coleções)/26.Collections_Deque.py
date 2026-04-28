"""
 - Collections - Deque : É uma lista de alta performance

"""


#    Fazendo o import
from collections import deque


#    Criando deques :

deq = deque("Viniswitch")
print(deq)
print(type(deq))


#    Adicionando elementos no deque
deq.append("2026")#    Adiciona o elemento no final
print(deq)

deq.appendleft("2077")#    Adiciona à esquerda da lista
print(deq)


#    Remover elementos
print(deq)
print(deq.pop())#    Remove e retorna o ultimo elemento
print(deq)
print(deq.popleft())
















