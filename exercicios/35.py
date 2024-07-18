"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
"""

r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))


if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")
