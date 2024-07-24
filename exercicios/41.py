'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos é MIRIM; até 14
anos é INFANTIL, até 19 anos é JUNIOR, até 25 anos é SÊNIOR; acima é MASTER
'''

from datetime import datetime

user_DtNasc = int(input('O ano de nascimento: '))
idade = (datetime.today().year - user_DtNasc)


if idade < 9:
    print('Mirim')
elif idade >= 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 25:
    print('Senior')
else:
    print('Master')
