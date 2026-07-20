# Conjunto de vogais (minúsculas e maiúsculas) usado para verificação
vogals = "aeiouAEIOU"

# Lê uma frase fornecida pelo usuário
phrase = input("Insira uma Frase: ")

# Contador inicializado em zero
count = 0

# Itera por cada caractere da frase e incrementa `count` quando
# o caractere está presente na string `vogals`.
for char in phrase:
    if char in vogals:
        count += 1

# Exibe o número total de vogais encontradas na frase
print(f"Numeros de vogais na frase é {count}")
