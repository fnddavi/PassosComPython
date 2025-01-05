'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
(a) A média de idade do grupo.
(b) Qual é o nome do homem mais velho.
(c) Quantas mulheres têm menos de 20 anos.
'''

nomes = []
idades = []
sexos = []

for i in range(4):
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa: ')
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

print (f'A média de idade do grupo é {sum(idades)/len(idades)} anos.')
print(f'O homem mais velho é {nomes[idades.index(max(idades))]}')
print(f'{sexos.count("F") if "F" in sexos else 0} mulheres têm menos de 20 anos.')