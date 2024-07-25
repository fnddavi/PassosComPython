'''
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma
mensagem: o primeiro valor é maior; o segundo valor é maior; não existe valor maior, os
dois são iguais.
'''

print('Verificaremos qual numero é maior')
vlr_usr_1 = float(input('Primeiro: '))
vlr_usr_2 = float(input('Segundo: '))

if (vlr_usr_1 < 0) or (vlr_usr_2 < 0):
    print('Ainda não trabalhamos com numeros abaixo de 0')
else:
    if vlr_usr_1 > vlr_usr_2:
        print(f'Valor {vlr_usr_1} é maior!')
    
    elif vlr_usr_2 > vlr_usr_1:
        print(f'Valor {vlr_usr_2} é maior!')

    else:
        print('Os valores são iguais')

