x = int(input('Digite o primeiro valor : '))
y = int(input('Digite o segundo valor : '))

soma = 0

for i in range(x + 1, y):
    if i % 2 != 0:
        print(i)
        soma = soma + i

print(soma)

