'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"no nome.
'''

nome_ = input("O nome completo: ");
print("Há Silva em seu nome? {}".format('silva' in nome_.lower()))
