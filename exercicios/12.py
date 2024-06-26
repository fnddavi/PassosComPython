# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prc = float(input("Preco do produto: "))
nvVal = prc-(prc*0.05)
print('Novo valor: R$', nvVal)