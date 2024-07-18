'''
Escreva um programa que faça o computador "pensar"em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O
programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep
from colorama import Fore, Back, Style, init

init()

user_num = int(input("Digite um número de 0 a 5: "))
sis_num = randint(1, 5)

print('___' *10)
print("Aguarde...")
print('___' *10)
sleep(3)

if 1 <= user_num <= 5:
    if user_num == sis_num:
        print("Acertou!")
    else:
        print(Fore.RED + Back.WHITE + "Errou! O Número sorteado é {}".format(sis_num) + Style.RESET_ALL)
else:
    print(Fore.RED + Back.WHITE + 'Inseriu um numero fora do que foi solicitado...' + Style.RESET_ALL)
