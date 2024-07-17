'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''

ano = int(input("Quao o ano? "))

if ano % 4 == 0:
    if ano % 100 ==0 :
        if ano % 400==0:
            print("Bisexto")
        else:
            print("Não Bisexto")
    else:
        print("Bisexto")
else:
    print("Não Bisexto")