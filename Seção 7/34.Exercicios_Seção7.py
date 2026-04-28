"""
1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.
"""

#    Resolução :
'''
def dobro(num):
    print(f'O dobro de {num} é : {num * 2}')

dobro(float(input('Digite um numero : ')))


#    Correção do professor :
def dobro(numero: int) -> int:
    return numero * 2

if __name__ == '__main__':
    valor: int = 4
    print(f'O dobro de {valor} é : {dobro(valor)}')
'''

"""
2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 20204”.
"""
'''
#    Resolução :

data = list(str(input('Digite uma data : ')).split('/'))
meses = {1 : "Janeiro", 2 : "Fevereiro", 3 : "Março", 4 : "Abril", 5 : "Maio", 6 : "Junho", 7 : "Julho",
       8 : "Agosto", 9 : "Setembro", 10 : "Outubro", 11 : "Novembro", 12 : "Dezembro" }
month = ()

for chave, valor in meses.items():
    if int(data[1]) == chave:
        month = valor

def new_data(day, month, year ):
    print(f'É dia {day} de {month} de {year}')

new_data(day = data[0] , month = month, year = data[2])


#    Correção do professor :
def data_extenso(data: str) -> None:
    d = data.split('/')

    dia: int = int(d[0])
    mes: int = int(d[1])
    ano: int = int(d[2])

    if mes == 1:
        mes_string = 'Jan'
    elif mes == 2:
        mes_string = 'Feb'
    elif mes == 3:
        mes_string = 'Mar'
    elif mes == 4:
        mes_string = 'Abril'
    elif mes == 5:
        mes_string = 'Maio'
    elif mes == 6:
        mes_string = 'Junho'
    elif mes == 7:
        mes_string = 'Julho'
    elif mes == 8:
        mes_string = 'Agosto'
    elif mes == 9:
        mes_string = 'Setembro'
    elif mes == 10:
        mes_string = 'Outubro'
    elif mes == 11:
        mes_string = 'Novembro'
    elif mes == 12:
        mes_string = 'Dezembro'
    else:
        mes_string = 'Desconhecido'

    print(f'Dia {dia} de {mes_string} de {ano}')


if __name__ == "__main__":
    data_extenso('01/01/2024')

'''

"""
3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""

#    Resolução :
'''
def maior(lista):
    return max(lista)

entrada = input("Digite números separados por espaço: ").split()

lista = []
for n in entrada:
    lista.append(int(n))

print(maior(lista))


#    Correção do professor :
def maior(inteiros: list[int]) -> int:
    return max(inteiros)

if __name__ == '__main__':
    lista: list[int] = [2, 5, 0, 9, 83]
    print(f'O maior valor na lista {lista} é {maior(lista)}')
'''



