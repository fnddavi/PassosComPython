"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
(a) O nome com todas as letras maiúsculas e minúsculas.
(b) Quantas letras ao todo (sem considerar espaços).
(c) Quantas letras tem o primeiro nome.
"""

nome = input("Nome: ");
nomeSemEspaco = nome.replace(" ", "")
firstSpace = nome.find(" ")

print("a - ", nome.upper(), " ", nome.lower());
print("b - ", len(nomeSemEspaco));
print("c - ", len(nome[:firstSpace]));


# >>> By GPT:
# Solicita o nome completo do usuário:
nome_completo = input("Digite seu nome completo: ")

# Tratando caso a caso, maiusculas e minusculas:
nome_maiusculas = nome_completo.upper()
nome_minusculas = nome_completo.lower()

# (b) Quantidade de letras ao todo (sem considerar espaços)
quantidade_letras = len(nome_completo.replace(" ", ""))

# (c) Quantidade de letras no primeiro nome
primeiro_nome = nome_completo.split()[0]
quantidade_letras_primeiro_nome = len(primeiro_nome)

# Exibe os resultados
print(f"Em maiúsculas: {nome_maiusculas}")
print(f"Em minúsculas: {nome_minusculas}")
print(f"Quantidade de letras (sem espaços): {quantidade_letras}")
print(f"Quantidade de letras no primeiro nome: {quantidade_letras_primeiro_nome}")
