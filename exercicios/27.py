'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente. Exemplo: Ana Maria de Souza, primeiro: Ana,
último: Souza.
'''

nome = input("Nome completo: ").split()

# Armazena o primeiro nome (a primeira palavra da lista)
prim_nome = nome[0]

# Armazena o último nome (a última palavra da lista)
ultimo_nome = nome[-1]

print(f"Primeiro nome: {prim_nome} e ultimo nome: {ultimo_nome}")

