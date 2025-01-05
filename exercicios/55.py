'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

pesos = []
for p in range(5):
    peso = float(input('Digite o peso da pessoa: '))
    pesos.append(peso)

if len(pesos) > 0: # Verifica se a lista de pesos não está vazia
    maior_peso = pesos[0] # Inicializa com o primeiro valor, que é o maior peso até o momento
    menor_peso = pesos[0] # Inicializa com o primeiro valor, que é o menor peso até o momento
    for peso in pesos: # Itera sobre a lista de pesos
        if peso > maior_peso: # Compara o peso atual com o maior peso
            maior_peso = peso  # Atualiza o maior peso
        if peso < menor_peso: # Compara o peso atual com o menor peso
            menor_peso = peso # Atualiza o menor peso
    print(f'O maior peso lido foi {maior_peso}kg e o menor peso lido foi {menor_peso}kg.')
else:
    print('Nenhum peso foi lido.')
