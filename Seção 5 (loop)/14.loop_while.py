"""
- loop while:

Expressão geral (booleana):
    //execução do loop

#    O bloco do while será repetido em quanto a expressão booleana for verdadeira
(expressão booleana é toda expressão onde todo resultado é veradeiro ou falso)




"""

#    Exemplo 1 de loop while

num= 1#    Variavel iniciada em 1
while num < 10:#    Enquanto a variavel for menor q 10...
    print(num)
    num += 1
#    Importante lembrar de definir um criterio de parada


#    Exemplo 2

resposta = " "
while resposta != "sim":
    resposta = input("Você quer continuar ?")


