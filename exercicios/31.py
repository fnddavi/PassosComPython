'''
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o
preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para
viagens mais longas.
'''

user_dist = float(input('Distancia: '))
if user_dist<=200:
    print(f'Custo da viagem será de R${user_dist*0.5:.2f}')
else:
    print(f'Custo da viagem sera de R${user_dist*0.45:.2f}')
