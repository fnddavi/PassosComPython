'''
Crie um programa que faça o computador jogar JOKENPÔ com você.
'''

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
sys = randint(0,2)

print('Jô')
print('Ken')
print('Pô \n')
sleep(1)

usr = int(input(' [0]Pedra \n [1]Papel \n [2]Tesoura \n=> '))
print(f'PC Escolheu {itens[sys]}')
print(f'Você Escolheu {itens[usr]}')

if sys == 0:
    if usr == 0:
        print('Empatou')
    elif usr == 1:
        print('Você Ganhou')
    else:
        print('Você Perdeu')

elif sys == 1:
    if usr == 0:
        print('Você perdeu')
    elif usr == 1:
        print('Empatou')
    else:
        print('Você ganhou')

elif sys == 2:
    if usr == 0:
        print('Você Ganhou')
    elif usr == 1:
        print('Você Perdeu')
    else:
        print('Empatou')
else:
    print('Erro. Verifique!')