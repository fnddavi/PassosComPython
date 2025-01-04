"""
Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços. Exemplo: apos a sopa é um políndromo.
"""

# Lê a frase digitada pelo usuário, remove espaços no início e no final, e converte para minúsculas
in_frase = str(input("Digite uma frase: ")).strip().lower()

# Remove todos os espaços da frase
frase = in_frase.replace(" ", "")

# Verifica se a frase sem espaços é igual à sua inversa
if frase == frase[::-1]:
    # Se for igual, é um palíndromo
    print(f"A frase '{in_frase}' é um palíndromo.")
else:
    # Se não for igual, não é um palíndromo
    print(f"A frase '{in_frase}' não é um palíndromo.")
#
