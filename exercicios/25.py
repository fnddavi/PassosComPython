'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"no nome.
'''

nome_ = input("O nome completo: ").lower()

if "silva" in nome_:
    print("Há Silva em seu nome")
else:
    print("Não há Silva em seu nome")
