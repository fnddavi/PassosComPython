'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cda
km acima do limite.
'''

vel_veiculo = float(input("Velocidade registrada: "))
vel_considerada = vel_veiculo-80
if vel_considerada >= 1:
    print(f'Multado! Excedeu em {vel_considerada} km/h. Multa de {vel_considerada*7} R$')
else:
    print('Não foi desta vez, mas vamos te multar!')

