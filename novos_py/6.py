# Calcula o fatorial de um número inteiro não-negativo fornecido pelo usuário.
# Pede ao usuário um número inteiro e converte a entrada para `int`.
n = int(input("Um numero inteiro: "))

# Se o número for negativo, o fatorial não é definido (neste programa
# apenas avisamos o usuário). Caso contrário, calculamos o fatorial.
if n < 0:
    # Mensagem de erro para entrada inválida (número negativo).
    print("Numero negativo. Insira um que seja igual ou maior que 0")
else:
    # `nf` guarda o valor do fatorial acumulado. Começamos em 1 porque
    # o fatorial de 0 é 1 e multiplicar por 1 não altera o resultado.
    nf = 1

    # Laço que multiplica `nf` por cada inteiro de 1 até `n` (inclusivo).
    # Após o laço, `nf` conterá n! (n fatorial).
    for i in range(1, n + 1):
        nf *= i  # equivalente a: nf = nf * i

    # Exibe o resultado formatado ao usuário.
    print(f"Fatorial de {n} é {nf}")
