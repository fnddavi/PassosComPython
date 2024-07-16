'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"no nome.
'''

nome_ = input("O nome completo: ");
nome_low = nome_.lower();

def verificar_espaco(nome):
    if ' ' not in nome:
        print("É preciso ao menos dois termos no nome.")
        return "Erro"
    else:
        print("Aguarde a verificação...")
        return "OK"

verificado = (verificar_espaco(nome_))
if verificado == "OK" :
    if "silva" in nome_low :
        print("Há Silva em seu nome")
    else:
        print("Não há Silva em seu nome")