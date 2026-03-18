"""
-Saindo de loops com o Break



"""

#    Exemplo 1

for num in range(1, 10):
    if num == 5:
        break
    else:
        print(num)
print("Saindo do loop")


#    Exemplo 2

while True:
    comando = input('Digite "Sair" para sair')
    if comando == "Sair": break
    