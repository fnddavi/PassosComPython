'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
- à vista dinheiro/cheque: 10% DE DESCONTO; 
- à vista no cartão: 5 DE DESCONTO; 
- em até 2x no cartão: PREÇO NORMAL; 
- 3x ou mais no cartão: 20% DE JUROS.
'''
from time import sleep

preco = float(input('Valor da compra: '))
modo_pag = input('''Método de pagamento:
                 [a]A vista Dinheiro/Cheque
                 [b]A vista Cartão
                 [c]2x Cartão
                 [d]3x ou + Cartão
                 =>:  ''').lower()

# Definir um dicionário com algumas chaves e valores
dicio = {
    'a': 'A vista Dinheiro/Cheque',
    'b': 'A vista Cartão',
    'c': '2x Cartão',
    'd': '3x ou + Cartão'
}

# Verificar se a entrada está no dicionário
if modo_pag in dicio:
    print(f"{modo_pag}: {dicio[modo_pag]}")
    sleep(1)
else:
    print("Letra não encontrada no dicionário.1")

if modo_pag in dicio:
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
else:
    print("Letra não encontrada no dicionário.2")
