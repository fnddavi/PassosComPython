'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"no nome.
'''

nome_ = input("O nome completo: ");
nome_low = nome_.lower();


def verificar_espaco(nome):
    if ' ' not in nome:
        return "É preciso ao menos dois termos no nome." #Não passou aqui (15-07-2024)
    else:
        return "Aguarde..."

verificado = (verificar_espaco(nome_))
if verificado == "Aguarde..." :
    if "silva" in nome_low :
        print("True")
    else:
        print("False")