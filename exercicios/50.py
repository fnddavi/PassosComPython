'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

nm=0
for i in range(0, 6):
    nm = int(input(f"{i+1}o Numero: "))

if nm % 2 == 0:
    soma = (nm+nm)
    print(soma)