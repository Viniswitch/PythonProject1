N = int(input('Digite a quantidade de valores'))

for i in range(N):
    x = int(input(f'Digite o valor {i}/{N} : '))

    if x == 0:
        print("NULL")

    elif x % 2 == 0 and x > 0:
        print("EVEN POSITIVE")

    elif x % 2 == 0 and x < 0:
        print("EVEN NEGATIVE")

    elif x % 2 != 0 and x > 0:
        print("ODD POSITIVE")

    else:
        print("ODD NEGATIVE")