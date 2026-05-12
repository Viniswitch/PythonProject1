x = int(input('Digite o valor iniical : '))

count = 0

while count < 6:
    if x % 2 != 0:
        print(x)
        x = x + 1
        count = count + 1
    elif x % 2 == 0:
        print(x + 1)
        x = x + 2
        count = count + 1

