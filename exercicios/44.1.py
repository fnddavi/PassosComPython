'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
- à vista dinheiro/cheque: 10% DE DESCONTO; 
- à vista no cartão: 5 DE DESCONTO; 
- em até 2x no cartão: PREÇO NORMAL; 
- 3x ou mais no cartão: 20% DE JUROS.
'''
from time import sleep

print('{:=^40}'.format(' Lojas Tabajara '))
print(f"{' Bem Vindo! ':=^40}")

preco = float(input('Valor da compra: '))
modo_pag = input('''Método de pagamento:
                 [a]A vista Dinheiro/Cheque
                 [b]A vista Cartão
                 [c]2x Cartão
                 [d]3x ou + Cartão
                 =>:  ''').lower()


if modo_pag == 'a':
    print(f'Valor a ser pago: R${preco-(preco*0.1):.2f}')
elif modo_pag == 'b':
    print(f'Valor a ser pago: R${preco-(preco*0.05):.2f}')
elif modo_pag == 'c':
    print(f'Valor a ser pago: R${preco}')
elif modo_pag == 'd':
    print(f'Valor a ser pago: R${preco+(preco*0.2):.2f}')
else:
    print('Verifique os valores da compra')
