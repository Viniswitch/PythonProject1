#    contador Crescente :

a = int(input("Digite um numero inteiro: "))

for n in range(1, a):
    print(n)

# contador decrescente :

n = int(input("Digite um numero inteiro: "))

count = n

while count > 0:
    print(count)
    count = count - 1


#    Para ordenar em uma ordem especifica :

lista : list[int] = []
while len(lista) < 3:
    valor : int = int(input(f"Informe o valor{len(lista) + 1}/3: "))
    lista.append(valor)
    lista.sort()

print(f"({lista[0]}<{lista[1]}<{lista[2]})")



