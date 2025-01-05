'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

print(
    "Informe o ano de nascimento de sete pessoas para saber quantas já atingiram a maioridade e quantas ainda não.")


anosVerif = []
for i in range(7):
    anosInsert=int(input(f"{i+1}o ano de nascimento: "))
    anosVerif.append(2025-anosInsert)

print("Idades em ordem de inserção: ", anosVerif)

for i in range(len(anosVerif)):
    if anosVerif[i] >= 18:
        print(f"O {i+1}º individuo já atingiu a maioridade.")
    else:
        print(f"O {i+1}º individuo ainda não atingiu a maioridade.")