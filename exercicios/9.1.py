# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

nm=int(input('Numero: '))
tb = 0
while tb<=10:
    print(f'{nm} x {tb} = {nm*tb}')
    tb+=1