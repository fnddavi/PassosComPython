'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

pesos = []
for p in range(5):
    peso = float(input('Digite o peso da pessoa: '))
    pesos.append(peso)

print(f'O maior peso lido foi {max(pesos)}kg e o menor peso lido foi {min(pesos)}kg.')
