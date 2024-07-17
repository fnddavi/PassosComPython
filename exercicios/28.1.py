'''
Escreva um programa que faça o computador "pensar"em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O
programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random

user_num = int(input("Digite um número de 0 a 5: "))
sis_num = random.randint(1, 5)

if 1 <= user_num <= 5:
    if user_num == sis_num:
        print("Acertou!")
    else:
        print("Errou! O Número sorteado é {}".format(sis_num))
else:
    print('Inseriu um numero fora do que foi solicitado...')
