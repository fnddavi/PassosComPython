'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''
from datetime import date

ano = int(input("Insira o ano ou 0 para o ano atual "))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 ==0) or (ano % 400==0):
    print(f"{ano} É Bisexto")
else:
    print("{} Não é Bisexto".format(ano))