'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''

ano = int(input("Qual o ano? "))

if ano % 400 == 0:      # (*)
    print('Bisexto')
elif ano % 100 == 0:    # (*)
    print('Não Bisexto')
elif ano % 4 == 0:      # (*)
    print('Bisexto')
else:                   # (**)
    print('Não Bisexto')

# (*)Executado se a condição for verdadeira, se não, passa a proxima condicao
# (**) Executado se as condicoes anteriores não satisfazerem
