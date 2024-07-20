'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 pra binário; 2 para octal; 3 para hexadecimal
'''

print('='*60)
print('Aqui você pode converter numeros da base decimal para a base binária, octal ou hexadecimal\nInsira abaixo um numero que deseja converter')
print('='*60)

vlr_usr = int(input("Valor: "))

print('''Insira abaixo para qual base deseja converter:\n
      2 - para binaria\n
      8 - para octal\n
      16 - para hexadecimal\n''')

vlr_bs = int(input("Base: "))

if vlr_bs == 2:
    vlrBin = bin(vlr_usr)
    print (f'Valor binário de {vlr_usr} é {vlrBin}')
elif vlr_bs == 8:
    vlrOct = oct(vlr_usr)
    print (f'Valor octal de {vlr_usr} é {vlrOct}')
elif vlr_bs == 16:
    vlrHex = hex(vlr_usr)
    print (f'Valor octal de {vlr_usr} é {vlrHex}')
else:
    print('Inseriu algum valor errado. Verifique e tente novamente')
