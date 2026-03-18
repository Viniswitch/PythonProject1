"""
- Estruturas condicionais {if (Se); else; elif}


"""

"""
#    Estrutura condicional if, else em C

if(idade > 18){
    printf("Maior de idade");
}else if(idade == 18){
    printf("Tem 18 anos de idade");
}else{
    printf("É menor de idade");
}
"""

"""
#    Estrutura condicional if, else em Java

if(idade > 18){
    Systen.out.println("Maior de idade");
}else if(idade == 18){
    Systen.out.println("Tem 18 anos de idade");");
}else{
    Systen.out.println("É menor de idade");
"""


idade : int = int (input ("Qual a sua idade ?"))
if idade > 18:
    print("É maior de idade")
elif idade == 18:
    print("Tem 18 anos de idade")
else:
    print("É menor de idade")

#    Outra fornma :
ativo = True
logado = False

if ativo:
    print("Usuario Ativo")
else:
    print("Usuario Inativo. Cheque seu E-mail")

""""
#    Exemplo "feio",sem estruturas condicionais

idade : int = int (input ("Qual a sua idade ?"))
if idade == 18:
    print("Tem 18 anos de idade")
if idade < 18:
    print("É menor de idade")
if idade > 18:
    print("É maior de idade")
"""

