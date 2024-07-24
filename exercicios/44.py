'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
- à vista dinheiro/cheque: 10% DE DESCONTO; 
- à vista no cartão: 5 DE DESCONTO; 
- em até 2x no cartão: PREÇO NORMAL; 
- 3x ou mais no cartão: 20% DE JUROS.
'''

preco = float(input(''))

#ByGPT

# Definir um dicionário com algumas chaves e valores
dicionario = {
    'maçã': 'uma fruta doce',
    'banana': 'uma fruta amarela',
    'cenoura': 'um vegetal laranja'
}

# Solicitar entrada do usuário
entrada = input("Digite uma palavra: ")

# Verificar se a entrada está no dicionário
if entrada in dicionario:
    print(f"{entrada}: {dicionario[entrada]}")
else:
    print("Palavra não encontrada no dicionário.")
