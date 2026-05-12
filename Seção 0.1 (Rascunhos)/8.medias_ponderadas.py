n = int(input('Digite um numero inteiro para a quantidade de testes : '))

count = 0

while count < n:
    x = float(input(f'Digite o primeiro valor do teste {count + 1}: '))
    y = float(input(f'Digite o segundo valor do teste {count + 1} : '))
    z = float(input(f'Digite o terceiro valor do teste {count + 1} : '))
    print(f'A media ponderada desses valores é : {(x * 2 + y * 3 + z * 5) / 10}')
    count = count + 1


