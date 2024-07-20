'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se
já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo.
'''

from datetime import date

print("=" * 75)
print('Serviço militar obrigatório'.center(75))  # Centraliza o texto com 75 caracteres
print("=" * 75)

usr = int(input("Qual a sua idade, Jovem?\n "))
ano = date.today().year
anoNasc = (ano-usr)

if usr < 17:
    print('Relaxa, ainda não precisa se preocupar com isso')
elif usr == 17:
    print(f'Se faz 18 este ano de {ano}, procure o serviço miliar mais proximo e se aliste')
elif usr >= 18:
    print(f'Passou da hora de se alistar! Está atrasado em {(ano-anoNasc)-18} anos.')
