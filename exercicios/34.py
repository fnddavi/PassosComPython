'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os
inferiores o iguais, o aumento é de 15%.
'''

slr = float(input('Digite o salário do funcionário: '))

if slr <= 1250:
    print(f"Com aumento de 15%: R${(slr*0.15)+slr}")
else:
    print(f"Com aumento de 10%: R${(slr*0.10)+slr}")
