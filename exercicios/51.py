"""
Desenvolva um programa que leia o primeiro termo e a razão e uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

print("\nVamos calcular uma PA simples. Abaixo digite o Primeiro termo e a razão!\n")
ter = int(input("Primeiro termo: "))
raz = int(input("Razão: "))

termos = []
cont = 0

while cont < 10:
    termos.append(ter)
    ter += raz
    cont += 1

print(termos)
