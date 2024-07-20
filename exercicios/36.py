"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, caso contrário, o empréstimo será negado.
"""

from time import sleep

# Entrada de dados
vlrCasa = float(input("Valor do imóvel: "))
sal = float(input("Salário do(s) comprador(es): "))
prazo_m = (
    int(input("Pagamento em quantos anos: ")) * 12)  # Anos*12 para conseguirmos o prazo em meses

# Cálculo da parcela mensal
vlrParcela = vlrCasa / prazo_m
print("Prazo em meses: {:.2f}".format(prazo_m))
print("Parcela: {:.2f}".format(vlrParcela))
print("Limite no salário: {:.2f}".format(sal * 0.3))


# Pausa em segundos
sleep(2)

# Verificação da condição de aprovação do empréstimo
if vlrParcela > (sal * 0.3):
    print("Empréstimo negado. A parcela excede 30% do salário.")

else:
    print("Empréstimo aprovado! O financiamento pode ser realizado.")
