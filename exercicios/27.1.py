"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente. Exemplo: Ana Maria de Souza, primeiro: Ana,
último: Souza.
"""

nome = input("Nome completo: ")


def verificar_espaco(n):
    if " " not in n:
        print("É preciso ao menos dois termos no nome.")
        return "Erro"
    else:
        print("Aguarde a verificação...")
        return "OK"


nome_ok = verificar_espaco(nome)

if nome_ok == "OK":
    nome_new = nome.split()
    prim_nome = nome_new[0]
    ultimo_nome = nome_new[-1]
    print(f"Primeiro nome: {prim_nome} e ultimo nome: {ultimo_nome}")
else:
    print("Deu erro")

