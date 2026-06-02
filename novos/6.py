n = int(input("Um numero inteiro: "))
if n < 0:
    print("Numero negativo. Insira um que seja igual ou maior que 0")
else:
    nf = 1
    for i in range(1, n + 1):
        nf *= i
    print(f"Fatorial de {n} é {nf}")
