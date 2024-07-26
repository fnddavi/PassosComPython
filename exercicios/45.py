"""
Crie um programa que faça o computador jogar JOKENPÔ com você.
"""

from random import randint

dic = {"a": "Pedra", "b": "Papel", "c": "Tesoura"}

ent = input(" [a]Pedra \n [b]Papel \n [c]Tesoura \n=> ").lower()
sys = randint(1, 3)

if sys == 1:
    print("PC: Pedra")
elif sys == 2:
    print("PC: Papel")
elif sys == 3:
    print("PC: Tesoura")
else:
    print("PC Ta lokão")


if ent in dic:
    print(f"Você {dic[ent]}\n")
    if sys == 3 and ent == "a":
        print("Você Ganhou")
    elif sys == 2 and ent == "c":
        print("Você Ganhou")
    elif sys == 1 and ent == "b":
        print("Você Ganhou")
    else:
        print("Você Perdeu")
else:
    print("Bug, verifica ae")
