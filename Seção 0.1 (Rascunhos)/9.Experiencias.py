n = int(input('Quantiade de testes : '))

coelhos = 0
ratos = 0
sapos = 0

for i in range(n):

    qtd, tipo = input("Qual a quantidade e o tipo : ").split()
    qtd = int(qtd)

    if tipo == "C":
        coelhos = coelhos + qtd

    elif tipo == "R":
        ratos = ratos + qtd

    elif tipo == "S":
        sapos = sapos + qtd

total = coelhos + ratos + sapos

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")

print(f"Percentual de coelhos: {(coelhos / total) * 100:.2f} %")
print(f"Percentual de ratos: {(ratos / total) * 100:.2f} %")
print(f"Percentual de sapos: {(sapos / total) * 100:.2f} %")