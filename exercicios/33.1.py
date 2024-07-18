"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""

nrs = []

for i in range(3):
    n = int(input(f"Número {i+1}: "))
    nrs.append(n)

n1, n2, n3 = nrs

# Sugestão By GPT:
# Inicializa as variáveis de maior e menor com o primeiro número
maior = menor = n1

# Verifica se o segundo número é maior ou menor
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

# Verifica se o terceiro número é maior ou menor
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

# Mostra os resultados
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
