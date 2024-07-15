'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o
nome "SANTO"
'''

nome_cidade = str(input("Nome da cidade: "));
novo_cidade = nome_cidade.lower();

if "sant" in novo_cidade or "são" in novo_cidade:
    print("Cidade inicia com 'Santo(a)/São'");
else:
    print("Não contém 'Santo(a)/São' no nome da cidade");
