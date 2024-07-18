"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""

a = int(input("1o: "))
b = int(input("2o: "))
c = int(input("3o: "))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior=a
if b > a and b > a:
    maior = b
if c > a and c > b:
    maior = c

# Mostra os resultados
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
