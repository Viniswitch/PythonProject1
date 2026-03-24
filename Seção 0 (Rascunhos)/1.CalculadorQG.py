QG1 = int(input('Nota do QG 1 ?'))
QG2 = int(input('Nota do QG 2 ?'))
print(f'Nota do QG 1 : {QG1}')
print(f'Nota do QG 2 : {QG2}')

media = (QG1 * 2 + QG2 * 3)/ 5
print(f'Nota média = {media}')

if media >= 7:
    print('Aprovado')

if media < 7 :
    print("Reprovado nas provas")
    final = int(input('Qual é a nota da final ?'))
    if final >= 5:
         print('Aprovado')
    else:
        print('Reprovado')
if media < 3:
    print('Reprovado')



