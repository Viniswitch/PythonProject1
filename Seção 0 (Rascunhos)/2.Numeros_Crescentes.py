lista : list[int] = []
while len(lista) < 3:
    valor : int = int(input(f"Informe o valor{len(lista) + 1}/3: "))
    lista.append(valor)
    lista.sort()

print(f"({lista[0]}<{lista[1]}<{lista[2]})")

