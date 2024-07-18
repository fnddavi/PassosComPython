"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
"""
retas = []

for i in range(3):
    r = float(input(f'Reta {i+1}: '))
    retas.append(r)
r1, r2, r3 = retas

if ((r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1):
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")
